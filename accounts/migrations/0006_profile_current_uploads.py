# Generated by Django 5.1.6 on 2025-03-02 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_cover_photo'),
        ('media_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_uploads',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media_library.mediafile'),
        ),
    ]
