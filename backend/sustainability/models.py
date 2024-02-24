from django.db import models
from django.utils import timezone

#Co2リスト
class Co2List(models.Model):
    slug = models.SlugField()

    plant = models.IntegerField(verbose_name='plant', default=0)
    date = models.IntegerField(verbose_name='date', default=0)
    co2Cost = models.IntegerField(verbose_name='co2Cost', default=0)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 


#STMリスト
class StmList(models.Model):
    slug = models.SlugField()

    plant = models.IntegerField(verbose_name='plant', default=0)
    date = models.IntegerField(verbose_name='date', default=0)
    stmCost = models.IntegerField(verbose_name='stmCost', default=0)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#ElectricityUsage
class ElectricityUsage(models.Model):
    slug = models.SlugField()

    plant = models.IntegerField(verbose_name='plant', default=0)
    date = models.IntegerField(verbose_name='date', default=0)
    elecCost = models.IntegerField(verbose_name='elecCost', default=0)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#compressorAir
class CompressedAir(models.Model):
    slug = models.SlugField()

    plant = models.IntegerField(verbose_name='plant', default=0)
    date = models.IntegerField(verbose_name='date', default=0)
    compAirCost = models.IntegerField(verbose_name='compAirCost', default=0)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#wellWater
class WellWater(models.Model):
    slug = models.SlugField()

    plant = models.IntegerField(verbose_name='plant', default=0)
    date = models.IntegerField(verbose_name='date', default=0)
    wellWaterCost = models.IntegerField(verbose_name='wellWaterCost', default=0)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#pureWater
class PureWater(models.Model):
    slug = models.SlugField()

    plant = models.IntegerField(verbose_name='plant', default=0)
    date = models.IntegerField(verbose_name='date', default=0)
    pureWaterCost = models.IntegerField(verbose_name='pureWaterCost', default=0)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#Wwt
class Wwt(models.Model):
    slug = models.SlugField()

    plant = models.IntegerField(verbose_name='plant', default=0)
    date = models.IntegerField(verbose_name='date', default=0)
    wwtCost = models.IntegerField(verbose_name='wwtCost', default=0)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)


#ExhaustGas
class ExhaustGas(models.Model):
    slug = models.SlugField()

    plant = models.IntegerField(verbose_name='plant', default=0)
    date = models.IntegerField(verbose_name='date', default=0)
    exhaustGasCost = models.IntegerField(verbose_name='exhaustGasCost', default=0)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)