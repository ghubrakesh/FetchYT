from rest_framework.views import APIView
from .models import Video
from .pagination import VideoPagination
from .serializers import VideoSerializer

# Create your views here.

class VideoListView(APIView):
    def get(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        videos = Video.objects.all()
        paginator = VideoPagination()
        paginated_videos = paginator.paginate_queryset(videos, request)
        serializer = VideoSerializer(paginated_videos, many=True)
        return paginator.get_paginated_response(serializer.data)
