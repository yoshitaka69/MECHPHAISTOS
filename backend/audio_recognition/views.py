from django.shortcuts import render
from django.http import JsonResponse
from .models import MeetingRecording
from vosk import Model, KaldiRecognizer
import wave
import json
import os

# モデルの絶対パスを指定
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'vosk-model-small-en-us-0.15')
model = Model(model_path)

def upload_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']
        recording = MeetingRecording.objects.create(audio_file=audio_file)
        wf = wave.open(audio_file, 'rb')
        recognizer = KaldiRecognizer(model, wf.getframerate())
        transcription = []

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                transcription.append(result['text'])

        result = json.loads(recognizer.FinalResult())
        transcription.append(result['text'])

        transcript = ' '.join(transcription)
        recording.transcript = transcript
        recording.save()

        return JsonResponse({'transcript': transcript})

    return JsonResponse({'error': 'Invalid request'}, status=400)
