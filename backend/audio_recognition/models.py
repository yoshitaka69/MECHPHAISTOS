from django.db import models

class MeetingRecording(models.Model):
    audio_file = models.FileField(upload_to='recordings/')
    transcript = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recording {self.id}"
