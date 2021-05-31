
from wizard import utils
from wizard import tts
from pydub import AudioSegment
from pathlib import Path

def create_playlist(name, length=5):
    data = utils.json_to_dict(utils.DATA_PATH)
    playlists = data.get("playlists")
    if playlists:
        output = AudioSegment.silent(duration=1000)
        for file in playlists.get(name, []):
            no_ex = file.replace(".wav", "")
            speech = tts.text_to_speech(no_ex)
            tts.speech_to_file(speech, f"wizard/tmp/{no_ex}.mp3")
            utils.mp3_to_wav(f"wizard/tmp/{no_ex}.mp3", f"wizard/tmp/{no_ex}.wav")
            title = AudioSegment.from_wav(f"wizard/tmp/{no_ex}.wav")
            wav = AudioSegment.from_wav(f"wizard/audio/{file}")
            output += title
            output += AudioSegment.silent(duration=2000)
            output += wav 
            output += AudioSegment.silent(duration=2000)
    repeat = int(float(length * 60) / float(len(output) / 1000))
    output = output * max([repeat,1])
    Path('wizard/playlist').mkdir(parents=True, exist_ok=True)
    output.export(f"wizard/playlist/{name}.wav", format="wav")