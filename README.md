# waves
Lyric generator and song analyzer made using whisper, spleeter, librosa, chord_detection and Llama 3.2 1B Instruct.

## What it does
Generates lyrics of a track by firstly isolating the vocal parts of a song using `audio_separator` and then using `whisper` for transcription, then analyzes the text to draw conclusions on the overall song meaning.

## Clarifications and assumptions
- The combination of track name and artist is assumed to be a **unique key** for storing and searching existing songs for optimization. 

## Roadmap
**W** is *WIP*, **D** is *Done*
- (**D**) - Lyrics generator with transcription layer and vocals isolation
- (**D**) - Tracks and lyrics storage with json
- (**D**) - Single track meaning generation 
- (**W**) - Dynamics and key identifier
- (**W**) - AI integration with isolated dynamics
- (**W**) - Album meaning generation
- (**W**) - UI Overhaul