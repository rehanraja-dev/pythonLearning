from gtts import gTTS

tts = gTTS("यह हिंदी में एक उदाहरण है", lang='hi')
tts.save('hello.mp3')

