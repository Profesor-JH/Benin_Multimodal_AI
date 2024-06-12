def generate_subtitles(text, total_duration, chunk_count):
    """
    Generate subtitles dynamically based on the given text and total duration.

    Args:
        text (str): The text to be divided into subtitles.
        total_duration (float): Total duration of the video in seconds.
        chunk_count (int): Number of subtitle chunks to generate.

    Returns:
        list: List of subtitle tuples in the format (start_time, end_time, text).
    """
    chunk_duration = total_duration / chunk_count
    subtitles = []

    for i in range(chunk_count):
        start_time = i * chunk_duration
        end_time = min((i + 1) * chunk_duration, total_duration)
        chunk_text = text[i * len(text) // chunk_count : (i + 1) * len(text) // chunk_count]
        subtitles.append((start_time, end_time, chunk_text))

    return subtitles

def export_subtitle_srt(subtitles, output_file):
    """
    Export subtitles to SubRip (SRT) format.

    Args:
        subtitles (list): List of subtitle tuples in the format (start_time, end_time, text).
        output_file (str): Path to the output SRT file.
    """
    with open(output_file, 'w') as f:
        for i, (start_time, end_time, text) in enumerate(subtitles, start=1):
            f.write(f"{i}\n")
            f.write(f"{format_time(start_time)} --> {format_time(end_time)}\n")
            f.write(f"{text}\n\n")

def format_time(seconds):
    """
    Format time in seconds to SRT format (HH:MM:SS,sss).

    Args:
        seconds (float): Time in seconds.

    Returns:
        str: Formatted time string.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


