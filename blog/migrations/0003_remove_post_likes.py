# Generated by Django 4.2.13 on 2024-07-03 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_delete_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
