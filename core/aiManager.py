import json
from pathlib import Path
import ollama

# path constant
DB_PATH = Path("data/albums")
MODEL_NAME = "tinyllama"

def create_song_meaning(title: str, san_album: str):
    """
    Creates the song meaning by using the information of its lyrics and the name of the album itself
    """
    # Load json
    album_path = DB_PATH / f"{san_album}.json"
    if not album_path.exists():
        print(f"Album file {album_path} not found.")
        return "None"
    with open(album_path, "r", encoding="utf-8") as f:
        album = json.load(f)
    
    # Search specific song lyrics
    for song in album["songs"]:
        if song["title"] == title:
            lyrics = song["lyrics"]
            prompt = f"""You are a music analyst. Given all the lyrics from the song "{title}" from the album {album['album']}, 
                please write a concise but dense analysis of the song's overall meaning, themes, and emotional arc, noticing figures of 
                speech, interesting references and finding correlations between song name, album name and lyrics if there's any. 
                Skip the preamble (like "here's the result of ...") and go straight to the point.

                Lyrics:
                {lyrics}
                Analysis:"""
            response = ollama.generate(
                model=MODEL_NAME,
                prompt=prompt,
                options={"temperature": 0.6, "num_predict": 400}
            )

            if response and "response" in response:
                meaning: str = str(response["response"].strip())
                print(meaning)
            else:
                meaning: str = "None"
            return(meaning)
        
    print("Song not found")
    return "None"