from audio_separator.separator import Separator
from pathlib import Path
from core.exceptions import *

def isolate_vocals(song_name):
    """
    Isolate vocals using audio-separator (supports Demucs under the hood).
    Returns path to the extracted vocal track.
    """
    # Create output directory
    Path("media/isolated/vocals").mkdir(parents=True, exist_ok=True)

    # Initialize separator (first run downloads the model)
    separator = Separator(
        output_dir="media/isolated/vocals",
        output_single_stem="Vocals",           # Only generate the vocal track
        model_file_dir="models",               # Cache downloaded models locally
    )

    # assign model (good for vocal parts)
    separator.load_model(model_filename="UVR_MDXNET_KARA_2.onnx")

    # Separate the audio file
    output_files = separator.separate("media/input/" + song_name)

    # `output_files` is a list of generated files, e.g., ['.../vocals.wav']
    vocals_path = output_files[0] if output_files else None

    if not vocals_path:
        raise IsolationException

    print(f"Vocals saved to: {vocals_path}")
    return vocals_path