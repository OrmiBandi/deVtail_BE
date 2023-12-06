from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('study/', include('study.urls')),
    path('devmate/', include('devmate.urls')),
    path('todo/', include('todo.urls')),
    path('chat/', include('chat.urls')),
    path('schedule/', include('schedule.urls')),
    path('alert/', include('alert.urls')),
]
