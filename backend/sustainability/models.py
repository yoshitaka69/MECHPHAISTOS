from django.db import models
from django.utils import timezone
from accounts.models import Company
from ceList.models import CeList


#Co2リスト
class Co2(models.Model):
    slug = models.SlugField()

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.ForeignKey(CeList, on_delete=models.PROTECT, null=True, blank=True)

    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    co2Cost = models.DecimalField(verbose_name='co2Cost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 

    class Meta:
            verbose_name = 'Co2 list'
            verbose_name_plural = 'Co2 List'
            ordering = ('date',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    
    def __str__(self):
        return self.co2Cost



#STMリスト
class Stm(models.Model):
    slug = models.SlugField()

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.ForeignKey(CeList, on_delete=models.PROTECT, null=True, blank=True)

    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    stmCost = models.DecimalField(verbose_name='stmCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Stm list'
            verbose_name_plural = 'Stm List'
            ordering = ('date',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    
    def __str__(self):
        return self.stmCost




#ElectricityUsage
class ElectricityUsage(models.Model):
    slug = models.SlugField()

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.ForeignKey(CeList, on_delete=models.PROTECT, null=True, blank=True)

    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    elecCost = models.DecimalField(verbose_name='elecCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Elec list'
            verbose_name_plural = 'Elec List'
            ordering = ('date',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    
    def __str__(self):
        return self.elecCost





#compressorAir
class CompressedAir(models.Model):
    slug = models.SlugField()

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.ForeignKey(CeList, on_delete=models.PROTECT, null=True, blank=True)

    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    compAirCost = models.DecimalField(verbose_name='compAirCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'CompAir list'
            verbose_name_plural = 'CompAir List'
            ordering = ('date',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    
    def __str__(self):
        return self.compAirCost



#wellWater
class WellWater(models.Model):
    slug = models.SlugField()

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.ForeignKey(CeList, on_delete=models.PROTECT, null=True, blank=True)

    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    wellWaterCost = models.DecimalField(verbose_name='wellWaterCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'wellWater list'
            verbose_name_plural = 'wellWater List'
            ordering = ('date',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    
    def __str__(self):
        return self.wellWaterCost



#pureWater
class PureWater(models.Model):
    slug = models.SlugField()

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.ForeignKey(CeList, on_delete=models.PROTECT, null=True, blank=True)

    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    pureWaterCost = models.DecimalField(verbose_name='pureWaterCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'pureWater list'
            verbose_name_plural = 'pureWater List'
            ordering = ('date',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    
    def __str__(self):
        return self.pureWaterCost

#Wwt
class Wwt(models.Model):
    slug = models.SlugField()

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.ForeignKey(CeList, on_delete=models.PROTECT, null=True, blank=True)

    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    wwtCost = models.DecimalField(verbose_name='wwtCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'wwt list'
            verbose_name_plural = 'wwt List'
            ordering = ('date',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    
    def __str__(self):
        return self.wwtCost

#ExhaustGas
class ExhaustGas(models.Model):
    slug = models.SlugField()

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    plant = models.ForeignKey(CeList, on_delete=models.PROTECT, null=True, blank=True)

    date = models.DateField(verbose_name='date', blank=True, null=True, default=timezone.now)
    exhaustGasCost = models.DecimalField(verbose_name='exhaustGasCost', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00,)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True)

    
    class Meta:
            verbose_name = 'exhaustGas list'
            verbose_name_plural = 'exhaustGas List'
            ordering = ('date',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    
    def __str__(self):
        return self.exhaustGasCost
