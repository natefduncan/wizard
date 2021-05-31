import os
import json
from pathlib import Path
from pydub import AudioSegment
import re
import shutil


HOME = os.path.expanduser('~')
DATA_PATH = f"{HOME}/.wizard/data.json"

def clear_directory(path):
    shutil.rmtree(path)
    Path(path).mkdir(parents=True, exist_ok=True)

def split_sentences(st): 
    sentences = re.split(r'[.?!]\s*', st)
    if sentences[-1]:
        return sentences
    else:
        return sentences[:-1]

def clean_string(string):
    return string.replace("\n", " ")

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
    return json_to_dict(DATA_PATH).get("server")

def mp3_to_wav(mp3_path, wav_path):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")