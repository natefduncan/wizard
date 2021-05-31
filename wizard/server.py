import os
from pathlib import Path

from flask import Flask, Response, request, jsonify, send_file, render_template
app = Flask(__name__)

from wizard import tts
from wizard import utils
from wizard.playlist import create_playlist

def streamwav(name):
    def generate():
        with open(f"wizard/playlist/{name}.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@app.route("/add-file", methods=["POST"])
def add():
    lines = request.json.get("lines")
    file_name = request.json.get("file_name")
    if lines:
        Path(f'wizard/static/audio/{file_name}').mkdir(parents=True, exist_ok=True)
        utils.clear_directory(f'wizard/static/audio/{file_name}')
        for idx, line in enumerate(lines):
            speech = tts.text_to_speech(line)
            tts.speech_to_file(speech, f"wizard/static/audio/{file_name}/{file_name}-{str(idx+1)}.mp3")
        return jsonify({"message" : "OK"})
    else:
        return jsonify({"message" : "FAILURE"})

@app.route("/play/<name>")
def play(name):
    names = [i.replace(".mp3", "") for i in utils.list_files(f"wizard/static/audio/{name}")]
    names = sorted(names, key=lambda x : int(x.split("-")[1]))
    print(names)
    return render_template("player.html", names=names)

@app.route("/add-playlist", methods=["POST"])
def add_playlist():
    data = request.json
    d = utils.json_to_dict(utils.DATA_PATH)
    if not "playlists" in d:
        d["playlists"] = {}
    d["playlists"][data.get("name")] = data.get("files")
    utils.dict_to_json(d, utils.DATA_PATH)
    return jsonify({"message" : "OK"})

@app.route("/files", methods=["GET"])
def files():
    f = utils.list_files("wizard/static/audio")
    return jsonify({"files" : f})

