from django.db import models

# Create your models here.

class Schedule(models.Model):
    '''
    일정 모델
    '''
    user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='schedules'
    )
    schedule_title = models.CharField(max_length=100)
    schedule_content =models.CharField(max_length=200, null=True, blank=True)
    schedule_start = models.DateTimeField(null=True)
    schedule_end = models.DateTimeField(null=True)

    class Meta:
        verbose_name = '일정'
        verbose_name_plural = '일정'