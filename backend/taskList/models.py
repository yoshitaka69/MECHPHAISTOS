from django.db import models
from accounts.models import CompanyCode,CompanyName,Plant
from ceList.models import Equipment,Machine
from spareParts.models import BomList


class TaskListPM02(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListPM02_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListPM02_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListPM02_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListPM02_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCode',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskName',max_length=200,blank=True,null=True)
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
        verbose_name = 'Task List Pm02'
        verbose_name_plural = 'Task List Pm02'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'



class TaskListPM03(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListPM03_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListPM03_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListPM03_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListPM03_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCode',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskName',max_length=200,blank=True,null=True)
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
        verbose_name = 'Task List Pm03'
        verbose_name_plural = 'Task List Pm03'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'





class TaskListPM04(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListPM04_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListPM4_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListPM04_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListPM04_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListPM04_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCode',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskName',max_length=200,blank=True,null=True)
    laborCostOfPM = models.DecimalField(verbose_name='laborCostOfPM',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    countOfPM = models.PositiveSmallIntegerField(verbose_name='countOfPM',blank=True,null=True,default=0)
    latestPM = models.DateField(verbose_name='latestPM',blank=True,null=True)
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriod', blank=True, null=True)

    class Meta:
        verbose_name = 'Task List Pm04'
        verbose_name_plural = 'Task List Pm04'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'



class TaskListPM05(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListPM05_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListPM05_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListPM05_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListPM05_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCode',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskName',max_length=200,blank=True,null=True)
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
        verbose_name = 'Task List Pm05'
        verbose_name_plural = 'Task List Pm05'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'
    


class TypicalTaskList(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='typicalTaskList_companyCode',null=True, blank=True)
    taskCode = models.CharField(verbose_name='taskCode', max_length=100,blank=True,null=True)
    typicalTaskName = models.CharField(verbose_name='typicalTaskName', max_length=200,blank=True,null=True)
    typicalTaskCost = models.DecimalField(verbose_name='typicalTaskCost',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    typicalLatestDate = models.DateField(verbose_name='typicalLatestDate',blank=True,null=True)
    typicalConstPeriod = models.IntegerField(verbose_name='typicalConstPeriod', blank=True, null=True)
    typicalNextEventDate = models.DateField(verbose_name='typicalNextEventDate',blank=True,null=True)
    multiTasking = models.BooleanField(verbose_name='multiTasking',default=False)
    
    class Meta:
        verbose_name = 'Typical Task List'
        verbose_name_plural = 'Typical Task List'
        ordering = ('taskCode',) 
        
    def __str__(self):
        return str('TypicalTaskList')


class TaskList(models.Model):
    
    #accounts
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskList_companyCode',null=True, blank=True)

    #CeList
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskList_plant', null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskList_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskList_equipment',null=True, blank=True)

    #Typical Task 
    taskListNo = models.CharField(verbose_name='taskListNo', max_length=100,blank=True,null=True)

    typicalLatestDate = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='taskList_typicalLatestDate',null=True, blank=True)
    typicalTaskName = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='taskList_typicalTaskName',null=True, blank=True)
    typicalTaskCost = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='taskList_typicalTaskCost',null=True, blank=True)
    typicalConstPeriod = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='taskList_typicalConstPeriod',null=True, blank=True)
    multiTasking = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='taskList_multiTasking',null=True, blank=True)
    typicalNextEventDate = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='taskList_typicalNextEventDate',null=True, blank=True)
    typicalSituation = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='taskList_typicalSituation',null=True, blank=True)

    #bomCode
    bomCode =  models.ForeignKey(BomList, on_delete=models.CASCADE, related_name='taskList_bomCode',null=True, blank=True)
    bomCost = models.ForeignKey(BomList, on_delete=models.CASCADE, related_name='taskList_bomCost',null=True, blank=True)

    totalCost  = models.DecimalField(verbose_name='totalCost',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)

    #あとで下はmethodFieldに変更する。
    thisYear = models.BooleanField(verbose_name='thisYear',default=False)
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
        ordering = ('companyCode',) 
         

    def __str__(self):
        return str('Task List')


