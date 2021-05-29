import os
import json
from pathlib import Path

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