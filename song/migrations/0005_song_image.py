# Generated by Django 4.1.6 on 2023-02-06 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_song_audio_file_song_audio_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
