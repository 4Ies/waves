from core import lyricGenerator
from core import storageManager
from core import aiManager
from core.exceptions import *
import re

def start_transcription(filename: str, title: str, artist: str, track_num: int, album: str):
    """
    Generates lyrics by analizing song, saves the lyrics obtained in database (if not already present)
    """
    # title case the album name
    album.title()
    
    # sanitize album title to save its name as json
    if not (_is_album_name_valid(album)):
        return False
    else:
        san_album = _convert_to_store(album)
        if storageManager.check_song_already_stored(title, san_album):
            
            #Song already present inside json
            return
        else:
            try:
                print("controller: start of transcription")
                text = lyricGenerator.transcript(filename)

            except TranscriptionError:
                print("Controller encountered an error during transcription phase") 
                return
        
            print("controller: transcription done")
            print(text)
        
            storageManager.store_lyrics(title, artist, track_num, san_album, text, "")
        
        
def create_song_meaning(title:str, album:str):
    """
    Creates the song meaning using the storage manager and the ai manager
    """
    # sanitize album title to save its name as json
    if not (_is_album_name_valid(album)):
        print("Invalid album name")
        return False
    
    else:
        san_album = _convert_to_store(album)
        song_meaning = aiManager.create_song_meaning(title, san_album)
        if (song_meaning == "None"):
            print("Error in AIManager in creating meaning")

        else:
            storageManager.store_song_meaning(title, san_album, song_meaning)
            print("Meaning generated!")

def _convert_to_store(string):
    # Converts a string by switching " " with "_"
    return(string.replace(" ", "_"))

def _convert_to_show(string):
    # Converts a string by switching "_" with " "
    return(string.replace("_", " "))

def _is_album_name_valid(album: str):
    """
    Function that checks if album name is made by alphanumerical characters or underscores
    """

    regex = r'^[a-zA-Z0-9_ ]+$'
    return bool(re.fullmatch(regex, album))

def manually_insert_lyrics():

    return True

def get_song_lyrics(songcode:str):

    return "not implemented yet"

def get_album_lyrics(albumTitle: str, artist: str):

    return "not implemented yet"
