from django.db import models
from django.utils import timezone

#RepairingCostPM02
class RepairingCostPM02(models.Model):
    slug = models.SlugField()

    plant = models.CharField(verbose_name='plant',max_length=15)
    plannedPM02 = models.DecimalField(verbose_name='plannedPM02', max_digits=12, decimal_places=2,default=0)

class Meta:
    verbose_name_plural = 'Repairing Cost'
    ordering = ('-date_added',)