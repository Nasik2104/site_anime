# Generated by Django 5.0.6 on 2024-08-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_abandonedlist_user_alter_favoritelist_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendslist',
            old_name='anime',
            new_name='friends',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_pictures'),
        ),
    ]