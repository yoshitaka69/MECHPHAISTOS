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
    constructionPeriod = models.DurationField(verbose_name='constructionPeriod',blank=True,null=True,default=0)
    partsDeliveryTime = models.DurationField(verbose_name='partsDeliveryTime', blank=True,null=True,default=0)
    mttr = models.PositiveSmallIntegerField(verbose_name='mttr',blank=True,null=True,default=0)

    # PM02
    countOfPM02 = models.PositiveSmallIntegerField(verbose_name='countOfPM02',blank=True,null=True,default=0)
    latestPM02 = models.DateField(verbose_name='latestPM02',blank=True,null=True)
    taskOfPM02 = models.CharField(verbose_name='taskOfPM02', max_length=200)
    # PM03
    countOfPM03 = models.PositiveSmallIntegerField(verbose_name='countOfPM03',blank=True,null=True,default=0)
    latestPM03 = models.DateField(verbose_name='latestPM03',blank=True,null=True)
    taskOfPM03 = models.CharField(verbose_name='taskOfPM03', max_length=200)
    # PM04
    countOfPM04 = models.PositiveSmallIntegerField(verbose_name='countOfPM04',blank=True,null=True,default=0)
    latestPM04 = models.DateField(verbose_name='latestPM04', blank=True,null=True)
    taskOfPM04 = models.CharField(verbose_name='taskOfPM04', max_length=200,blank=True,null=True)
    # PM005
    countOfPM05 = models.PositiveSmallIntegerField(verbose_name='countOfPM05', blank=True,null=True,default=0,)
    latestPM05 = models.DateField(verbose_name='latestPM05', blank=True,null=True)
    taskOfPM05 = models.CharField(verbose_name='taskOfPM05', max_length=200,blank=True,null=True)

    nextEventDate = models.DateField(verbose_name='nextEventDate', blank=True,null=True)
    situation = models.CharField(verbose_name='situation', max_length=200,null=True,blank=True)
    ceDescription = models.TextField(verbose_name='ceDescription',blank=True,null=True,max_length=1000)

    thisYear10ago = models.BooleanField(verbose_name='thisYear10ago',default=False)
    thisYear9ago = models.BooleanField(verbose_name='thisYear9ago', default=False)
    thisYear8ago = models.BooleanField(verbose_name='thisYear8ago', default=False)
    thisYear7ago = models.BooleanField(verbose_name='thisYear7ago', default=False)
    thisYear6ago = models.BooleanField(verbose_name='thisYear6ago', default=False)
    thisYear5ago = models.BooleanField(verbose_name='thisYear5ago', default=False)
    thisYear4ago = models.BooleanField(verbose_name='thisYear4ago', default=False)
    thisYear3ago = models.BooleanField(verbose_name='thisYear3ago', default=False)
    thisYear2ago = models.BooleanField(verbose_name='thisYear2ago', default=False)
    thisYear1ago = models.BooleanField(verbose_name='thisYear1ago', default=False)
    thisYear = models.CharField(verbose_name='thisYear', max_length=200)#今年だけは文字列を表示する可能性があるのでcharField
    thisYear1later = models.BooleanField(verbose_name='thisYear1later', default=False)
    thisYear2later = models.BooleanField(verbose_name='thisYear2later', default=False)
    thisYear3later = models.BooleanField(verbose_name='thisYear3later', default=False)
    thisYear4later = models.BooleanField(verbose_name='thisYear4later', default=False)
    thisYear5later = models.BooleanField(verbose_name='thisYear5later', default=False)
    thisYear6later = models.BooleanField(verbose_name='thisYear6later', default=False)
    thisYear7later = models.BooleanField(verbose_name='thisYear7later', default=False)
    thisYear8later = models.BooleanField(verbose_name='thisYear8later', default=False)
    thisYear9later = models.BooleanField(verbose_name='thisYear9later', default=False)
    thisYear10later = models.BooleanField(verbose_name='thisYear10later', default=False)

    """記入した日付を記入してくれる"""
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 

class Meta:
    verbose_name_plural = 'Critical equipment list'
    ordering = ('-date_added',)


