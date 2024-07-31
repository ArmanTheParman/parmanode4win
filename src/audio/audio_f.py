import threading, time, sys, os
from variables import *
from os import environ
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' #must come before pygame import
import pygame

class MusicPlayer:
    def __init__(self, file_path, vol=0.5):
        self.vol = vol
        self.file_path = file_path
        self.music_thread = None
        self._stop_event = threading.Event()

    def _play(self):
        with open(os.devnull, "w") as f:
            sys.stdout = f
            pygame.mixer.init()
            sys.stdout = sys.__stdout__ #restore sys.stdout
            pygame.mixer.music.load(self.file_path)
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





        