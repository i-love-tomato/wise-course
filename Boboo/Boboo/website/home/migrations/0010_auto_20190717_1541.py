# Generated by Django 2.2.3 on 2019-07-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190717_0857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ['create_time']},
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='publishtime',
            new_name='create_time',
        ),
        migrations.AddField(
            model_name='meeting',
            name='publish_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]