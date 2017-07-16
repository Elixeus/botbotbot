#!/usr/bin/env python

"""This is a demo file for speech recognition in python"""
# reference: https://pythonspot.com/en/speech-recognition-using-google-speech-api/

import speech_recognition as sr


# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print 'Microphone with name {name} found for Microphone(device_index={index})'.format(name=name, index=index)
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Please say your input')
    audio = r.listen(source)

print r.recognize_sphinx(audio)

# from pocketsphinx import LiveSpeech
# for phrase in LiveSpeech():
#     print phrase
