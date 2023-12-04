from django.db import models

class DevMate(models.Model):
    '''
    DevMate 모델
    '''
    send_user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='send_users'
    )
    receive_user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='receive_users'
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class UserBlock(models.Model):
    '''
    사용자 차단 모델
    '''
    blocking_user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='blocking_users'
    )
    blocked_user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='blocked_users'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '사용자 차단'
        verbose_name_plural = '사용자 차단'


class UserReport(models.Model):
    '''
    사용자 신고 모델
    '''
    reporting_user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='reporting_users'
    )
    reported_user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='reported_users'
    )
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '사용자 신고'
        verbose_name_plural = '사용자 신고'
