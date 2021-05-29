
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
            speech = tts.text_to_speech(name.replace(".wav", ""))
            tts.speech_to_wav(speech, f"wizard/tmp/{file}")
            title = AudioSegment.from_wav(f"wizard/tmp/{file}")
            wav = AudioSegment.from_wav(f"wizard/audio/{file}")
            output += title
            output += AudioSegment.silent(duration=3000)
            output += wav 
    repeat = int(length * 60 / len(output) / 1000)
    output = output * repeat
    Path('wizard/playlist').mkdir(parents=True, exist_ok=True)
    output.export(f"wizard/playlist/{name}.wav", format="wav")