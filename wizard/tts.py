from gtts import gTTS

def text_to_speech(text):
    return gTTS(text)

def speech_to_wav(tts, path):
    tts.save(path)