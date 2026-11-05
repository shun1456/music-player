import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import tkinter as tk
import time
from just_playback import Playback

player = Playback()
music_list_initial = []
music_list = []
title = ''
author = ''
slash = r"\ "
slash = slash.removesuffix(' ')
song = {}
current_song = ''

for filename in os.listdir(r'C:\Users\shun\Music\song storage'):
    music_list_initial.append(filename.removesuffix('.mp3'))

for i in range(len(music_list_initial)):
    file_path = r'C:\Users\shun\Music\song storage' + slash + music_list_initial[i] + '.mp3'
    audio = MP3(file_path, ID3=EasyID3)
    author = audio.get('artist', ['неизвестно'])[0]
    title = audio.get('title', ["неизвестно"])[0]
    duration_in_seconds = audio.info.length
    duration_in_seconds = int(duration_in_seconds)
    if duration_in_seconds % 60 < 10:
        duration = str(duration_in_seconds // 60) + ':' + '0' + str(duration_in_seconds % 60)
    else:
        duration = str(duration_in_seconds // 60) + ':' + str(duration_in_seconds % 60)
    song = {'title': title.removesuffix(' (Sefon.Pro)'), 'author': author, 'duration': duration, 'filepath': file_path}
    music_list.append(song)
current_music_list = music_list

#print(music_list)


def sort_by_one(object, music_list):
    return_list = []
    authors = []
    for i in music_list:
        if i['title'] == object:
            return_list.append(i)
            break
        elif object in i['author']:
            return_list.append(i)
    global current_music_list
    current_music_list = return_list
    return return_list


def sort_list_by_alph(object, music_list):
    list_a = []
    sorted_list = []
    if object == 'author':
        for i in music_list:
            list_a.append(i['author'])
    elif object == 'title':
        for i in music_list:
            list_a.append(i['title'])
    list_a.sort(key=str.lower)
    for i in music_list:
        if i['author'] in list_a:
            sorted_list.append(i)
        elif i['title'] in list_a:
            sorted_list.append(i)
    global current_music_list
    current_music_list = sorted_list
    return sorted_list


def play(current_music_list):
    global current_song
    for i in current_music_list:
        player.load_file(i['filepath'])
        player.play()
        current_song = i['filepath']
        while player.playing():
            time.sleep(1)
    current_song = ''


def toggle(current_song):
    if current_song == '':
        return
    if player.active:
        if player.playing:
            player.pause()
        else:
            player.resume()


def rewind(exact_time):
    player.seek(exact_time)
