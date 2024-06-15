from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    label = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.label
