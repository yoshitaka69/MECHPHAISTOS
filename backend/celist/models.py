from django.db import models
from django.utils import timezone

class Ce(models.Model):
    slug = models.SlugField()

    ceListNo = models.PositiveIntegerField(verbose_name='ceListNo', null=True,blank=True,default=0)
    companyCode = models.CharField(verbose_name='companyCode', max_length=200,null=True,blank=True)
    plant = models.CharField(verbose_name='plant', max_length=200,null=True,blank=True)
    locationNo = models.CharField(verbose_name='locationNo', max_length=200,null=True,blank=True)
    function = models.CharField(verbose_name='function', max_length=200,null=True,blank=True)
    equipment = models.CharField(verbose_name='equipment', max_length=200,null=True,blank=True)
    bomNo = models.CharField(verbose_name='bomNo', max_length=200,null=True,blank=True)#BomNoは設備-Noとかするかも
    totalBomCost = models.DecimalField(verbose_name='totalBomCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00,)

    valueImpact = models.CharField(verbose_name='valueImpact', max_length=200)
    constructionPeriod = models.CharField(verbose_name='constructionPeriod', max_length=200)
    partsDeliveryTime = models.CharField(verbose_name='partsDeliveryTime', max_length=200)
    mttr = models.CharField(verbose_name='mttr', max_length=200)

    # PM02
    countOfPM02 = models.CharField(verbose_name='countOfPM02', max_length=200)
    latestPM02 = models.CharField(verbose_name='latestPM02', max_length=200)
    taskOfPM02 = models.CharField(verbose_name='taskOfPM02', max_length=200)
    # PM03
    countOfPM03 = models.CharField(verbose_name='countOfPM03', max_length=200)
    latestPM03 = models.CharField(verbose_name='latestPM03', max_length=200)
    taskOfPM03 = models.CharField(verbose_name='taskOfPM03', max_length=200)
    # PM04
    countOfPM04 = models.CharField(verbose_name='countOfPM04', max_length=200)
    latestPM04 = models.CharField(verbose_name='latestPM04', max_length=200)
    taskOfPM04 = models.CharField(verbose_name='taskOfPM04', max_length=200)
    # PM005
    countOfPM05 = models.CharField(verbose_name='countOfPM05', max_length=200)
    latestPM05 = models.CharField(verbose_name='latestPM05', max_length=200)
    taskOfPM05 = models.CharField(verbose_name='taskOfPM05', max_length=200)

    nextEventDate = models.CharField(verbose_name='nextEventDate', max_length=200)
    situation = models.CharField(verbose_name='situation', max_length=200)
    ceDescription = models.CharField(verbose_name='ceDescription', max_length=200)

    thisYear10ago = models.BooleanField(verbose_name='thisYear10ago',  default=False,)
    thisYear9ago = models.BooleanField(verbose_name='thisYear9ago',  default=False,)
    thisYear8ago = models.BooleanField(verbose_name='thisYear8ago', default=False,)
    thisYear7ago = models.BooleanField(verbose_name='thisYear7ago',  default=False,)
    thisYear6ago = models.BooleanField(verbose_name='thisYear6ago',  default=False,)
    thisYear5ago = models.BooleanField(verbose_name='thisYear5ago',  default=False,)
    thisYear4ago = models.BooleanField(verbose_name='thisYear4ago',  default=False,)
    thisYear3ago = models.BooleanField(verbose_name='thisYear3ago',  default=False,)
    thisYear2ago = models.BooleanField(verbose_name='thisYear2ago',  default=False,)
    thisYear1ago = models.BooleanField(verbose_name='thisYear1ago',  default=False,)
    thisYear = models.CharField(verbose_name='thisYear', max_length=200)#今年だけは文字列を表示する可能性があるのでcharField
    thisYear1later = models.BooleanField(verbose_name='thisYear1later',  default=False,)
    thisYear2later = models.BooleanField(verbose_name='thisYear2later', default=False,)
    thisYear3later = models.BooleanField(verbose_name='thisYear3later', max_length=200)
    thisYear4later = models.BooleanField(verbose_name='thisYear4later', max_length=200)
    thisYear5later = models.BooleanField(verbose_name='thisYear5later', max_length=200)
    thisYear6later = models.BooleanField(verbose_name='thisYear6later', max_length=200)
    thisYear7later = models.BooleanField(verbose_name='thisYear7later', max_length=200)
    thisYear8later = models.BooleanField(verbose_name='thisYear8later', max_length=200)
    thisYear9later = models.BooleanField(verbose_name='thisYear9later', max_length=200)
    thisYear10later = models.BooleanField(verbose_name='thisYear10later', max_length=200)

    """記入した日付を記入してくれる"""
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 

class Meta:
    verbose_name_plural = 'Critical equipment list'
    ordering = ('-date_added',)


class SpareParts(models.Model):
    slug = models.SlugField()

    image = models.ImageField(verbose_name='image',)
    partsName = models.CharField(verbose_name='partsName', max_length=200)
    category = models.CharField(verbose_name='category', max_length=200)
    partsModel = models.IntegerField(verbose_name='partsModel', default=0)
    serialNumber = models.CharField(verbose_name='serialNumber', max_length=200)
    taskListNo = models.CharField(verbose_name='taskListNo', max_length=200)
    partsCost = models.IntegerField(verbose_name='partsCost', default=0)
    numberOf = models.CharField(verbose_name='numberOf', max_length=200)
    unit = models.CharField(verbose_name='unit', max_length=200)
    location = models.IntegerField(verbose_name='location', default=0)
    partsDeliveryTime = models.CharField(verbose_name='partsDeliveryTime', max_length=200)
    partsDescription = models.CharField(verbose_name='partsDescription', max_length=200)


class Task(models.Model):
    slug = models.SlugField()

    plant = models.ImageField(verbose_name='plant',)
    equipment = models.CharField(verbose_name='equipment', max_length=200)
    function = models.CharField(verbose_name='function', max_length=200)
    latestPM02 = models.IntegerField(verbose_name='latestPM02', default=0)
    latestPM03 = models.CharField(verbose_name='latestPM03', max_length=200)
    latestPM04 = models.CharField(verbose_name='latestPM04', max_length=200)
    taskOfPM02 = models.IntegerField(verbose_name='taskOfPM02', default=0)
    laborCost = models.CharField(verbose_name='laborCost', max_length=200)
    partsName = models.CharField(verbose_name='partsName', max_length=200)
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriod', default=0)
    nextEventDate = models.CharField(verbose_name='nextEventDate', max_length=200)
    situation = models.CharField(verbose_name='situation', max_length=200)
    thisYear10ago = models.CharField(verbose_name='thisYear10ago', max_length=200)
    thisYear9ago = models.CharField(verbose_name='thisYear9ago', max_length=200)
    thisYear8ago = models.CharField(verbose_name='thisYear8ago', max_length=200)
    thisYear7ago = models.CharField(verbose_name='thisYear7ago', max_length=200)
    thisYear6ago = models.CharField(verbose_name='thisYear6ago', max_length=200)
    thisYear5ago = models.CharField(verbose_name='thisYear5ago', max_length=200)
    thisYear4ago = models.CharField(verbose_name='thisYear4ago', max_length=200)
    thisYear3ago = models.CharField(verbose_name='thisYear3ago', max_length=200)
    thisYear2ago = models.CharField(verbose_name='thisYear2ago', max_length=200)
    thisYear1ago = models.CharField(verbose_name='thisYear1ago', max_length=200)
    thisYear = models.CharField(verbose_name='thisYear', max_length=200)
    thisYear1later = models.CharField(verbose_name='thisYear1later', max_length=200)
    thisYear2later = models.CharField(verbose_name='thisYear2later', max_length=200)
    thisYear3later = models.CharField(verbose_name='thisYear3later', max_length=200)
    thisYear4later = models.CharField(verbose_name='thisYear4later', max_length=200)
    thisYear5later = models.CharField(verbose_name='thisYear5later', max_length=200)
    thisYear6later = models.CharField(verbose_name='thisYear6later', max_length=200)
    thisYear7later = models.CharField(verbose_name='thisYear7later', max_length=200)
    thisYear8later = models.CharField(verbose_name='thisYear8later', max_length=200)
    thisYear9later = models.CharField(verbose_name='thisYear9later', max_length=200)
    thisYear10later = models.CharField(verbose_name='thisYear10later', max_length=200)