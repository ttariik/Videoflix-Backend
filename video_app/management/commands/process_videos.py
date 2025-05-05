from django.core.management.base import BaseCommand
from video_app.models import Video
from video_app.services import convert_video_to_qualities, generate_thumbnail

class Command(BaseCommand):
    help = 'Process all videos to generate different quality versions'

    def handle(self, *args, **options):
        videos = Video.objects.all()
        self.stdout.write(f"Found {videos.count()} videos to process")
        
        for video in videos:
            self.stdout.write(f"Processing video {video.id}: {video.title}")
            try:
                convert_video_to_qualities(video)
                generate_thumbnail(video)
                self.stdout.write(self.style.SUCCESS(f"Successfully processed video {video.id}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error processing video {video.id}: {str(e)}")) 