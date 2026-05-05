import whisper
import core.isolator as isolator
from core.exceptions import *

def transcript(audio_name):

    try: 
        print("Separating vocal track...")
        vocals_file = isolator.isolate_vocals(audio_name)

    except ImportError:
        raise TranscriptionError

    print("Loading model for transcription...")
    model = whisper.load_model("base") # tiny, base, small, medium, large, turbo
    print("Done")

    print("Start of transcription...")
    print(vocals_file)
    result = model.transcribe(
        "media/isolated/vocals/" + vocals_file,
        language="en",                # Specify language to improve accuracy
        task="transcribe",            # Use "translate" to convert non-English to English
        fp16=False                    # Disable for CPU-only systems
    )
    print("Done")

    lyrics = format_lyrics(result)
    return lyrics


def format_lyrics(result):
    """
    Convert Whisper result to clean lyric card format.
    """
    
    # Optional: Split into lines at natural breaks (punctuation + line length)
    lines = []
    current_line = ""
    
    # Use segments to preserve timing-based line grouping
    for segment in result["segments"]:
        text = segment["text"].strip()
        if not text:
            continue
            
        # Add to current line, but break if too long or if we have a sentence end
        if current_line and (len(current_line) + len(text) > 50 or text.endswith(('.', '!', '?'))):
            lines.append(current_line)
            current_line = text
        else:
            if current_line:
                current_line += " " + text
            else:
                current_line = text
    
    if current_line:
        lines.append(current_line)
    
    # Join with newlines
    lyric_card = "\n".join(lines)
    return lyric_card