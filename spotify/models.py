from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

import pycountry
from .utils import generate_random_username

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=150, unique=True, default=generate_random_username)
    display_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) # Hashed password will be stored
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # Gender
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
        ('non_binary', 'Non-binary'),
    ]  
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='prefer_not_to_say')

    # Account status
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    # Email Verified
    email_verified = models.BooleanField(default=False)

    # Subscription/Plan
    SUBSCRIPTION_CHOICES = [
        ('free', 'Free'),
        ('invidual', 'Individual'),
        ('student', 'Student'),
        ('duo', 'Duo'),
        ('family', 'Family')
    ]
    subscription_type = models.CharField(max_length=20, choices=SUBSCRIPTION_CHOICES, default='free')

    # Country/Region
    COUNTRY_CHOICES = [(country.name, country.name) for country in pycountry.countries] + [('None', 'None')]
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='None')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Check if password is already hashed
        if not self.password.startswith('pbkdf2_'):  # To avoid rehashing if already hashed
            self.password = make_password(self.password)

        # Ensure that user_name is unique
        while User.objects.filter(user_name=self.user_name).exists():
            self.user_name = generate_random_username()

        # Save changes
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name