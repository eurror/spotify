# Generated by Django 4.1.6 on 2023-02-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0003_alter_song_album_alter_song_artist_alter_song_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='song',
            name='audio_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
