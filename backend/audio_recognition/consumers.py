import os
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import numpy as np
from vosk import Model, KaldiRecognizer, SetLogLevel

# Voskのログレベルを設定
SetLogLevel(-1)

# 絶対パスを使用してモデルを指定
model_path = os.path.join(os.path.dirname(__file__), '../models/vosk-model-small-en-us-0.15')
model = Model(model_path)

class AudioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connection established.")
        await self.accept()
    
    async def disconnect(self, close_code):
        print(f"WebSocket disconnected with close code: {close_code}")
    
    async def receive(self, bytes_data):
        try:
            print("Received data")
            audio_data = np.frombuffer(bytes_data, dtype=np.int16)
            print(f"Audio data: {audio_data}")
            recognizer = KaldiRecognizer(model, 16000)
            if recognizer.AcceptWaveform(audio_data):
                result = recognizer.Result()
                print(f"Recognition result: {result}")
                await self.send(text_data=json.dumps({
                    'transcript': result
                }))
            else:
                print("Recognition failed")
        except Exception as e:
            print(f"Error processing data: {e}")
            await self.close(code=1011)  # Internal error
            raise e  # 例外を再度スローして、上位レイヤでキャッチさせる

    async def websocket_disconnect(self, message):
        print("WebSocket disconnected")
        await super().websocket_disconnect(message)
