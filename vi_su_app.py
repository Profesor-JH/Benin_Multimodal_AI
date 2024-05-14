import streamlit as st
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

def main():
    st.title("Video Player with Subtitles")

    # Process the video and subtitles
    # Replace the placeholders with your actual video, subtitle, and output file paths
    video_file = "video2.mp4"
    subtitle_file = "output.srt"
    output_file = "output_video_with_subtitles.mp4"

    add_subtitles_to_video(video_file, subtitle_file, output_file)

    # Display the processed video with subtitles
    st.video(output_file)

if __name__ == "__main__":
    main()
