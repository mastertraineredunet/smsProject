from .models import UserProfile
from django import forms
class profileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'mobile_number', 'address', 'branch', 'dob', 'gender']
