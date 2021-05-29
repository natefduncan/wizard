from gtts import gTTS

def text_to_speech(text):
    return gTTS(text)

def speech_to_file(tts, path):
    tts.save(path)