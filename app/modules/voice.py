import os

import speech_recognition as sr


class VoiceModule:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self, audio_path):
        """Convert speech to text using PocketSphinx (lightweight STT)."""
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
                text = self.recognizer.recognize_sphinx(audio)
                return text
        except Exception as e:
            return f"Error in speech recognition: {e}"

    def synthesize_speech(self, text, output_path="output.wav"):
        """Convert text to speech using eSpeak (lightweight TTS)."""
        os.system(f'espeak "{text}" -w {output_path}')
        return output_path
