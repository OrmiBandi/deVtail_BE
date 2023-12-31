# Generated by Django 4.2.7 on 2023-12-04 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '카테고리',
                'verbose_name_plural': '카테고리',
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='study/imgs/%Y/%m/%d/')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('cycle', models.IntegerField()),
                ('day', models.IntegerField(choices=[(1, '월요일'), (2, '화요일'), (3, '수요일'), (4, '목요일'), (5, '금요일'), (6, '토요일'), (7, '일요일')])),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('introduce', models.TextField(blank=True, null=True)),
                ('topic', models.CharField(blank=True, max_length=100, null=True)),
                ('difficulty', models.CharField(blank=True, choices=[('상', '상'), ('중', '중'), ('하', '하')], max_length=2, null=True)),
                ('max_member', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='study.category')),
                ('chat_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.chatroom')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '스터디',
                'verbose_name_plural': '스터디',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.study')),
            ],
            options={
                'verbose_name': '태그',
                'verbose_name_plural': '태그',
            },
        ),
        migrations.CreateModel(
            name='StudyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.study')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '스터디 멤버',
                'verbose_name_plural': '스터디 멤버',
            },
        ),
        migrations.CreateModel(
            name='RefLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.study')),
            ],
            options={
                'verbose_name': '참조링크',
                'verbose_name_plural': '참조링크',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('is_secret', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('origin_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='study.comment')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.study')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글',
            },
        ),
    ]
