import pygame, threading, time
from variables import *

class MusicPlayer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.music_thread = None
        self._stop_event = threading.Event()

    def _play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() and not self._stop_event.is_set():
            pygame.time.Clock().tick(10)
        pygame.mixer.quit() 
    
    def play_music(self):
        self._stop_event.clear()
        self._music_thread = threading.Thread(target=self._play)
        self._music_thread.start()
    
    def stop_music(self):
        self._stop_event.set()
        if self._music_thread is not None:
            self._music_thread.join()


        