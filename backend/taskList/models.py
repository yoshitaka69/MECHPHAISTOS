from django.db import models
from django.utils import timezone
from accounts.models import Company
#from ceList.models import CeList


class TaskList(models.Model):
    slug = models.SlugField()

    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    
    #CeListから
    taskCode = models.CharField(verbose_name='taskCode',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskName',max_length=200,blank=True,null=True)
    #plant = models.ForeignKey(CeList, on_delete=models.CASCADE, null=True, blank=True)
    #equipment = models.ForeignKey(CeList, on_delete=models.CASCADE, null=True, blank=True)
    #function = models.ForeignKey(CeList, on_delete=models.CASCADE, null=True, blank=True)
    
    # taskList
    taskOfPM = models.CharField(verbose_name='taskOfPM',max_length=200,blank=True,null=True)
    laborCostOfPM = models.DecimalField(verbose_name='laborCostOfPM',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    countOfPM = models.PositiveSmallIntegerField(verbose_name='countOfPM',blank=True,null=True,default=0)
    latestPM = models.DateField(verbose_name='latestPM',blank=True,null=True)
    periodOfPM = models.DateField(verbose_name='periodOfPM',blank=True,null=True,default=timezone.now)

    #typeOfMaintenance
    typeOfMaintenance = models.CharField(verbose_name='typeOfMaintenance',max_length=50,blank=True,null=True)
    
    #Probability of failure
    constructionPeriod = models.DateField(verbose_name='constructionPeriod', blank=True,null=True,default=timezone.now)
    nextEventDate = models.DateField(verbose_name='nextEventDate',blank=True,null=True)
    situation = models.CharField(verbose_name='situation', max_length=200,blank=True,null=True)

    #period of task
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


    #PM03
    #taskOfPM03 = models.CharField(verbose_name='taskOfPM03', max_length=200,blank=True,null=True)
    #laborCostOfPM03 = models.DecimalField(verbose_name='laborCostOfPM03',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    #countOfPM03 = models.PositiveSmallIntegerField(verbose_name='countOfPM03',blank=True,null=True,default=0)
    #latestPM03 = models.DateField(verbose_name='latestPM03', max_length=200,blank=True,null=True,blank=True,null=True) 
    #periodOfPM03 = models.DateField(verbose_name='periodOfPM03',blank=True,null=True,default=timezone.now)#分析用で事後でデータ入力

    # PM04
    #taskOfPM04 = models.CharField(verbose_name='taskOfPM04', max_length=200,blank=True,null=True)
    #laborCostOfPM04 = models.DecimalField(verbose_name='laborCostOfPM04',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    #countOfPM04 = models.PositiveSmallIntegerField(verbose_name='countOfPM04',blank=True,null=True,default=0)
    #latestPM04 = models.DateField(verbose_name='latestPM04', max_length=200,blank=True,null=True,blank=True,null=True)
    #periodOfPM04 = models.DateField(verbose_name='periodOfPM04',blank=True,null=True,default=timezone.now)#分析用で事後でデータ入力

    # PM005
    #taskOfPM05 = models.CharField(verbose_name='taskOfPM045', max_length=200,blank=True,null=True)
    #laborCostOfPM05 = models.DecimalField(verbose_name='laborCostOfPM05',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    #countOfPM05 = models.PositiveSmallIntegerField(verbose_name='countOfPM05', blank=True,null=True,default=0,)
    #latestPM05 = models.DateField(verbose_name='latestPM05', blank=True,null=True)
    #periodOfPM05 = models.DateField(verbose_name='periodOfPM05',blank=True,null=True,default=timezone.now)#分析用で事後でデータ入力

    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task List'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return self.taskName
