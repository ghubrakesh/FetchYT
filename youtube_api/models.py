from django.db import models

# Create your models here.

class Video(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_datetime = models.DateTimeField()
    thumbnail_urls = models.JSONField()

    class Meta:
        indexes = [
            models.Index(fields=['publish_datetime']),
        ]
        ordering = ['-publish_datetime']

    def __str__(self):
        return self.title
