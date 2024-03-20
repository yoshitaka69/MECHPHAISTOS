from django.db import models
from accounts.models import CompanyCode,CompanyName,Plant
from ceList.models import Equipment,CeList



class TaskList(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskList_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskList_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskList_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskList_equipment',null=True, blank=True)
    machineName = models.ForeignKey(CeList, on_delete=models.CASCADE, related_name='taskList_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCode',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskName',max_length=200,blank=True,null=True)
    typeOfPM = models.CharField(verbose_name='typeOfPM',max_length=200,blank=True,null=True)
    laborCostOfPM = models.DecimalField(verbose_name='laborCostOfPM',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    countOfPM = models.PositiveSmallIntegerField(verbose_name='countOfPM',blank=True,null=True,default=0)
    latestPM = models.DateField(verbose_name='latestPM',blank=True,null=True)
    periodOfPM = models.IntegerField(verbose_name='periodOfPM', blank=True, null=True)  # 整数フィールドに変更
    

    #Probability of failure
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriod', blank=True, null=True)  # 整数フィールドに変更
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
    thisYear = models.CharField(verbose_name='thisYear', max_length=200,blank=True,null=True)
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


    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task List'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'
