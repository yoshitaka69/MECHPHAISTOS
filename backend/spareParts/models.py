from django.db import models
from django.utils import timezone
from datetime import timedelta
from accounts.models import CompanyCode,CompanyName
from ceList.models import Plant,Equipment,Machine

class Category(models.Model):
   category = models.CharField(verbose_name='category', max_length=10,blank=True,null=True)
   description = models.TextField(verbose_name='category', max_length=200,blank=True,null=True)
   class Meta:
      verbose_name = 'Category'
      verbose_name_plural = 'Category'
      ordering = ('category',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
   def __str__(self):
        return f'{self.category}'


class Location(models.Model):
     
   companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='location_companyCode', null=True, blank=True)
   companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='location_companyName', null=True, blank=True)
   location_Id = models.CharField(verbose_name='location_id', max_length=200,blank=True,null=True)
   location = models.CharField(verbose_name='location', max_length=200,blank=True,null=True)
   class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Location'
        ordering = ('location',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
   def __str__(self):
        return f'{self.location}'


class Classification(models.Model):
     
   classification = models.CharField(verbose_name='classification', max_length=200,blank=True,null=True)
   description = models.TextField(verbose_name='description', max_length=200,blank=True,null=True)
   class Meta:
      verbose_name = 'Classification'
      verbose_name_plural = 'Classification'
      ordering = ('classification',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
   def __str__(self):
        return f'{self.classification}'


class SpareParts(models.Model):

    #CeListから引用
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='spareParts_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='spareParts_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='spareParts_plant', null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='spareParts_equipment', null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='spareParts_machineName', null=True, blank=True)

    #画像
    image = models.ImageField(verbose_name='image',null=True,blank=True)

    #parts 基本情報
    bomCode = models.PositiveIntegerField(verbose_name='bomNo',null=True,blank=True,default=0)
    partsNo = models.CharField(verbose_name='partsName', max_length=200,blank=True,null=True)
    partsName = models.CharField(verbose_name='partsName', max_length=200,blank=True,null=True)
    partsModel = models.CharField(verbose_name='partsModel',max_length=200,blank=True,null=True)
    serialNumber = models.CharField(verbose_name='serialNumber',max_length=200,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='spareParts_category', null=True, blank=True)#ここは間違いなくPROTECT

    #部品コスト
    partsCost = models.DecimalField(verbose_name='partsCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    numberOf = models.CharField(verbose_name='numberOf',max_length=200,blank=True,null=True)
    unit = models.CharField(verbose_name='unit',max_length=200,blank=True,null=True)

    #物理的な状況
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='spareParts_location', null=True, blank=True)#ここは間違いなくPROTECT
    stock = models.CharField(verbose_name='stock', max_length=200,null=True,blank=True)
    partsDeliveryTime = models.DateField(verbose_name='partsDeliveryTime', blank=True,null=True,default=timezone.now)

    #部品の説明
    classification = models.ForeignKey(Classification, on_delete=models.PROTECT, related_name='spareParts_classification', null=True, blank=True)#ここは間違いなくPROTECT
    inventoryTurnover = models.CharField(verbose_name='classification',max_length=200,blank=True,null=True)
    partsDescription = models.TextField(verbose_name='partsDescription',blank=True,null=True,max_length=1000)



    class Meta:
        verbose_name = 'Spare Parts List'
        verbose_name_plural = 'Spare Parts List'
        ordering = ('partsName',) 


    def __str__(self):
            return f'{self.partsName}'


class SparePartsAlertNextMonth(models.Model):
   companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='spareParts_companyCode', null=True, blank=True)
   companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='spareParts_companyName', null=True, blank=True)
   plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='spareParts_plant', null=True, blank=True)

   nextMonthOrder1 = models.CharField(verbose_name='nextMonthorder1',max_length=200,blank=True,null=True)
   nextMonthOrder2 = models.CharField(verbose_name='nextMonthorder2',max_length=200,blank=True,null=True)
   nextMonthOrder3 = models.CharField(verbose_name='nextMonthorder3',max_length=200,blank=True,null=True)
   nextMonthOrder4 = models.CharField(verbose_name='nextMonthorder4',max_length=200,blank=True,null=True)
   nextMonthOrder5 = models.CharField(verbose_name='nextMonthorder5',max_length=200,blank=True,null=True)
   nextMonthOrder6 = models.CharField(verbose_name='nextMonthorder6',max_length=200,blank=True,null=True)
   nextMonthOrder7 = models.CharField(verbose_name='nextMonthorder7',max_length=200,blank=True,null=True)
   nextMonthOrder8 = models.CharField(verbose_name='nextMonthorder8',max_length=200,blank=True,null=True)
   nextMonthOrder9 = models.CharField(verbose_name='nextMonthorder9',max_length=200,blank=True,null=True)
   nextMonthOrder10 = models.CharField(verbose_name='nextMonthorder10',max_length=200,blank=True,null=True)
   nextMonthOrder11 = models.CharField(verbose_name='nextMonthorder11',max_length=200,blank=True,null=True)
   nextMonthOrder12 = models.CharField(verbose_name='nextMonthorder12',max_length=200,blank=True,null=True)
   nextMonthOrder13 = models.CharField(verbose_name='nextMonthorder13',max_length=200,blank=True,null=True)
   nextMonthOrder14 = models.CharField(verbose_name='nextMonthorder14',max_length=200,blank=True,null=True)
   nextMonthOrder15 = models.CharField(verbose_name='nextMonthorder15',max_length=200,blank=True,null=True)

   class Meta:
        verbose_name = 'SparePartsAlertNextMonth'
        verbose_name_plural = 'SparePartsAlertNextMonth'
        ordering = ('companyCode',) 

    def __str__(self):
            return str'(nextMonthOrder)'
   
