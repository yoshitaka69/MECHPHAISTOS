from django.db import models
from django.utils import timezone

#Co2リスト
class Co2(models.Model):
    slug = models.SlugField()

    plant = models.CharField(verbose_name='plant', max_length=200, default='', null=True, blank=True)
    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    co2Cost = models.DecimalField(verbose_name='co2Cost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 

#STMリスト
class Stm(models.Model):
    slug = models.SlugField()

    plant = models.CharField(verbose_name='plant', max_length=200, default='', null=True, blank=True)
    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    stmCost = models.DecimalField(verbose_name='stmCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#ElectricityUsage
class ElectricityUsage(models.Model):
    slug = models.SlugField()

    plant = models.CharField(verbose_name='plant', max_length=200, default='', null=True, blank=True)
    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    elecCost = models.DecimalField(verbose_name='elecCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#compressorAir
class CompressedAir(models.Model):
    slug = models.SlugField()

    plant = models.CharField(verbose_name='plant', max_length=200, default='', null=True, blank=True)
    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    compAirCost = models.DecimalField(verbose_name='compAirCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#wellWater
class WellWater(models.Model):
    slug = models.SlugField()

    plant = models.CharField(verbose_name='plant', max_length=200, default='', null=True, blank=True)
    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    wellWaterCost = models.DecimalField(verbose_name='wellWaterCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#pureWater
class PureWater(models.Model):
    slug = models.SlugField()

    plant = models.CharField(verbose_name='plant', max_length=200, default='', null=True, blank=True)
    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    pureWaterCost = models.DecimalField(verbose_name='pureWaterCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#Wwt
class Wwt(models.Model):
    slug = models.SlugField()

    plant = models.CharField(verbose_name='plant', max_length=200, default='', null=True, blank=True)
    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    wwtCost = models.DecimalField(verbose_name='wwtCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#ExhaustGas
class ExhaustGas(models.Model):
    slug = models.SlugField()

    plant = models.CharField(verbose_name='plant', max_length=200, default='', null=True, blank=True)
    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)