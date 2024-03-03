from django.db import models
from django.utils import timezone

from accounts.models import Company
from ceList.models import Ce

#RepairingCostPM02
class Pm02(models.Model):
    slug = models.SlugField()

    companyCode = models.OneToOneField(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.OneToOneField(Ce, on_delete=models.PROTECT, null=True, blank=True)

    plannedPM02 = models.DecimalField(verbose_name='plannedPM02', max_digits=12, decimal_places=2,default=0)
    plannedMonth = models.DateField(verbose_name='plannedMonth',default=timezone.now)
    plannedCost = models.DecimalField(verbose_name='plannedCost', max_digits=12, decimal_places=2,default=0)
    totalPlannedPM02 = models.DecimalField(verbose_name='totalPlannedPM02', max_digits=12, decimal_places=2,default=0)

    actualPM02 = models.DecimalField(verbose_name='actualPM02', max_digits=12, decimal_places=2,default=0)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0)
    totalActualPM02 = models.DecimalField(verbose_name='totalActualPM02', max_digits=12, decimal_places=2,default=0)

    no1PlannedPM02 = models.DecimalField(verbose_name='no1PlannedPM02', max_digits=12, decimal_places=2,default=0)
    no1ActualPM02 = models.DecimalField(verbose_name='no1ActualPM02', max_digits=12, decimal_places=2,default=0)

class Meta:
    verbose_name_plural = 'Repairing Cost'
    ordering = ('-date_added',)

class Pm03(models.Model):
    slug = models.SlugField()

    companyCode = models.OneToOneField(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.OneToOneField(Ce, on_delete=models.PROTECT, null=True, blank=True)

    plannedPM03 = models.DecimalField(verbose_name='plannedPM03', max_digits=12, decimal_places=2,default=0)
    plannedMonth = models.DateField(verbose_name='plannedMonth',default=timezone.now)
    plannedCost = models.DecimalField(verbose_name='plannedCost', max_digits=12, decimal_places=2,default=0)
    totalPlannedPM03 = models.DecimalField(verbose_name='totalPlannedPM03', max_digits=12, decimal_places=2,default=0)

    actualPM03 = models.DecimalField(verbose_name='actualPM03', max_digits=12, decimal_places=2,default=0)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0)
    totalActualPM03 = models.DecimalField(verbose_name='totalActualPM03', max_digits=12, decimal_places=2,default=0)

    no1PlannedPM03 = models.DecimalField(verbose_name='no1PlannedPM03', max_digits=12, decimal_places=2,default=0)
    no1ActualPM03 = models.DecimalField(verbose_name='no1ActualPM03', max_digits=12, decimal_places=2,default=0)


class Pm04(models.Model):
    slug = models.SlugField()

    companyCode = models.OneToOneField(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.OneToOneField(Ce, on_delete=models.PROTECT, null=True, blank=True)

    actualPM04 = models.DecimalField(verbose_name='actualPM04', max_digits=12, decimal_places=2,default=0)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0)
    totalActualPM04 = models.DecimalField(verbose_name='totalActualPM04', max_digits=12, decimal_places=2,default=0)

    no1ActualPM04 = models.DecimalField(verbose_name='no1ActualPM04', max_digits=12, decimal_places=2,default=0)

class Pm05(models.Model):
    slug = models.SlugField()

    companyCode = models.OneToOneField(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.OneToOneField(Ce, on_delete=models.PROTECT, null=True, blank=True)
    
    plannedPM05 = models.DecimalField(verbose_name='plannedPM05', max_digits=12, decimal_places=2,default=0)
    plannedMonth = models.DateField(verbose_name='plannedMonth',default=timezone.now)
    plannedCost = models.DecimalField(verbose_name='plannedCost', max_digits=12, decimal_places=2,default=0)
    totalPlannedPM05 = models.DecimalField(verbose_name='totalPlannedPM05', max_digits=12, decimal_places=2,default=0)

    actualPM05 = models.DecimalField(verbose_name='actualPM05', max_digits=12, decimal_places=2,default=0)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0)
    totalActualPM05 = models.DecimalField(verbose_name='totalActualPM05', max_digits=12, decimal_places=2,default=0)

    no1PlannedPM05 = models.DecimalField(verbose_name='no1PlannedPM05', max_digits=12, decimal_places=2,default=0)
    no1ActualPM05 = models.DecimalField(verbose_name='no1ActualPM05', max_digits=12, decimal_places=2,default=0)