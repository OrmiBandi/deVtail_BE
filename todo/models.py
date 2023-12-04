from django.db import models

# Create your models here.

class Todo(models.Model):
    '''
    할일 모델
    '''
    study = models.ForeignKey(
        'study.Study', on_delete=models.CASCADE, related_name='todos'
    )
    user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='todos', null=True
    )
    todo_title = models.CharField(max_length=100)
    todo_content =models.CharField(max_length=200, null=True, blank=True)
    todo_start = models.DateTimeField()
    todo_end = models.DateTimeField()
    todo_status = models.CharField(max_length=100, default='Todo')

    class Meta:
        verbose_name = '할일'
        verbose_name_plural = '할일'