from django.db import models
from django.utils import timezone
from datetime import timedelta
from accounts.models import Company
#from ceList.models import Ce


class SpareParts(models.Model):
    slug = models.SlugField()

    #companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    #plant = models.ForeignKey(Ce, on_delete=models.CASCADE, null=True, blank=True)

    image = models.ImageField(verbose_name='image',)
    bomNo = models.PositiveIntegerField(verbose_name='bomNo',null=True,blank=True,default=0)

    #parts 基本情報
    partsName = models.CharField(verbose_name='partsName', max_length=200,blank=True,null=True)
    partsModel = models.CharField(verbose_name='partsModel',max_length=200,blank=True,null=True)
    serialNumber = models.CharField(verbose_name='serialNumber',max_length=200,blank=True,null=True)
    category = models.CharField(verbose_name='category', max_length=200,blank=True,null=True)

    #部品コスト
    partsCost = models.DecimalField(verbose_name='partsCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    numberOf = models.CharField(verbose_name='numberOf',max_length=200,blank=True,null=True)
    unit = models.CharField(verbose_name='unit',max_length=200,blank=True,null=True)

    #物理的な状況
    location = models.CharField(verbose_name='location',max_length=200,blank=True,null=True)
    stock = models.CharField(verbose_name='stock', max_length=200,null=True,blank=True)

    #taskListNo = models.ForeignKey(Task, on_delete=models.PROTECT, null=True, blank=True)
    partsDeliveryTime = models.DateField(verbose_name='partsDeliveryTime', blank=True,null=True,default=timezone.now)
    partsDescription = models.TextField(verbose_name='partsDescription',blank=True,null=True,max_length=1000)

