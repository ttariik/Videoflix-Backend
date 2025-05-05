from rest_framework import serializers
from .models import Video, UserVideoProgress

class VideoSerializer(serializers.ModelSerializer):
    video_120p = serializers.SerializerMethodField()
    video_360p = serializers.SerializerMethodField()
    video_720p = serializers.SerializerMethodField()
    video_1080p = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            'id', 'title', 'description', 'video_file',
            'thumbnail', 'category', 'created_at',
            'video_120p', 'video_360p', 'video_720p', 'video_1080p'
        ]
        read_only_fields = [
            'thumbnail', 'video_120p', 'video_360p',
            'video_720p', 'video_1080p'
        ]

    def get_video_120p(self, obj):
        if obj.video_120p:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video_120p.url)
            return obj.video_120p.url
        return None

    def get_video_360p(self, obj):
        if obj.video_360p:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video_360p.url)
            return obj.video_360p.url
        return None

    def get_video_720p(self, obj):
        if obj.video_720p:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video_720p.url)
            return obj.video_720p.url
        return None

    def get_video_1080p(self, obj):
        if obj.video_1080p:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video_1080p.url)
            return obj.video_1080p.url
        return None

class UserVideoProgressSerializer(serializers.ModelSerializer):
    video = VideoSerializer(read_only=True)
    video_id = serializers.PrimaryKeyRelatedField(
        queryset=Video.objects.all(),
        source='video',
        write_only=True
    )

    class Meta:
        model = UserVideoProgress
        fields = [
            'id', 'video', 'video_id', 'last_viewed_position',
            'viewed', 'last_viewed_at'
        ]
        read_only_fields = ['last_viewed_at'] 