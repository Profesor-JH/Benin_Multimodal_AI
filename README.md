# Kwabo: Breaking Language Barriers for Tourism
Mi Kwabo is an application designed to break language barriers for tourism by providing functionalities such as speech recognition, text translation, and subtitle generation for videos.

# Key Technologies Used
This project utilizes a variety of technologies and libraries to achieve its functionality. Below is a summary of the key technologies used:

**1. Python:** The core programming language used for scripting and automation.

**2. Streamlit:** A powerful framework for creating interactive web applications using Python, used for building the user interface of the application.

**3. PyDub:** A library for audio manipulation, used to extract and process audio from video files.

**4. MoviePy:** A library for video editing, used to extract video duration.

**5. Hugging Face Transformers:** A library from Hugging Face for natural language processing, used for speech recognition and translation.

*   Automatic Speech Recognition (ASR): Implemented using a pre-trained model from the transformers library.

*   Translation: Utilizes a custom model from Hugging Face for translating text between different languages.

**6. FFmpeg:** A powerful multimedia framework used for adding subtitles to video files.

**7. Tempfile:** A Python library used to create temporary files and directories.

**8. YAML:** Used for configuration management (e.g., database configuration in config.yaml).

**9. Subprocess:** Used to run external commands and scripts from within Python.

**10. OS:** A module that provides a way to use operating system dependent functionality, such as reading or writing to the file system.

# Project Structure

```
Mi_Kwabo/
├── Audio_Extractor.py               # Script for extracting audio from video files
├── README.md                        # Project README file
├── Speech_Pocessor.py               # Script for speech recognition and translation
├── __pycache__/                     # Directory for cached bytecode files
├── app.py                           # Streamlit application entry point
├── backup_untracked_files/          # Backup directory for untracked files
├── benin.png                        # Background image for the app
├── merge.py                         # Script for merging subtitles with video files
├── mmtafrica/                       # Directory for MMT Africa model
├── mmtafrica~f4a573c7477c47b57a8d60783869a18f225fbdbc  # Backup file
├── requirements.txt                 # Project dependencies
├── setup.sh                         # Setup script for initializing the environment
├── styles.css                       # CSS file for styling the app
├── subtitle.py                      # Script for generating and exporting subtitles
├── vi_su_app.py                     # Additional script for video and subtitle processing
├── video_duration_extractor.py      # Script for extracting video duration

```

# Overview
The Mi Kwabo application facilitates the extraction of audio from video files, performs speech recognition on the extracted audio, translates the recognized text into a target language, generates subtitles based on the translation, and merges these subtitles back into the original video.

# Features

**1. Audio Extraction:** Extract audio from uploaded video files.

**2. Speech Recognition:** Convert audio to text using a pre-trained speech recognition model.

**3. Text Translation:** Translate the recognized text into a target language.

**4. Subtitle Generation:** Create subtitles from the translated text.

**5. Video Merging:** Merge the generated subtitles back into the original video.

**6. User Interface:** Interactive web interface using Streamlit.

# Installation
1. Clone the repository:
```
git clone https://github.com/Profesor-JH/Benin_Multimodal_AI.git
cd Mi_Kwabo
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the setup script:

```
chmod +x setup.sh
./setup.sh
```

4. Start the application:
```
streamlit run app.py
```

# Usage
1. Open the application in your web browser:

2. Upload a video file in MP4 format.

    * Select the source language and the target language for translation.

    * Run the following processes by clicking their respective buttons:

    * Run Speech Recognition: Extract audio and perform speech recognition.

    * Run Text Translation: Translate the recognized text into the selected target language.

    * Generate Subtitles: Generate subtitles based on the translated text.

    * Merge Subtitles with Video: Merge the generated subtitles with the original video file.

# File Descriptions
**app.py:** The main Streamlit application file. It contains the UI and integrates all functionalities.

**Audio_Extractor.py:** Extracts audio from video files using the pydub library.

**Speech_Pocessor.py:** Contains functions for speech recognition and translation using pre-trained models.

**merge.py:** Merges subtitles with video files using ffmpeg.

**subtitle.py:** Generates and exports subtitles in SRT format.

**video_duration_extractor.py:** Extracts the duration of a video file using moviepy.

# Dependencies
The dependencies for this project are listed in the requirements.txt file. These include:

```
Streamlit
pydub
transformers
torch
moviepy
ffmpeg
Contributing
Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.
```

License
This project is licensed under the MIT License.

