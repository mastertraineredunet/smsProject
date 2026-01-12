from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    branch = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    # def __str__(self):
    #     return f"{self.user.username}'s profile"