import subprocess

def add_subtitles_to_video(video_file, subtitle_file, output_file):
    """
    Add subtitles to a given video file.

    Args:
        video_file (str): Path to the input video file.
        subtitle_file (str): Path to the subtitle file (in SRT format).
        output_file (str): Path to the output video file with subtitles.
    """
    # Command to add subtitles using ffmpeg
    command = [
        "ffmpeg",
        "-i", video_file,
        "-vf", f"subtitles={subtitle_file}",
        "-c:a", "copy",
        output_file
    ]

    # Execute the ffmpeg command
    subprocess.run(command)

