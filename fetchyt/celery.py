import os
import random
import logging
from celery import Celery
from celery.schedules import crontab
from .utils import API_KEYS
import requests


log = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fetchyt.settings')

app = Celery('fetchyt')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task
def fetch_latest_videos():
    from youtube_api.models import Video
    YOUTUBE_API_KEY = random.choice(API_KEYS)
    SEARCH_QUERY = 'cricket' 
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={SEARCH_QUERY}&maxResults=5&publishedAfter=2024-10-10T00:00:00Z&order=date&type=video&key={YOUTUBE_API_KEY}'

    response = requests.get(url)
    if response.status_code == 200:
        videos = response.json().get('items', [])
        video_objects = []
        existing_video_ids = set()

        existing_videos = Video.objects.filter(video_id__in=[item['id']['videoId'] for item in videos])
        existing_video_ids.update(existing_videos.values_list('video_id', flat=True))
        for item in videos:
            video_id = item['id']['videoId']
            
            video_data = {
                'video_id': video_id,
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'publish_datetime': item['snippet']['publishedAt'],
                'thumbnail_urls': item['snippet']['thumbnails']
            }

            if video_id in existing_video_ids:
                video = existing_videos.get(video_id=video_id)
                for key, value in video_data.items():
                    setattr(video, key, value)  # Update the video object's attributes
            else:
                video_objects.append(Video(**video_data))
        
        if video_objects:
            print("bulk creating")
            Video.objects.bulk_create(video_objects)

        if existing_videos:
            Video.objects.bulk_update(existing_videos, ['title', 'description', 'publish_datetime', 'thumbnail_urls'])

        log.info("fetchyt:celery :: fetch_latest_videos() celery task execution completed Successfully")
        
    else:
        log.error(f"fetchyt:celery :: fetch_latest_videos() celery task execution Failed. Response: {response.json()}")


app.conf.beat_schedule = {
    'fetch-latest-videos-every-10-seconds': {
        'task': 'fetchyt.celery.fetch_latest_videos',
        'schedule': 600.0,
    },
}
