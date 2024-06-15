import json
from channels.generic.websocket import AsyncWebsocketConsumer
import numpy as np
from vosk import Model, KaldiRecognizer

model = Model("vosk-model-small-en-us-0.15")

class AudioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        pass
    
    async def receive(self, bytes_data):
        audio_data = np.frombuffer(bytes_data, dtype=np.int16)
        recognizer = KaldiRecognizer(model, 16000)
        recognizer.AcceptWaveform(audio_data)
        result = recognizer.Result()
        await self.send(text_data=json.dumps({
            'transcript': result
        }))
