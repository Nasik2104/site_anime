# Generated by Django 5.0.6 on 2024-09-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_abandonedlist_user_alter_favoritelist_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
