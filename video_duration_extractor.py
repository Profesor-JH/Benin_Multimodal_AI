from moviepy.editor import VideoFileClip

def get_video_duration(video_path):
    """
    Get the duration of a video file.

    Args:
        video_path (str): Path to the video file.

    Returns:
        float: Duration of the video in seconds.
    """
    clip = VideoFileClip(video_path)
    duration = clip.duration
    clip.close()
    return duration
