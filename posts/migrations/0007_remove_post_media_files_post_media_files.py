# Generated by Django 5.1.6 on 2025-03-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_library', '0003_alter_mediafile_file'),
        ('posts', '0006_remove_post_media_files_post_media_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='media_files',
        ),
        migrations.AddField(
            model_name='post',
            name='media_files',
            field=models.ManyToManyField(blank=True, related_name='posts', to='media_library.mediafile'),
        ),
    ]
