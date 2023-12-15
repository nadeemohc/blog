from django.db import models

# Create your models here.
GENDER_CHOICES = [
    ('', 'Select Gender'),
    ('M', 'Male'),
    ('F', 'Female'),
]

class UserProfile(models.Model):
    username = models.CharField(unique=True)
    gender = models.CharField(choices=GENDER_CHOICES)
    email = models.CharField(unique=True)
    password = models.CharField()

    def __str__(self):
        return self.username
