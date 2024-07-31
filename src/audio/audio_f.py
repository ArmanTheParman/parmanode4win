import threading
import time
import sys
import os
from os import environ
from pydub import AudioSegment
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Must come before pygame import
import pygame

class MusicPlayer:
    def __init__(self, file_path, vol=0.5):
        self.vol = vol
        self.file_path = file_path
        self.wav_path = self.convert_to_wav(file_path)
        self.music_thread = None
        self._stop_event = threading.Event()

    def convert_to_wav(self, file_path):
        if file_path.endswith(".m4a"):
            audio = AudioSegment.from_file(file_path, format="m4a")
            wav_path = file_path.replace(".m4a", ".wav")
            audio.export(wav_path, format="wav")
            return wav_path
        return file_path

    def _play(self):
        with open(os.devnull, "w") as f:
            sys.stdout = f
            pygame.mixer.init()
            sys.stdout = sys.__stdout__  # Restore sys.stdout
            pygame.mixer.music.load(self.wav_path)
            pygame.mixer.music.set_volume(self.vol)
            pygame.mixer.music.play()

        while pygame.mixer.music.get_busy() and not self._stop_event.is_set():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()

    def play_music(self, vol=None):
        if vol is not None:
            self.vol = vol
        self._stop_event.clear()
        self._music_thread = threading.Thread(target=self._play)
        self._music_thread.start()

    def stop_music(self):
        self._stop_event.set()
        if self._music_thread is not None:
            self._music_thread.join()

    def set_volume(self, vol):
        self.vol = vol
        pygame.mixer.music.set_volume(self.vol)