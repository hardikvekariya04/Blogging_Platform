# Generated by Django 4.2.13 on 2024-07-02 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]