import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from fetchyt.utils import *
from .models import Video
from .pagination import VideoPagination
from .serializers import VideoSerializer

# Create your views here.
log = logging.getLogger(__name__)


class VideoListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # import pdb; pdb.set_trace()
            videos = Video.objects.all()
            paginator = VideoPagination()
            paginated_videos = paginator.paginate_queryset(videos, request)
            serializer = VideoSerializer(paginated_videos, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            log.error(f"{RED}ERROR fetchyt:views :: VideoListView.get() error : {str(e)}{NC}")
            return Response({'error': str(e)}, status=500)
