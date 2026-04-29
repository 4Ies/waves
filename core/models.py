# core/models.py
from dataclasses import dataclass, asdict
from typing import List, Optional
from datetime import datetime
import json

@dataclass
class Song:
    """Type-safe song object for your lyrics database"""
    id: str
    title: str
    lyrics: str
    artist: str = "To be generated"
    explaination: str = "To be generated"

# Usage
# Create songs (all same type)
song1 = Song(
    id="goodbye_cruel_world",
    title="13. goodbye cruel world.mp3",
    lyrics="Full lyrics text here...",
)

song2 = Song(
    id="another_song",
    title="Another Song.mp3",
    lyrics="More lyrics...",
    artist="Some Artist",
)