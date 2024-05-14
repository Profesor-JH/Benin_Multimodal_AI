from pydub import AudioSegment
def extract_audio(video_path):
    """
    Extract audio from a video file.

    Args:
        video_path (str): Path to the video file.

    Returns:
        bytes: Extracted audio in WAV format.
    """
    # Load the video file
    video = AudioSegment.from_file(video_path)

    # Extract audio
    audio_file = video.export(format="wav")

    return audio_file