from django.db import models
from accounts.models import CompanyCode,CompanyName,Plant
from ceList.models import Equipment,Machine
from spareParts.models import BomList


#PlannedなのかActualなのかを比較する必要があり。


#TaskList PlannedPM02
class TaskListPPM02(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListPPM02_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListPPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListPPM02_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListPPM02_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListPPM02_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCodePPM02',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskNamePPM2',max_length=200,blank=True,null=True)
    laborCostOfPPM02 = models.DecimalField(verbose_name='laborCostOfPPM02',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    countOfPPM02 = models.PositiveSmallIntegerField(verbose_name='countOfPPM02',blank=True,null=True,default=0)
    latestPPM02 = models.DateField(verbose_name='latestPPM02',blank=True,null=True)
    periodOfPPM02 = models.IntegerField(verbose_name='periodOfPPM02', blank=True, null=True)  # 整数フィールドに変更
    
    #Probability of failure
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriodPPM02', blank=True, null=True)  # 整数フィールドに変更
    nextEventDate = models.DateField(verbose_name='nextEventDatePPM02',blank=True,null=True)
    situation = models.CharField(verbose_name='situationPPM02', max_length=200,blank=True,null=True)

    #period of task
    thisYear10ago = models.BooleanField(verbose_name='thisYear10agoPPm02',default=False)
    thisYear9ago = models.BooleanField(verbose_name='thisYear9agoPPM02',default=False)
    thisYear8ago = models.BooleanField(verbose_name='thisYear8agoPPM02',default=False)
    thisYear7ago = models.BooleanField(verbose_name='thisYear7agoPPM02',default=False)
    thisYear6ago = models.BooleanField(verbose_name='thisYear6agoPPM02',default=False)
    thisYear5ago = models.BooleanField(verbose_name='thisYear5agoPPM02',default=False)
    thisYear4ago = models.BooleanField(verbose_name='thisYear4agoPPM02',default=False)
    thisYear3ago = models.BooleanField(verbose_name='thisYear3agoPPM02',default=False)
    thisYear2ago = models.BooleanField(verbose_name='thisYear2agoPPM02',default=False)
    thisYear1ago = models.BooleanField(verbose_name='thisYear1agoPPM02',default=False)
    thisYear = models.BooleanField(verbose_name='thisYearPPM02',default=False)
    thisYear1later = models.BooleanField(verbose_name='thisYear1laterPPM02',default=False)
    thisYear2later = models.BooleanField(verbose_name='thisYear2laterPPM02',default=False)
    thisYear3later = models.BooleanField(verbose_name='thisYear3laterPPM02',default=False)
    thisYear4later = models.BooleanField(verbose_name='thisYear4laterPPM02',default=False)
    thisYear5later = models.BooleanField(verbose_name='thisYear5laterPPM02',default=False)
    thisYear6later = models.BooleanField(verbose_name='thisYear6laterPPM02',default=False)
    thisYear7later = models.BooleanField(verbose_name='thisYear7laterPPM02',default=False)
    thisYear8later = models.BooleanField(verbose_name='thisYear8laterPPM02',default=False)
    thisYear9later = models.BooleanField(verbose_name='thisYear9laterPPM02',default=False)
    thisYear10later = models.BooleanField(verbose_name='thisYear10laterPPM02',default=False)


    class Meta:
        verbose_name = 'Task List PPm02'
        verbose_name_plural = 'Task List PPm02'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'




#TaskListActualPM02
class TaskListAPM02(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListAPM02_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListAPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListAPM02_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListAPM02_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListAPM02_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCodeAPM02',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskNameAPM02',max_length=200,blank=True,null=True)
    laborCostOfAPM02 = models.DecimalField(verbose_name='laborCostOfAPM02',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    startDateAPM02 = models.DateField(verbose_name='startDateAPM02',blank=True,null=True)
    endDateAPM02 =models.DateField(verbose_name='endDateAPM02',blank=True,null=True)
    
    #Probability of failure
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriodAPM02', blank=True, null=True)  # 整数フィールドに変更

    #description
    description = models.TextField(verbose_name='descriptionAPM02',max_length=1000,blank=True,null=True,)


    class Meta:
        verbose_name = 'Task List APm02'
        verbose_name_plural = 'Task List APm02'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'









class TaskListPPM03(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListPPM03_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListPPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListPPM03_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListPPM03_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListPPM03_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCodePPM03',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskNamePPM03',max_length=200,blank=True,null=True)
    laborCostOfPPM03 = models.DecimalField(verbose_name='laborCostOfPPM03',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    countOfPPM03 = models.PositiveSmallIntegerField(verbose_name='countOfPPM03',blank=True,null=True,default=0)
    latestPPM03 = models.DateField(verbose_name='latestPPM03',blank=True,null=True)
    periodOfPPM03 = models.IntegerField(verbose_name='periodOfPPM03', blank=True, null=True)  # 整数フィールドに変更
    
    #Probability of failure
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriodPPM03', blank=True, null=True)  # 整数フィールドに変更
    nextEventDate = models.DateField(verbose_name='nextEventDatePPM03',blank=True,null=True)
    situation = models.CharField(verbose_name='situationPPM03', max_length=200,blank=True,null=True)

    #period of task
    thisYear10ago = models.BooleanField(verbose_name='thisYear10agoPPM03',default=False)
    thisYear9ago = models.BooleanField(verbose_name='thisYear9agoPPM03',default=False)
    thisYear8ago = models.BooleanField(verbose_name='thisYear8agoPPM03',default=False)
    thisYear7ago = models.BooleanField(verbose_name='thisYear7agoPPM03',default=False)
    thisYear6ago = models.BooleanField(verbose_name='thisYear6agoPPM03',default=False)
    thisYear5ago = models.BooleanField(verbose_name='thisYear5agoPPM03',default=False)
    thisYear4ago = models.BooleanField(verbose_name='thisYear4agoPPM03',default=False)
    thisYear3ago = models.BooleanField(verbose_name='thisYear3agoPPM03',default=False)
    thisYear2ago = models.BooleanField(verbose_name='thisYear2agoPPM03',default=False)
    thisYear1ago = models.BooleanField(verbose_name='thisYear1agoPPM03',default=False)
    thisYear = models.BooleanField(verbose_name='thisYearPPM03',default=False)
    thisYear1later = models.BooleanField(verbose_name='thisYear1laterPPM03',default=False)
    thisYear2later = models.BooleanField(verbose_name='thisYear2laterPPM03',default=False)
    thisYear3later = models.BooleanField(verbose_name='thisYear3laterPPM03',default=False)
    thisYear4later = models.BooleanField(verbose_name='thisYear4laterPPM03',default=False)
    thisYear5later = models.BooleanField(verbose_name='thisYear5laterPPM03',default=False)
    thisYear6later = models.BooleanField(verbose_name='thisYear6laterPPM03',default=False)
    thisYear7later = models.BooleanField(verbose_name='thisYear7laterPPM03',default=False)
    thisYear8later = models.BooleanField(verbose_name='thisYear8laterPPM03',default=False)
    thisYear9later = models.BooleanField(verbose_name='thisYear9laterPPM03',default=False)
    thisYear10later = models.BooleanField(verbose_name='thisYear10laterPPM03',default=False)


    class Meta:
        verbose_name = 'Task List PPm03'
        verbose_name_plural = 'Task List PPm03'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'




#TaskListActualPM03
class TaskListAPM03(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListAPM03_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListAPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListAPM03_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListAPM03_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListAPM03_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCodeAPM03',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskNameAPM03',max_length=200,blank=True,null=True)
    laborCostOfAPM03 = models.DecimalField(verbose_name='laborCostOfAPM03',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    startDateAPM03 = models.DateField(verbose_name='startDateAPM03',blank=True,null=True)
    endDateAPM03 =models.DateField(verbose_name='endDateAPM03',blank=True,null=True)
    
    #Probability of failure
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriodAPM03', blank=True, null=True)  # 整数フィールドに変更

    #description
    description = models.TextField(verbose_name='descriptionAPM03',max_length=1000,blank=True,null=True,)


    class Meta:
        verbose_name = 'Task List APm03'
        verbose_name_plural = 'Task List APm03'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'










class TaskListAPM04(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListAPM04_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListAPM4_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListAPM04_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListAPM04_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListAPM04_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCodeAPM04',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskNameAPM04',max_length=200,blank=True,null=True)
    laborCostOfAPM04 = models.DecimalField(verbose_name='laborCostOfAPM04',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    countOfAPM04 = models.PositiveSmallIntegerField(verbose_name='countOfAPM04',blank=True,null=True,default=0)
    latestAPM04 = models.DateField(verbose_name='latestAPM04',blank=True,null=True)
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriodAPM04', blank=True, null=True)

    class Meta:
        verbose_name = 'Task List APm04'
        verbose_name_plural = 'Task List APm04'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'





class TaskListPPM05(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListPPM05_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListPPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListPPM05_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListPPM05_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListPPM05_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCodePPM05',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskNamePPM05',max_length=200,blank=True,null=True)
    laborCostOfPPM05 = models.DecimalField(verbose_name='laborCostOfPPM05',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    countOfPPM05 = models.PositiveSmallIntegerField(verbose_name='countOfPPM05',blank=True,null=True,default=0)
    latestPPM05 = models.DateField(verbose_name='latestPPM05',blank=True,null=True)
    periodOfPPM05 = models.IntegerField(verbose_name='periodOfPPM05', blank=True, null=True)  # 整数フィールドに変更
    
    #Probability of failure
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriodPPM05', blank=True, null=True)  # 整数フィールドに変更
    nextEventDate = models.DateField(verbose_name='nextEventDatePPM05',blank=True,null=True)
    situation = models.CharField(verbose_name='situationPPM05', max_length=200,blank=True,null=True)

    #period of task
    thisYear10ago = models.BooleanField(verbose_name='thisYear10agoPPM05',default=False)
    thisYear9ago = models.BooleanField(verbose_name='thisYear9agoPPM05',default=False)
    thisYear8ago = models.BooleanField(verbose_name='thisYear8agoPPM05',default=False)
    thisYear7ago = models.BooleanField(verbose_name='thisYear7agoPPM05',default=False)
    thisYear6ago = models.BooleanField(verbose_name='thisYear6agoPPM05',default=False)
    thisYear5ago = models.BooleanField(verbose_name='thisYear5agoPPM05',default=False)
    thisYear4ago = models.BooleanField(verbose_name='thisYear4agoPPM05',default=False)
    thisYear3ago = models.BooleanField(verbose_name='thisYear3agoPPM05',default=False)
    thisYear2ago = models.BooleanField(verbose_name='thisYear2agoPPM05',default=False)
    thisYear1ago = models.BooleanField(verbose_name='thisYear1agoPPM05',default=False)
    thisYear = models.BooleanField(verbose_name='thisYearPPM5',default=False)
    thisYear1later = models.BooleanField(verbose_name='thisYear1laterPPM05',default=False)
    thisYear2later = models.BooleanField(verbose_name='thisYear2laterPPM05',default=False)
    thisYear3later = models.BooleanField(verbose_name='thisYear3laterPPM05',default=False)
    thisYear4later = models.BooleanField(verbose_name='thisYear4laterPPM05',default=False)
    thisYear5later = models.BooleanField(verbose_name='thisYear5laterPPM05',default=False)
    thisYear6later = models.BooleanField(verbose_name='thisYear6laterPPM05',default=False)
    thisYear7later = models.BooleanField(verbose_name='thisYear7laterPPM05',default=False)
    thisYear8later = models.BooleanField(verbose_name='thisYear8laterPPM05',default=False)
    thisYear9later = models.BooleanField(verbose_name='thisYear9laterPPM05',default=False)
    thisYear10later = models.BooleanField(verbose_name='thisYear10laterPPM05',default=False)


    class Meta:
        verbose_name = 'Task List PPm05'
        verbose_name_plural = 'Task List PPm05'
        ordering = ('taskCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

    def __str__(self):
            return f'{self.taskName}'
    



#TaskListActualAPM05
class TaskListAPM05(models.Model):

    #accountsより
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='taskListAPM05_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='taskListAPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='taskListAPM05_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='taskListAPM05_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='taskListAPM05_machineName',null=True, blank=True)

    taskCode = models.CharField(verbose_name='taskCodeAPM05',max_length=200,blank=True,null=True)
    taskName = models.CharField(verbose_name='taskNameAPM05',max_length=200,blank=True,null=True)
    laborCostOfAPM05 = models.DecimalField(verbose_name='laborCostOfAPM05',max_digits=10,decimal_places=5,blank=True,null=True,default=0.00)
    startDateAPM05 = models.DateField(verbose_name='startDateAPM05',blank=True,null=True)
    endDateAPM05 =models.DateField(verbose_name='endDateAPM05',blank=True,null=True)
    
    #Probability of failure
    constructionPeriod = models.IntegerField(verbose_name='constructionPeriodAPM05', blank=True, null=True)  # 整数フィールドに変更

    #description
    description = models.TextField(verbose_name='descriptionAPM05',max_length=1000,blank=True,null=True,)


    class Meta:
        verbose_name = 'Task List APm05'
        verbose_name_plural = 'Task List APm05'
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
    typicalSituation = models.CharField(verbose_name='typicalSituation', max_length=200,blank=True,null=True)
    
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


    def save(self, *args, **kwargs):
        if not self.taskListNo:
            # 最新のtaskListNoを取得し、1を加算して新しいtaskListNoを生成
            last_task = TaskList.objects.order_by('taskListNo').last()
            if last_task:
                self.taskListNo = f"{int(last_task.taskListNo) + 1:04d}"  # 例: '0005'
            else:
                self.taskListNo = '0001'
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task List'
        ordering = ('companyCode',) 
         

    def __str__(self):
        return str('Task List')


