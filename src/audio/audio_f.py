import pygame
from variables import *

def play_music():
    bpgtm = p4w / "src" / "audio" / "bpgtm.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(bpgtm)