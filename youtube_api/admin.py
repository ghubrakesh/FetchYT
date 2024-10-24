from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id', 'publish_datetime']
    list_filter = ['publish_datetime']

admin.site.register(Video, VideoAdmin)