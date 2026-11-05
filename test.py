from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import tkinter as tk
import time
from just_playback import Playback

file_path = r'C:\Users\shun\Music\song storage\ASCALOR & SXNDSTXRM - ALTER TEKK.mp3'
# audio = MP3(file_path, ID3=EasyID3)
# name=audio.get('artist',['неизвестно'])[0]
# title=audio.get('title')[0]
# album= audio.get("album", ["Неизвестно"])[0]
# date=audio.get("date", ["Неизвестно"])[0]
# genre=audio.get("genre", ["Неизвестно"])[0]
# print (name,title,'album,date,genre')
# print(dict(audio))
player = Playback()
player.load_file(file_path)
player.play()
time.sleep(60)
