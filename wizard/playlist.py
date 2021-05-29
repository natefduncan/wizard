
from wizard import utils
from wizard import tts
from pydub import AudioSegment
from pathlib import Path

def create_playlist(name, length=5):
    data = utils.json_to_dict("data.json")
    playlists = data.get("playlists")
    if playlists:
        output = AudioSegment.silent(duration=1000)
        for file in playlists.get(name, []):
            speech = tts.text_to_speech(name.replace(".mp3", ""))
            tts.speech_to_mp3(speech, f"wizard/tmp/{file}")
            title = AudioSegment.from_mp3(f"wizard/tmp/{file}")
            mp3 = AudioSegment.from_mp3(f"wizard/audio/{file}")
            output += title
            output += AudioSegment.silent(duration=3000)
            output += mp3 
    repeat = int(length * 60 / len(output) / 1000)
    output = output * repeat
    Path('wizard/playlist').mkdir(parents=True, exist_ok=True)
    output.export(f"wizard/playlist/{name}.mp3", format="mp3")