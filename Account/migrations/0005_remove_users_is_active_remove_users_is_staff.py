# Generated by Django 4.2.2 on 2023-10-22 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_users_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_staff',
        ),
    ]