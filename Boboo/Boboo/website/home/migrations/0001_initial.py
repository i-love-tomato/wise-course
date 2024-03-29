# Generated by Django 2.2.3 on 2019-07-12 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingname', models.CharField(max_length=100)),
                ('meetingtime', models.DateTimeField()),
                ('place', models.CharField(max_length=50)),
                ('introduction', models.CharField(max_length=400)),
                ('publishtime', models.DateTimeField(auto_now_add=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_column', to='login.UserProfile')),
                ('user_participation', models.ManyToManyField(blank=True, related_name='meeting_participation', to='login.UserProfile')),
            ],
            options={
                'ordering': ['publishtime'],
            },
        ),
    ]
