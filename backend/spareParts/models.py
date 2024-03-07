from django.db import models
from django.utils import timezone
from datetime import timedelta
from accounts.models import Company
from ceList.models import CeList


class SpareParts(models.Model):
    slug = models.SlugField()

    #CeListから引用
    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    plant = models.ForeignKey(CeList, on_delete=models.CASCADE, null=True, blank=True)
    equipment = models.CharField(verbose_name='equipment', max_length=200,null=True,blank=True)
    function = models.CharField(verbose_name='function', max_length=200,null=True,blank=True)

    #画像
    image = models.ImageField(verbose_name='image',)

    #parts 基本情報
    partsNo = models.CharField(verbose_name='partsName', max_length=200,blank=True,null=True)
    partsName = models.CharField(verbose_name='partsName', max_length=200,blank=True,null=True)
    partsModel = models.CharField(verbose_name='partsModel',max_length=200,blank=True,null=True)
    serialNumber = models.CharField(verbose_name='serialNumber',max_length=200,blank=True,null=True)
    category = models.CharField(verbose_name='category', max_length=200,blank=True,null=True)
    bomCode = models.PositiveIntegerField(verbose_name='bomNo',null=True,blank=True,default=0)

    #部品コスト
    partsCost = models.DecimalField(verbose_name='partsCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    numberOf = models.CharField(verbose_name='numberOf',max_length=200,blank=True,null=True)
    unit = models.CharField(verbose_name='unit',max_length=200,blank=True,null=True)

    #物理的な状況
    location = models.CharField(verbose_name='location',max_length=200,blank=True,null=True)
    stock = models.CharField(verbose_name='stock', max_length=200,null=True,blank=True)
    partsDeliveryTime = models.DateField(verbose_name='partsDeliveryTime', blank=True,null=True,default=timezone.now)

    #部品の説明
    partsDescription = models.TextField(verbose_name='partsDescription',blank=True,null=True,max_length=1000)


    class Meta:
        verbose_name = 'Spare Parts List'
        verbose_name_plural = 'Spare Parts List'
        ordering = ('partsName',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return self.partsName