from django.db import models

class ChatRoom(models.Model):
    '''
    채팅방 모델
    '''
    users = models.ManyToManyField('accounts.User', related_name='chatrooms')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '채팅방'
        verbose_name_plural = '채팅방'


class ChatMessage(models.Model):
    '''
    채팅 메시지 모델
    '''
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey('accounts.User')
    chat_room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '채팅 메시지'
        verbose_name_plural = '채팅 메시지'