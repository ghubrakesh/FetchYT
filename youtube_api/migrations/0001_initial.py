# Generated by Django 5.1.2 on 2024-10-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('publish_datetime', models.DateTimeField()),
                ('thumbnail_urls', models.JSONField()),
            ],
            options={
                'ordering': ['-publish_datetime'],
                'indexes': [models.Index(fields=['publish_datetime'], name='youtube_api_publish_870635_idx')],
            },
        ),
    ]