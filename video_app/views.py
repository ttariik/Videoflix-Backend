from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_rq import job
from .models import Video, UserVideoProgress
from .serializers import VideoSerializer, UserVideoProgressSerializer
from .services import convert_video_to_qualities, generate_thumbnail

@job
def process_video(video_id):
    try:
        video = Video.objects.get(id=video_id)
        print(f"Starting video processing for video {video_id}")
        convert_video_to_qualities(video)
        generate_thumbnail(video)
        print(f"Completed video processing for video {video_id}")
    except Video.DoesNotExist:
        print(f"Video with id {video_id} does not exist")
    except Exception as e:
        print(f"Error processing video {video_id}: {str(e)}")

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        video = serializer.save()
        process_video.delay(video.id)
        return video

    @action(detail=True, methods=['post'])
    def reprocess(self, request, pk=None):
        video = self.get_object()
        process_video.delay(video.id)
        return Response({'status': 'video processing started'})

class UserVideoProgressViewSet(viewsets.ModelViewSet):
    serializer_class = UserVideoProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserVideoProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
