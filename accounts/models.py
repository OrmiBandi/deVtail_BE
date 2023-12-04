from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomUserManager

class User(AbstractUser, PermissionsMixin):
    '''
    사용자 모델
    '''
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    development_field = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='user/imgs/%Y/%m/%d/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return f'/accounts/profile/{self.pk}'