class SpareParts(models.Model):
    slug = models.SlugField()

    image = models.ImageField(verbose_name='image',)
    partsName = models.CharField(verbose_name='partsName', max_length=200,blank=True,null=True)
    category = models.CharField(verbose_name='category', max_length=200,blank=True,null=True)
    partsModel = models.CharField(verbose_name='partsModel',max_length=200,blank=True,null=True)
    serialNumber = models.CharField(verbose_name='serialNumber',max_length=200,blank=True,null=True)
    taskListNo = models.CharField(verbose_name='taskListNo',max_length=200,blank=True,null=True)
    partsCost = models.DecimalField(verbose_name='partsCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    numberOf = models.CharField(verbose_name='numberOf',max_length=200,blank=True,null=True)
    unit = models.CharField(verbose_name='unit',max_length=200,blank=True,null=True)
    location = models.CharField(verbose_name='location',max_length=200,blank=True,null=True)
    partsDeliveryTime = models.DurationField(verbose_name='partsDeliveryTime',blank=True,null=True,default=0)
    partsDescription = models.TextField(verbose_name='partsDescription',blank=True,null=True,max_length=1000)

class Task(models.Model):
    slug = models.SlugField()

    plant = models.ImageField(verbose_name='plant',)
    equipment = models.CharField(verbose_name='equipment', max_length=200,blank=True,null=True)
    function = models.CharField(verbose_name='function', max_length=200,blank=True,null=True)
    latestPM02 = models.DateField(verbose_name='latestPM02', blank=True,null=True)
    latestPM03 = models.DateField(verbose_name='latestPM03', blank=True,null=True)
    latestPM04 = models.DateField(verbose_name='latestPM04', blank=True,null=True)
    taskOfPM02 = models.CharField(verbose_name='taskOfPM02',max_length=200,blank=True,null=True)
    laborCost = models.DecimalField(verbose_name='laborCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    partsName = models.CharField(verbose_name='partsName', max_length=200,blank=True,null=True)
    constructionPeriod = models.DurationField(verbose_name='constructionPeriod', blank=True,null=True,default=0)
    nextEventDate = models.DateField(verbose_name='nextEventDate',blank=True,null=True)
    situation = models.CharField(verbose_name='situation', max_length=200,blank=True,null=True)
    thisYear10ago = models.BooleanField(verbose_name='thisYear10ago',default=False)
    thisYear9ago = models.BooleanField(verbose_name='thisYear9ago',default=False)
    thisYear8ago = models.BooleanField(verbose_name='thisYear8ago',default=False)
    thisYear7ago = models.BooleanField(verbose_name='thisYear7ago',default=False)
    thisYear6ago = models.BooleanField(verbose_name='thisYear6ago',default=False)
    thisYear5ago = models.BooleanField(verbose_name='thisYear5ago',default=False)
    thisYear4ago = models.BooleanField(verbose_name='thisYear4ago',default=False)
    thisYear3ago = models.BooleanField(verbose_name='thisYear3ago',default=False)
    thisYear2ago = models.BooleanField(verbose_name='thisYear2ago',default=False)
    thisYear1ago = models.BooleanField(verbose_name='thisYear1ago',default=False)
    thisYear = models.CharField(verbose_name='thisYear', max_length=200)
    thisYear1later = models.BooleanField(verbose_name='thisYear1later',default=False)
    thisYear2later = models.BooleanField(verbose_name='thisYear2later',default=False)
    thisYear3later = models.BooleanField(verbose_name='thisYear3later',default=False)
    thisYear4later = models.BooleanField(verbose_name='thisYear4later',default=False)
    thisYear5later = models.BooleanField(verbose_name='thisYear5later',default=False)
    thisYear6later = models.BooleanField(verbose_name='thisYear6later',default=False)
    thisYear7later = models.BooleanField(verbose_name='thisYear7later',default=False)
    thisYear8later = models.BooleanField(verbose_name='thisYear8later',default=False)
    thisYear9later = models.BooleanField(verbose_name='thisYear9later',default=False)
    thisYear10later = models.BooleanField(verbose_name='thisYear10later',default=False)