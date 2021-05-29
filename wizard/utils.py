import os
import json
from pathlib import Path
from pydub import AudioSegment

def file_to_text(path):
    with open(path) as f:
        text = f.read()
    return text

def get_file_name(path):
    p = Path(path)
    return p.stem

def dict_to_json(d, path):
    with open(path, "w") as f: 
        json.dump(d, f)

def json_to_dict(path):
    with open(path) as f:
        d = json.load(f)
    return d

def list_files(path):
    return os.listdir(path)

def get_url():
    return json_to_dict("data.json").get("server")

def mp3_to_wav(mp3_path, wav_path):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")