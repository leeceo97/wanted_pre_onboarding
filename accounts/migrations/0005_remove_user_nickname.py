# Generated by Django 4.0.3 on 2022-04-14 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_testuser_user_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]
