import os
import subprocess
import logging
from django.conf import settings
from .models import Video

logger = logging.getLogger(__name__)

def convert_video_to_qualities(video_instance: Video):

    input_path = video_instance.video_file.path
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    
    logger.info(f"Starting video conversion for {input_path}")
    
    qualities = {
        '1080p': {'height': 1080, 'bitrate': '4000k'},
        '720p': {'height': 720, 'bitrate': '2500k'},
        '360p': {'height': 360, 'bitrate': '1000k'},
        '120p': {'height': 120, 'bitrate': '400k'}
    }
    
    for quality, settings in qualities.items():
        output_dir = os.path.join('media', 'videos', quality)
        os.makedirs(output_dir, exist_ok=True)
        
        output_path = os.path.join(output_dir, f"{base_name}_{quality}.mp4")
        
        logger.info(f"Converting to {quality} - Output: {output_path}")
        
        command = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'scale=-2:{settings["height"]}',
            '-b:v', settings['bitrate'],
            '-c:v', 'libx264',
            '-preset', 'medium',
            '-c:a', 'aac',
            '-b:a', '128k',
            '-y',  
            output_path
        ]
        
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            logger.info(f"Successfully converted to {quality}")
            
            relative_path = os.path.join('videos', quality, f"{base_name}_{quality}.mp4")
            setattr(video_instance, f'video_{quality}', relative_path)
            logger.info(f"Updated video instance with {quality} path: {relative_path}")
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Error converting to {quality}: {e.stderr}")
            continue
    
    video_instance.save()
    logger.info("Video conversion completed and saved")

def generate_thumbnail(video_instance: Video):
    """
    Generate a thumbnail from the video using FFmpeg.
    """
    input_path = video_instance.video_file.path
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    
    output_dir = os.path.join('media', 'thumbnails')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, f"{base_name}_thumb.jpg")
    
    logger.info(f"Generating thumbnail for {input_path}")
    
    command = [
        'ffmpeg',
        '-i', input_path,
        '-ss', '00:00:01',  
        '-vframes', '1',
        '-vf', 'scale=320:-1',  
        '-y',  
        output_path
    ]
    
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        relative_path = os.path.join('thumbnails', f"{base_name}_thumb.jpg")
        video_instance.thumbnail = relative_path
        video_instance.save()
        logger.info(f"Thumbnail generated successfully: {relative_path}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error generating thumbnail: {e.stderr}") 