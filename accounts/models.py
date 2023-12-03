from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    development_field = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    profile_image = models.ImageField(upload_to='accounts/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return f'/accounts/profile/{self.pk}'
