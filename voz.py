from python_google_speak import speech_generator
from python_google_speak import speech_output

sound_generator = speech_generator.SpeechGenerator(p_locale="en_US")
sound_data = sound_generator.generate_audio_data("hello.")
speech_output.playback_audio_data(sound_data)
