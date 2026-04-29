from core import lyricGenerator
from core import storageManager
import re

def start_transcription(filename: str, title: str, artist: str, track_num: int, album: str):
    # sanitize album title to save its name as json
    if not (_is_album_name_valid(album)):
        return False
    else:
        text = lyricGenerator.transcript(filename)
        print(text)
        san_album = _convert_to_store(album)
        if(storageManager.store_lyrics(title, artist, track_num, san_album, text, "")):
            print("Song stored successfully!")
        else:
            print("Error in saving song")

def _convert_to_store(string):
    # Converts a string by switching " " with "_"
    return(string.replace(" ", "_"))

def _convert_to_show(string):
    # Converts a string by switching "_" with " "
    return(string.replace("_", " "))

def _is_album_name_valid(album: str):
    # Accepts only alphanumerical and underscores
    regex = r'^[a-zA-Z0-9_ ]+$'

    return bool(re.fullmatch(regex, album))

def get_song_lyrics(songcode:str):

    return "not implemented yet"

def get_album_lyrics(albumTitle: str, artist: str):

    return "not implemented yet"
