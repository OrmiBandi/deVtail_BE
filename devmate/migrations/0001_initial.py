# Generated by Django 4.2.7 on 2023-12-04 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reported_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_users', to=settings.AUTH_USER_MODEL)),
                ('reporting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '사용자 신고',
                'verbose_name_plural': '사용자 신고',
            },
        ),
        migrations.CreateModel(
            name='UserBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('blocked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked_users', to=settings.AUTH_USER_MODEL)),
                ('blocking_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocking_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '사용자 차단',
                'verbose_name_plural': '사용자 차단',
            },
        ),
        migrations.CreateModel(
            name='DevMate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('received_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_users', to=settings.AUTH_USER_MODEL)),
                ('sent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
