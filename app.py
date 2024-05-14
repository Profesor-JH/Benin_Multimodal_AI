import streamlit as st
import tempfile
import os
from pydub import AudioSegment
import Speech_Pocessor as SA
import Audio_Extractor as AE
import video_duration_extractor as de
import subtitle as su
import merge as me



# Language map for translation
language_map = {'English': 'en', 'Swahili': 'sw', 'Fon': 'fon', 'Igbo': 'ig',
                'Kinyarwanda': 'rw', 'Xhosa': 'xh', 'Yoruba': 'yo', 'French': 'fr'}


#Link to CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    local_css("styles.css")
    # Display the image as the background cover
    st.markdown(
        """
        <style>
            .reportview-container {
                background: url('benin.png') no-repeat center center fixed;
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Mi Kwabo: Breaking Language Barriers for Tourism")

    source_language = st.selectbox("Select source language:", list(language_map.keys()))
    target_language = st.selectbox("Select target language:", list(language_map.keys()))

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])

    if uploaded_file is not None:
        # Initialize session state
        if 'temp_dir' not in st.session_state:
            st.session_state.temp_dir = tempfile.mkdtemp()

        # Save the uploaded video to a temporary directory
        video_path = os.path.join(st.session_state.temp_dir, "uploaded_video.mp4")
        with open(video_path, "wb") as f:
            f.write(uploaded_file.read())

        # Extract audio from the video
        audio = AE.extract_audio(video_path)

        if audio is not None:
            # Resample audio to 16kHz
            audio = AudioSegment.from_file(audio, format="wav")
            audio = audio.set_frame_rate(16000)
            audio_path = os.path.join(st.session_state.temp_dir, "extracted_audio.wav")
            audio.export(audio_path, format="wav")

        if st.button("Run Speech Recognition"):
            with open(audio_path, "rb") as f:
                audio = f.read()
            # Perform speech recognition
            transcription = SA.perform_speech_recognition(audio)

            if transcription:
                st.session_state.transcription = transcription
                st.write("Transcription:", transcription)

        if st.button("Run Text Translation"):
            if 'transcription' not in st.session_state:
                st.error("Please run speech recognition first.")
            else:
                # Perform translation
                translation = SA.perform_translation(source_language, target_language, st.session_state.transcription)

                if translation:
                    st.session_state.translation = translation
                    st.write(f"Translation ({target_language}):", translation)

        if st.button("Generate Subtitles"):
            if 'translation' not in st.session_state:
                st.error("Please run text translation first.")
            else:
                # Generate subtitles
                st.write("Generating subtitles...")
                total_duration = de.get_video_duration(video_path)
                chunk_count = 10  # Number of subtitle chunks to generate
                subtitles = su.generate_subtitles(st.session_state.translation, total_duration, chunk_count)
                subtitles_path = os.path.join(st.session_state.temp_dir, "output.srt")
                su.export_subtitle_srt(subtitles, subtitles_path)
                st.session_state.subtitles_path = subtitles_path
                st.write("Subtitles generated successfully")

        if st.button("Merge Subtitles with Video"):
            if 'subtitles_path' not in st.session_state:
                st.error("Please generate subtitles first.")
            else:
                # Merge subtitles with video
                st.write("Merging subtitles with video...")
                output_file = os.path.join(st.session_state.temp_dir, "output_video_with_subtitles.mp4")
                me.add_subtitles_to_video(video_path, st.session_state.subtitles_path, output_file)
                st.write(f"Transcription ({source_language}):",st.session_state.transcription)
                st.write(f"Translation ({target_language}):",st.session_state.translation)
                st.write("Video with Subtitles")
                st.video(output_file)

                # Clean up temporary files
                os.remove(audio_path)
                os.remove(video_path)
                os.remove(output_file)
                os.remove(st.session_state.subtitles_path)
                del st.session_state.subtitles_path
                del st.session_state.transcription
                del st.session_state.translation


if __name__ == "__main__":
    main()
