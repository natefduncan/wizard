from flask import Flask, Response, request, jsonify
app = Flask(__name__)

from wizard import tts
from wizard import utils
from wizard.playlist import create_playlist

def stream_playlist(name):
    def generate():
        with open("wizard/playlist/{name}.mp3", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/mpeg")

@app.route("/add-file", methods=["POST"])
def add():
    text = request.json.get("text")
    file_name = request.json.get("file_name")
    if text:
        speech = tts.text_to_speech(text)
        tts.speech_to_mp3(speech, f"wizard/audio/{file_name}.mp3")
        return jsonify({"message" : "OK"})
    else:
        return jsonify({"message" : "FAILURE"})

@app.route("/playlist/<name>")
def playlist(name):
    try:
        d = utils.json_to_dict("data.json")
    except Exception as e:
        return jsonify({"message" : e})
    playlist = d.get("playlists")
    if name in playlist:
        create_playlist(name, 10)
        return stream_playlist(name)
    else:
        return jsonify({"message" : "FAILURE"})

@app.route("/add-playlist", methods=["POST"])
def add_playlist():
    data = request.json
    d = utils.json_to_dict("data.json")
    if not "playlists" in d:
        d["playlists"] = {}
    d["playlists"][data.get("name")] = data.get("files")
    utils.dict_to_json(d, "data.json")
    return jsonify({"message" : "OK"})

@app.route("/files", methods=["GET"])
def files():
    f = utils.list_files("wizard/audio")
    return jsonify({"files" : f})

