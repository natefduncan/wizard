from flask import Flask, Response

app = Flask(__name__)

@app.route("/mp3")
def streammp3():
    def generate():
        with open("wizard/audio/stream.mp3", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/mpeg")