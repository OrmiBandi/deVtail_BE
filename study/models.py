from django.db import models

class Study(models.Model):
    difficulty_choices = [
        ('상', '상'),
        ('중', '중'),
        ('하', '하'),
    ]
    day_choices = [
        (1, '월요일'),
        (2, '화요일'),
        (3, '수요일'),
        (4, '목요일'),
        (5, '금요일'),
        (6, '토요일'),
        (7, '일요일'),
    ]
    chat_room = models.ForeignKey('chat.ChatRoom', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    leader = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    goal = models.CharField(max_length=100)
    thumbnail = models.ImageField(null=True, blank=True)
    startdate = models.DateField()
    enddate = models.DateField()
    cycle = models.IntegerField()
    day = models.IntegerField(choices=day_choices)
    starttime = models.TimeField()
    endtime = models.TimeField()
    introduce = models.TextField(null=True, blank=True)
    topic = models.CharField(max_length=100, null=True, blank=True)
    difficulty = models.CharField(max_length=2, choices=difficulty_choices, null=True, blank=True)
    max_member = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'스터디장 : {self.user.username}, 스터디 목표 : {self.study_goal}'


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name
    

class Tag(models.Model):
    study = models.ForeignKey('Study', on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class RefLink(models.Model):
    study = models.ForeignKey('Study', on_delete=models.CASCADE)
    link_category = models.CharField(max_length=100)
    link_name = models.CharField(max_length=100)

    def __str__(self):
        return self.link_name

class Comment(models.Model):
    study = models.ForeignKey('Study', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=500)
    origin_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    is_secret = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'스터디 : {self.study}, 작성자 : {self.user.username}'

class StudyMember(models.Model):
    study = models.ForeignKey('Study', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'스터디 : {self.study}, 회원 : {self.user.username}'