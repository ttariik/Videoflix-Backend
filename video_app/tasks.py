from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os
import subprocess
import django_rq
from moviepy import VideoFileClip
from django.core.files import File
import io
from PIL import Image
from .models import Video
import time


def process_video(video_id):
    try:
        video = Video.objects.get(id=video_id)
        
        generate_thumbnail(video)
        
        convert_video_to_resolutions(video_id)
        
        print(f"Video {video_id} erfolgreich verarbeitet")
        return True
    except Exception as e:
        print(f"Fehler bei der Videoverarbeitung: {str(e)}")
        return False


def generate_thumbnail(video):
    video_clip = VideoFileClip(video.video_file.path)
    if video_clip.duration < 2:
        return
    frame = video_clip.get_frame(5)
    pil_image = Image.fromarray(frame).convert("RGB")
    pil_image.thumbnail((200, 150), Image.Resampling.LANCZOS)
    thumb_io = io.BytesIO()
    pil_image.save(thumb_io, 'PNG')
    thumb_dir = os.path.join(settings.MEDIA_ROOT, 'thumbnails')
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)
    thumb_file_name = os.path.join(thumb_dir, f"{video.title}_thumb.png")
    with open(thumb_file_name, 'wb') as f:
        f.write(thumb_io.getvalue())
    video.thumbnail = os.path.join(
        'thumbnails', f"{video.title}_thumb.png")
    video.save()
    video_clip.close()


def convert_video_to_resolutions(video_id):
    video = Video.objects.get(id=video_id)
    input_path = video.video_file.path
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    
    resolutions = {
        '120p': 120,
        '360p': 360,
        '720p': 720,
        '1080p': 1080
    }
    
    for resolution, height in resolutions.items():
        output_path = os.path.join(settings.MEDIA_ROOT, f'videos/{resolution}', f'{base_name}_{resolution}.mp4')
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        command = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'scale=-2:{height}',
            '-c:v', 'libx264',
            '-crf', '23',
            '-preset', 'medium',
            '-c:a', 'aac',
            '-b:a', '128k',
            output_path
        ]
        
        try:
            subprocess.run(command, check=True, capture_output=True)
            
            relative_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
            setattr(video, f'video_{resolution}', relative_path)
            video.save()
            
            print(f"Video erfolgreich in {resolution} konvertiert")
            
        except subprocess.CalledProcessError as e:
            print(f"Fehler bei der Konvertierung zu {resolution}: {e.stderr.decode()}")
            continue
