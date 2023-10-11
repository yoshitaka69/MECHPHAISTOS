from django.db import models

from django.db import models

class Ce(models.Model):
    name      = models.CharField(max_length=256)
    industory = models.CharField(max_length=256)
    location  = models.CharField(max_length=256)

    def __str__(self):
        return self.name
