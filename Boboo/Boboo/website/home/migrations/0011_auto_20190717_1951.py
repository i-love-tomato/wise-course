# Generated by Django 2.2.3 on 2019-07-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190717_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='enddatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='startdatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
