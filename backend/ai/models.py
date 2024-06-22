from django.db import models

class ImageAnalysis(models.Model):
    image = models.ImageField(upload_to='images/')
    label = models.CharField(max_length=100, blank=True)
    predicted_label = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label
