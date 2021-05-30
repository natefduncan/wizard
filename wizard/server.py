from flask import Flask, Response, request, jsonify, send_file
app = Flask(__name__)

from wizard import tts
from wizard import utils
from wizard.playlist import create_playlist

"""
def stream_playlist(name):
    def generate():
        with open(f"wizard/playlist/{name}.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/mpeg3")
"""
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
    text = request.json.get("text")
    file_name = request.json.get("file_name")
    if text:
        speech = tts.text_to_speech(text)
        tts.speech_to_file(speech, f"wizard/tmp/{file_name}.mp3")
        utils.mp3_to_wav(f"wizard/tmp/{file_name}.mp3", f"wizard/audio/{file_name}.wav")
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
        return streamwav(name)
        #return send_file(f"playlist/{name}.wav", as_attachment=True)
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

