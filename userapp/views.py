from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    # Handle user signup
    if request.method == 'POST':
        # Process the signup form
        form = UserCreationForm(request.POST)
        # Validate and save the new user
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    # Handle user login
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        #it authenticate user and return user object
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to a home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    # Handle user logout
    logout(request)
    return redirect('login')  # Redirect to login page after logout
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')