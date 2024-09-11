# Generated by Django 5.0.6 on 2024-08-08 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime'),
        ),
        migrations.AlterField(
            model_name='room',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.episode'),
        ),
    ]