# Generated by Django 2.2.3 on 2019-07-12 02:58

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('hobby', models.CharField(max_length=50)),
                ('birth', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('workplace', models.CharField(max_length=50)),
                ('lastLogin', models.DateTimeField(auto_now=True)),
                ('c_time', models.DateField(auto_now_add=True)),
                ('introduction', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['c_time'],
            },
        ),
    ]
