from gtts import gTTS

def text_to_speech(text):
    return gTTS(text)

def speech_to_mp3(tts, path):
    tts.save(path)