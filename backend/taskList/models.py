from django.db import models
from django.utils import timezone
from accounts.models import Company
#from ceList.models import Ce

#Taskは子。Ce　>　<<Task>>　> SpareParts
class Task(models.Model):
    slug = models.SlugField()


    #taskListNo = models.OneToOneField(Ce, on_delete=models.PROTECT, null=True, blank=True)

    latestPM02 = models.DateField(verbose_name='latestPM02', blank=True,null=True)
    latestPM03 = models.DateField(verbose_name='latestPM03', blank=True,null=True)
    latestPM04 = models.DateField(verbose_name='latestPM04', blank=True,null=True)
    taskOfPM02 = models.CharField(verbose_name='taskOfPM02',max_length=200,blank=True,null=True)
    laborCost = models.DecimalField(verbose_name='laborCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    partsName = models.CharField(verbose_name='partsName', max_length=200,blank=True,null=True)

    constructionPeriod = models.DateField(verbose_name='constructionPeriod', blank=True,null=True,default=timezone.now)
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


    #companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    #plant = models.ForeignKey(Ce, on_delete=models.CASCADE, null=True, blank=True)
    #equipment = models.ForeignKey(Ce, on_delete=models.CASCADE, null=True, blank=True)
    #function = models.ForeignKey(Ce, on_delete=models.CASCADE, null=True, blank=True)