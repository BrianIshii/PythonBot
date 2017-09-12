import speech_recognition as sr

# [inp] -> str
# returns a string of the user's request
def listen(prompt=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        if prompt is True:
            inp = r.listen(source, timeout=1, phrase_time_limit=1)
        else:
            inp = r.listen(source)
    try:
        print(r.recognize_google(inp))
        return r.recognize_google(inp)
    except sr.UnknownValueError:
        print("bad input")
    except sr.RequestError as e:
        print("{0}".format(e))



