import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import tkinter as tk
import time
from just_playback import Playback

player = Playback()


def make_song_folder():
    song_filepath = os.path.join(os.path.expanduser("~"), "song_filepath")
    with open(song_filepath, "w", encoding="utf-8") as file:
        if file == '':
            filepath = 'ghj'  # функция записи пути к папке
            os.makedirs(filepath, exist_ok=True)
            with open(song_filepath, "w", encoding="utf-8") as file:
                file.write(filepath)


def get_all_songs_metadata():
    music_list = []
    music_list_initial = []
    song_filepath = os.path.join(os.path.expanduser("~"), "song_filepath")
    for filename in os.listdir(song_filepath):
        music_list_initial.append(filename)
    for i in range(len(music_list_initial)):
        filepath = song_filepath
        audio = MP3(filepath, ID3=EasyID3)
        author = audio.get('artist', ['неизвестно'])[0]
        title = audio.get('title', ["неизвестно"])[0]
        duration_in_seconds = audio.info.length
        duration_in_seconds = int(duration_in_seconds)
        song = {'title': title.removesuffix(' (Sefon.Pro)'), 'author': author, 'duration': duration_in_seconds,
                'filepath': filepath}
        music_list.append(song)
        return music_list


def search(object, music_list):
    sorted_list = []
    for i in music_list:
        if object in i['title']:
            sorted_list.append(i)
            break
        elif object in i['author']:
            sorted_list.append(i)
    return sorted_list


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
    return sorted_list


def play(song):
    for i in music_list:
        player.load_file(i['filepath'])
        player.play()
        current_song = i['filepath']
        if player.playing():
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
