import streamlit as st
from transformers import pipeline
import torch
from mmtafrica.mmtafrica import load_params, translate
from huggingface_hub import hf_hub_download

# Create a speech recognition pipeline using a pre-trained model
pipe = pipeline("automatic-speech-recognition", model="chrisjay/fonxlsr")

# Load translation parameters and model
checkpoint = hf_hub_download(repo_id="chrisjay/mmtafrica", filename="mmt_translation.pt")
device = 'gpu' if torch.cuda.is_available() else 'cpu'
params = load_params({'checkpoint':checkpoint,'device':device})

# Language map for translation
language_map = {'English':'en','Swahili':'sw','Fon':'fon','Igbo':'ig',
                'Kinyarwanda':'rw','Xhosa':'xh','Yoruba':'yo','French':'fr'}



def perform_speech_recognition(audio_file):
    '''
    This function performs speech recognition on the input audio file.
    '''
    try:
        transcription = pipe(audio_file)
        return transcription['text']
    except Exception as e:
        st.error(f"Speech recognition failed: {e}")
        return None

def perform_translation(source_language, target_language, transcription):
    '''
    This function translates the transcription from the source language to the target language.
    '''
    source_language_ = language_map[source_language]
    target_language_ = language_map[target_language]

    try:
        pred = get_translation(source_language_, target_language_, transcription)
        return pred
    except Exception as error:
        st.error(f"Issue with translation: {error}")
        return None

def get_translation(source_language,target_language,source_sentence=None):
    '''
    This takes a sentence and gets the translation.
    '''

    source_language_ = source_language
    target_language_ = target_language

    try:
        pred = translate(params,source_sentence,source_lang=source_language_,target_lang=target_language_)
        if pred == '':
            return f"Could not find translation"
        else:
            return pred
    except Exception as error:
        st.error(f"Issue with translation: {error}")
        return None

