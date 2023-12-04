from django.contrib import admin
from .models import DevMate, UserBlock, UserReport

admin.site.register(DevMate)
admin.site.register(UserBlock)
admin.site.register(UserReport)
