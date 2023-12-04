from django.db import models

# Create your models here.

class Alert(models.Model):
    '''
    알림 모델
    '''

    ALERT_CATEGORIES = [
        ('alert_devmate', '데브메이트'),
        ('alert_chat', '채팅'),
        ('alert_todo', '할일'),
        ('alert_schedule', '일정'),
        ('alert_other', '기타')
    ]

    user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE
    )
    alert_content = models.CharField(max_length=100)
    alert_category = models.CharField(max_length=20, choices=ALERT_CATEGORIES)
    alert_at = models.DateTimeField(auto_now_add=True)
    alert_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = '알림'
        verbose_name_plural = '알림'
