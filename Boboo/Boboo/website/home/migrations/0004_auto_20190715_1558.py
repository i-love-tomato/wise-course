# Generated by Django 2.2.3 on 2019-07-15 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_meeting_meetingtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='publisher',
        ),
        migrations.AddField(
            model_name='meeting',
            name='theme',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
