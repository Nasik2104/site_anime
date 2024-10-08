# Generated by Django 5.0.6 on 2024-08-02 14:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('studios', models.CharField(max_length=128)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('episodes_count', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='anime_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VoiceActingTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('number', models.IntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('video', models.FileField(upload_to='episodes/')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='anime.anime')),
                ('voice_acting_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='anime.voiceactingteam')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(to='anime.genre'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_room', to=settings.AUTH_USER_MODEL)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='anime.anime')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='anime.episode')),
                ('watchers', models.ManyToManyField(related_name='room', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='voices',
            field=models.ManyToManyField(to='anime.voiceactingteam'),
        ),
    ]
