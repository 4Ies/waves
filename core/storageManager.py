import json
from pathlib import Path

from core.exceptions import *

# path constant
DB_PATH = Path("data/albums")

def check_song_already_stored(title: str, san_album: str):
    """
    Checks if a song already exists in storage

    **Returns:** *True* if song is already stored, *False* otherwise
    """

    # Check if json with album exists, if not create it
    album_path = DB_PATH / f"{san_album}.json"
    album_path.parent.mkdir(parents=True, exist_ok=True)

    if album_path.exists():
        with open(album_path, 'r', encoding='utf-8') as jsonFile:
            album_data = json.load(jsonFile)
        for song in album_data["songs"]:
            if song["title"] == title:
                return True
        
    return False

def store_lyrics(title: str, artist: str, track_num: int, san_album: str, text:str, meaning:str):
    """
    Stores lyrics of a song inside the json of its album

    - **Returns**: true if song gets saved properly
    """

    # Create dictionary to be translated in json
    data = {
        "code": _encode_pair(title, artist),
        "title": title,
        "artist": artist,
        "track_num": track_num,
        "album": san_album,
        "lyrics": text,
        "meaning": meaning
    }

    # Check if json with album exists, if not create it
    album_path = DB_PATH / f"{san_album}.json"
    album_path.parent.mkdir(parents=True, exist_ok=True)

    if album_path.exists():
        with open(album_path, 'r', encoding='utf-8') as jsonFile:
            album_data = json.load(jsonFile)
        album_data["songs"].append(data)
    else:
        album_data = {
            "album": san_album,
            "artist": artist,
            "songs": [data]
        }

    with open(album_path, "w", encoding="utf-8") as f:
        json.dump(album_data, f, indent=2, ensure_ascii=False)

def store_song_meaning(title:str, san_album:str, meaning:str):
    """
    Stores a single song meaning

    **Throws:** SongNotFound, AlbumNotFound
    """

    album_path = DB_PATH / f"{san_album}.json"
    if album_path.exists():
        with open(album_path, 'r', encoding='utf-8') as jsonFile:
            album = json.load(jsonFile)
        
        for song in album["songs"]:
            if song["title"] == title:
                song["meaning"] = meaning

                with open(album_path, 'w', encoding='utf-8') as jsonFile:
                    json.dump(album, jsonFile, indent=2, ensure_ascii=False)
                return
            
        # Otherwise, no song exists
        raise SongNotFound

    else:

        # Otherwise, no album exists
        raise AlbumNotFound

def _encode_pair(title: str, artist: str):
    """
    Extremely simple encoding of title+artist, can be modified for better security
    """

    title = title.replace(" ", "")
    artist = artist.replace(" ","")
    return (title+artist)