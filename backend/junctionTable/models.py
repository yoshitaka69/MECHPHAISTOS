from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import choice
from django.conf import settings





#----------------------------------------------------------------------------------------------------------------------------------------------



from django.db import models
from django.db.models import Max
from accounts.models import CompanyCode, CompanyName, Plant
from ceList.models import Equipment, CeList, Machine
from spareParts.models import BomList
from taskList.models import TaskListPPM02, TaskListPPM03, TaskListAPM04, TaskListPPM05, TypicalTaskList, TaskList

class MasterDataTable(models.Model):

    # accountsから取得
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='masterDataTable_companyCode', null=True, blank=True)
    companyName = models.CharField(verbose_name='companyName', max_length=200, blank=True, null=True)
    plant = models.CharField(verbose_name='plant', max_length=200, blank=True, null=True)

    # Celist
    ceListNo = models.CharField(verbose_name='ceListNo', max_length=200, blank=True, null=True, unique=True)
    equipment = models.CharField(verbose_name='equipment', max_length=200, blank=True, null=True)
    machineName = models.CharField(verbose_name='machineName', max_length=200, blank=True, null=True)

    # TaskList
    taskPM02 = models.CharField(verbose_name='taskPM02', max_length=200, blank=True, null=True)
    countOfPM02 = models.IntegerField(verbose_name='countOfPM02', blank=True, null=True, default=0)
    latestPM02 = models.DateField(verbose_name='latestPM02', blank=True, null=True)
    laborCostOfPM02 = models.DecimalField(verbose_name='laborCostOfPM02', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)

    taskPM03 = models.CharField(verbose_name='taskPM03', max_length=200, blank=True, null=True)
    countOfPM03 = models.IntegerField(verbose_name='countOfPM03', blank=True, null=True, default=0)
    latestPM03 = models.DateField(verbose_name='latestPM03', blank=True, null=True)
    laborCostOfPM03 = models.DecimalField(verbose_name='laborCostOfPM03', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)

    taskPM04 = models.CharField(verbose_name='taskPM04', max_length=200, blank=True, null=True)
    countOfPM04 = models.IntegerField(verbose_name='countOfPM04', blank=True, null=True, default=0)
    latestPM04 = models.DateField(verbose_name='latestPM04', blank=True, null=True)
    laborCostOfPM04 = models.DecimalField(verbose_name='laborCostOfPM04', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)

    taskPM05 = models.CharField(verbose_name='taskPM05', max_length=200, blank=True, null=True)
    countOfPM05 = models.IntegerField(verbose_name='countOfPM05', blank=True, null=True, default=0)
    latestPM05 = models.DateField(verbose_name='latestPM05', blank=True, null=True)
    laborCostOfPM05 = models.DecimalField(verbose_name='laborCostOfPM05', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)

    # TypicalTaskList
    typicalTaskName = models.CharField(verbose_name='typicalTaskName', max_length=200, blank=True, null=True)
    typicalConstPeriod = models.CharField(verbose_name='typicalConstPeriod', max_length=200, blank=True, null=True)
    typicalTaskCost = models.DecimalField(verbose_name='typicalTaskCost', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    typicalNextEventDate = models.DateField(verbose_name='typicalNextEventDate', blank=True, null=True)
    typicalSituation = models.CharField(verbose_name='typicalSituation', max_length=200, blank=True, null=True)
    multiTask = models.BooleanField(verbose_name='multiTask', default=False, blank=True)

    # BomList
    bomCode = models.CharField(verbose_name='bomCode', max_length=200, blank=True, null=True)
    bomCost = models.DecimalField(verbose_name='bomCost', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    bomStock = models.CharField(verbose_name='bomStock', max_length=200, blank=True, null=True)
    maxPartsDeliveryTimeInBom = models.IntegerField(verbose_name='maxPartsDeliveryTimeInBom', blank=True, null=True, default=0)

    # 将来的にcalかここで計算させる。
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)

    # Impact
    levelSetValue = models.CharField(verbose_name='levelSetValue', max_length=200, null=True, blank=True)
    mttr = models.PositiveSmallIntegerField(verbose_name='mttr', blank=True, null=True, default=0)
    possibilityOfContinuousProduction = models.CharField(verbose_name='possibilityOfContinuousProduction', max_length=200, null=True, blank=True)

    # Critical Equipment Level
    impactForProduction = models.CharField(verbose_name='impactForProduction', max_length=200, blank=True, null=True)
    probabilityOfFailure = models.CharField(verbose_name='probabilityOfFailure', max_length=200, blank=True, null=True)
    assessment = models.CharField(verbose_name='assessment', max_length=20, blank=True, null=True)

    # Status of measures
    rcaOrReplace = models.BooleanField(verbose_name='rcaOrReplace', default=False, null=True, blank=True)
    sparePartsOrAlternative = models.BooleanField(verbose_name='sparePartsOrAlternative', default=False, null=True, blank=True)
    coveredFromTask = models.BooleanField(verbose_name='coveredFromTask', default=False, null=True, blank=True)
    twoways = models.BooleanField(verbose_name='twoways', default=False, null=True, blank=True)
    ceDescription = models.TextField(verbose_name='ceDescription', blank=True, null=True, max_length=1000)

    # period of task
    thisYear10ago = models.BooleanField(verbose_name='thisYear10ago', default=False)
    thisYear9ago = models.BooleanField(verbose_name='thisYear9ago', default=False)
    thisYear8ago = models.BooleanField(verbose_name='thisYear8ago', default=False)
    thisYear7ago = models.BooleanField(verbose_name='thisYear7ago', default=False)
    thisYear6ago = models.BooleanField(verbose_name='thisYear6ago', default=False)
    thisYear5ago = models.BooleanField(verbose_name='thisYear5ago', default=False)
    thisYear4ago = models.BooleanField(verbose_name='thisYear4ago', default=False)
    thisYear3ago = models.BooleanField(verbose_name='thisYear3ago', default=False)
    thisYear2ago = models.BooleanField(verbose_name='thisYear2ago', default=False)
    thisYear1ago = models.BooleanField(verbose_name='thisYear1ago', default=False)
    thisYear = models.BooleanField(verbose_name='thisYear', default=False)
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

    class Meta:
        verbose_name = 'Master Data Table'
        verbose_name_plural = 'Master Data Table'
        ordering = ('ceListNo',)  # モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
        unique_together = ('companyCode', 'ceListNo')  # companyCodeとceListNoの組み合わせがユニークであることを示す。

    def save(self, *args, **kwargs):
        if not self.ceListNo:  # ceListNoが指定されていない場合、自動生成
            max_ce_list_no = MasterDataTable.objects.aggregate(Max('ceListNo'))['ceListNo__max']
            if max_ce_list_no:
                self.ceListNo = str(int(max_ce_list_no) + 1).zfill(5)  # 5桁のゼロ埋めで次の番号を設定
            else:
                self.ceListNo = '00001'  # 最初のレコードの場合、'00001'から開始
        super(MasterDataTable, self).save(*args, **kwargs)

    def __str__(self):
        return str('Master Data Table')






#----------------------------------------------------------------------------------------------------------------------------------------------











class BomAndTask(models.Model):
    
#accountsから取得
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='bomAndTask_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='bomAndTask_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='bomAndTask_plant',null=True, blank=True)

    bomCode = models.ForeignKey(BomList, on_delete=models.CASCADE, related_name='bomAndTask_bomCode',null=True, blank=True)
    taskCode = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='bomAndTask_taskCode',null=True, blank=True)
    
    bomAndTaskSet = models.CharField(verbose_name='bomAndTaskSet',blank=True,null=True,max_length=100)
    bomAndTaskSetCost = models.DecimalField(verbose_name='bomAndTaskSetCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    

    class Meta:
        verbose_name = 'BomAndTask'
        verbose_name_plural = 'BomAndTask'
        ordering = ('bomCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    

    def __str__(self):
        return str('BomAndTask')




#----------------------------------------------------------------------------------------------------------------------------------------------


class CeListAndTask(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='ceListAndTask_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='ceListAndTask_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='ceListAndTask_plant',null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='ceListAndTask_equipment',null=True, blank=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='ceListAndTask_machine',null=True, blank=True)
    
    no1HighLevelMachine = models.CharField(verbose_name='no1HighLevelMachine',blank=True,null=True,max_length=100)
    no1HighPriorityTaskName = models.CharField(verbose_name='no1HighPriorityTaskName',blank=True,null=True,max_length=100)

    no2HighLevelMachine = models.CharField(verbose_name='no2HighLevelMachine',blank=True,null=True,max_length=100)
    no2HighPriorityTaskName = models.CharField(verbose_name='no2HighPriorityTaskName',blank=True,null=True,max_length=100)

    no3HighLevelMachine = models.CharField(verbose_name='no3HighLevelMachine',blank=True,null=True,max_length=100)
    no3HighPriorityTaskName = models.CharField(verbose_name='no3HighPriorityTaskName',blank=True,null=True,max_length=100)

    no4HighLevelMachine = models.CharField(verbose_name='no4HighLevelMachine',blank=True,null=True,max_length=100)
    no4HighPriorityTaskName = models.CharField(verbose_name='no4HighPriorityTaskName',blank=True,null=True,max_length=100)

    no5HighLevelMachine = models.CharField(verbose_name='no5HighLevelMachine',blank=True,null=True,max_length=100)
    no5HighPriorityTaskName = models.CharField(verbose_name='no5HighPriorityTaskName',blank=True,null=True,max_length=100)

    no6HighLevelMachine = models.CharField(verbose_name='no6HighLevelMachine',blank=True,null=True,max_length=100)
    no6HighPriorityTaskName = models.CharField(verbose_name='no6HighPriorityTaskName',blank=True,null=True,max_length=100)

    no7HighLevelMachine = models.CharField(verbose_name='no7HighLevelMachine',blank=True,null=True,max_length=100)
    no7HighPriorityTaskName = models.CharField(verbose_name='no7HighPriorityTaskName',blank=True,null=True,max_length=100)

    no8HighLevelMachine = models.CharField(verbose_name='no8HighLevelMachine',blank=True,null=True,max_length=100)
    no8HighPriorityTaskName = models.CharField(verbose_name='no8HighPriorityTaskName',blank=True,null=True,max_length=100)

    no9HighLevelMachine = models.CharField(verbose_name='no9HighLevelMachine',blank=True,null=True,max_length=100)
    no9HighPriorityTaskName = models.CharField(verbose_name='no9HighPriorityTaskName',blank=True,null=True,max_length=100)

    no10HighLevelMachine = models.CharField(verbose_name='no10HighLevelMachine',blank=True,null=True,max_length=100)
    no10HighPriorityTaskName = models.CharField(verbose_name='no10HighPriorityTaskName',blank=True,null=True,max_length=100)

    no11HighLevelMachine = models.CharField(verbose_name='no11HighLevelMachine',blank=True,null=True,max_length=100)
    no11HighPriorityTaskName = models.CharField(verbose_name='no11HighPriorityTaskName',blank=True,null=True,max_length=100)

    no12HighLevelMachine = models.CharField(verbose_name='no12HighLevelMachine',blank=True,null=True,max_length=100)
    no12HighPriorityTaskName = models.CharField(verbose_name='no12HighPriorityTaskName',blank=True,null=True,max_length=100)

    no13HighLevelMachine = models.CharField(verbose_name='no13HighLevelMachine',blank=True,null=True,max_length=100)
    no13HighPriorityTaskName = models.CharField(verbose_name='no13HighPriorityTaskName',blank=True,null=True,max_length=100)

    no14HighLevelMachine = models.CharField(verbose_name='no14HighLevelMachine',blank=True,null=True,max_length=100)
    no14HighPriorityTaskName = models.CharField(verbose_name='no14HighPriorityTaskName',blank=True,null=True,max_length=100)

    no15HighLevelMachine = models.CharField(verbose_name='no15HighLevelMachine',blank=True,null=True,max_length=100)
    no15HighPriorityTaskName = models.CharField(verbose_name='no15HighPriorityTaskName',blank=True,null=True,max_length=100)

    no16HighLevelMachine = models.CharField(verbose_name='no16HighLevelMachine',blank=True,null=True,max_length=100)
    no16HighPriorityTaskName = models.CharField(verbose_name='no16HighPriorityTaskName',blank=True,null=True,max_length=100)

    no17HighLevelMachine = models.CharField(verbose_name='no17HighLevelMachine',blank=True,null=True,max_length=100)
    no17HighPriorityTaskName = models.CharField(verbose_name='no17HighPriorityTaskName',blank=True,null=True,max_length=100)

    no18HighLevelMachine = models.CharField(verbose_name='no18HighLevelMachine',blank=True,null=True,max_length=100)
    no18HighPriorityTaskName = models.CharField(verbose_name='no18HighPriorityTaskName',blank=True,null=True,max_length=100)

    no19HighLevelMachine = models.CharField(verbose_name='no19HighLevelMachine',blank=True,null=True,max_length=100)
    no19HighPriorityTaskName = models.CharField(verbose_name='no19HighPriorityTaskName',blank=True,null=True,max_length=100)

    no20HighLevelMachine = models.CharField(verbose_name='no20HighLevelMachine',blank=True,null=True,max_length=100)
    no20HighPriorityTaskName = models.CharField(verbose_name='no20HighPriorityTaskName',blank=True,null=True,max_length=100)


    class Meta:
        verbose_name = 'CeList And Task'
        verbose_name_plural = 'CeList And Task'
        ordering = ('companyCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    

    def __str__(self):
        return str('CeList And Task')
    
 
# assessment の優先度を定義
ASSESSMENT_PRIORITY = {
    "Very High": 5,
    "High": 4,
    "Middle": 3,
    "Low": 2,
    "Very Low": 1
}

@receiver(post_save, sender=MasterDataTable)
def update_ceListAndTask(sender, instance, **kwargs):
    if settings.DEBUG:
        print(f"MasterDataTable instance saved: {instance}")

    # assessment が "Very High", "High", "Middle", "Low", "Very Low" のエントリを抽出し、優先度の高い順にソート
    assessment_entries = MasterDataTable.objects.filter(
        assessment__in=ASSESSMENT_PRIORITY.keys()
    ).order_by('-assessment')

    if not assessment_entries.exists():
        if settings.DEBUG:
            print("No relevant assessment entries found for companyCode: ", instance.companyCode)
        return

    # CeListAndTaskの対応するインスタンスを取得または作成
    ce_list_and_task, created = CeListAndTask.objects.get_or_create(companyCode=instance.companyCode)
    
    # 優先度の高い順に各マシンとタスクを設定
    for idx, entry in enumerate(assessment_entries[:20], 1):  # 最初の20エントリのみを取得
        machine_name = entry.machineName.machineName  # Machine インスタンスから machineName 属性を取得
        task_name = entry.typicalTaskName.typicalTaskName if entry.typicalTaskName else "No Task"  # None チェックを追加
        setattr(ce_list_and_task, f'no{idx}HighLevelMachine', machine_name)
        setattr(ce_list_and_task, f'no{idx}HighPriorityTaskName', task_name)
        
        if settings.DEBUG:
            print(f'Set no{idx}HighLevelMachine to {machine_name}')
            print(f'Set no{idx}HighPriorityTaskName to {task_name}')

    ce_list_and_task.save()

    if settings.DEBUG:
        print("CeListAndTask instance updated with new machine and task names.")





#----------------------------------------------------------------------------------------------------------------------------------------------



class BadActorManagement(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='badActorManagement_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='badActorManagement_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='badActorManagement_plant',null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='badActorManagement_equipment',null=True, blank=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='badActorManagement_machine',null=True, blank=True)

    badActor = models.CharField(verbose_name='badActor',blank=True,null=True,max_length=100)


    class Meta:
        verbose_name = 'Bad Actor Management'
        verbose_name_plural = 'Bad Actor Management'
        ordering = ('companyCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    

    def __str__(self):
        return str('Bad Actor Management')




class EventYearPPM(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='eventYearPPM_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='eventYearPPM_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='eventYearPPM_plant',null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='eventYearPPM_equipment',null=True, blank=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='eventYearPPM_machine',null=True, blank=True)


    PPM10YearCostAgo = models.DecimalField(verbose_name='PPM10YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM9YearCostAgo = models.DecimalField(verbose_name='PPM9YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)  
    PPM8YearCostAgo = models.DecimalField(verbose_name='PPM8YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00) 
    PPM7YearCostAgo = models.DecimalField(verbose_name='PPM7YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)  
    PPM6YearCostAgo = models.DecimalField(verbose_name='PPM6YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM5YearCostAgo = models.DecimalField(verbose_name='PPM5YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM4YearCostAgo = models.DecimalField(verbose_name='PPM4YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)  
    PPM3YearCostAgo = models.DecimalField(verbose_name='PPM3YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00) 
    PPM2YearCostAgo = models.DecimalField(verbose_name='PPM2YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)  
    PPM1YearCostAgo = models.DecimalField(verbose_name='PPM1YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM0YearCost = models.DecimalField(verbose_name='PPM0YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM1YearCost = models.DecimalField(verbose_name='PPM1YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM2YearCost = models.DecimalField(verbose_name='PPM2YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM3YearCost = models.DecimalField(verbose_name='PPM3YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM4YearCost = models.DecimalField(verbose_name='PPM4YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM5YearCost = models.DecimalField(verbose_name='PPM5YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM6YearCost = models.DecimalField(verbose_name='PPM6YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM7YearCost = models.DecimalField(verbose_name='PPM7YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM8YearCost = models.DecimalField(verbose_name='PPM8YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM9YearCost = models.DecimalField(verbose_name='PPM9YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    PPM10YearCost = models.DecimalField(verbose_name='PPM10YearCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)

    class Meta:
        verbose_name = 'Event Year PPM'
        verbose_name_plural = 'Event Year PPM'
        ordering = ('companyCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    

    def __str__(self):
        return str('Event Year PPM')


class GapOfRepairingCost(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='gapOfRepairingCost_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='gapOfRepairingCost_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='gapOfRepairingCost_plant',null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='gapOfRepairingCost_equipment',null=True, blank=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='gapOfRepairingCost_machine',null=True, blank=True)


    GapCostPPM10Ago = models.DecimalField(verbose_name='PPM10YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM9Ago  = models.DecimalField(verbose_name='PPM9YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)  
    GapCostPPM8Ago  = models.DecimalField(verbose_name='PPM8YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00) 
    GapCostPPM7Ago  = models.DecimalField(verbose_name='PPM7YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)  
    GapCostPPM6Ago  = models.DecimalField(verbose_name='PPM6YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM5Ago  = models.DecimalField(verbose_name='PPM5YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM4Ago  = models.DecimalField(verbose_name='PPM4YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)  
    GapCostPPM3Ago = models.DecimalField(verbose_name='PPM3YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00) 
    GapCostPPM2Ago  = models.DecimalField(verbose_name='PPM2YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)  
    GapCostPPM1Ago  = models.DecimalField(verbose_name='PPM1YearCostAgo',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM0 = models.DecimalField(verbose_name='GapCostPPM0',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM1 = models.DecimalField(verbose_name='GapCostPPM1',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM2 = models.DecimalField(verbose_name='GapCostPPM2',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM3 = models.DecimalField(verbose_name='GapCostPPM3',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM4 = models.DecimalField(verbose_name='GapCostPPM4',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM5 = models.DecimalField(verbose_name='GapCostPPM5',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM6 = models.DecimalField(verbose_name='GapCostPPM6',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM7 = models.DecimalField(verbose_name='GapCostPPM7',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM8 = models.DecimalField(verbose_name='GapCostPPM8',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM9 = models.DecimalField(verbose_name='GapCostPPM9',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    GapCostPPM10 = models.DecimalField(verbose_name='GapCostPPM10',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)

    class Meta:
        verbose_name = 'GapOfRepairingCost'
        verbose_name_plural = 'GapOfRepairingCost'
        ordering = ('companyCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    

    def __str__(self):
        return str('GapOfRepairingCost')
    




#----------------------------------------------------------------------------------------------------------------------------------------------

# models.py
from django.db import models

class ScheduleForGantt(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='scheduleForGantt_companyCode', null=True, blank=True)
    name = models.CharField(max_length=100)
    pmType = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return self.name

    





#scheduleForCalendarモデル
#----------------------------------------------------------------------------------------------------------------------------------------------
#このモデルはsignals.pyを持っています。workOrderモデルからの保存処理に対応してますので、注意してください。
#----------------------------------------------------------------------------------------------------------------------------------------------
    
from django.db import models

class ScheduleForCalendar(models.Model):
    eventDataNo = models.IntegerField(null=True, blank=True)  
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='scheduleForCalendar_companyCode', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='eventTitle')  # イベントのタイトル

    eventType = models.CharField(
        max_length=50,
        choices=[
            ('work order', 'Work Order'),
            ('daily report', 'Daily Report'),
            ('task', 'Task'),
            ('failure date', 'Failure Date')
        ],
        verbose_name='eventType',
        null=True, blank=True
    )

    startDatetime = models.DateTimeField(verbose_name='startDate&Time')  # イベントの開始日時
    endDatetime = models.DateTimeField(verbose_name='endDate&Time')  # イベントの終了日時
    description = models.TextField(blank=True, null=True, verbose_name='eventDescription')  # イベントの説明（オプション）

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['startDatetime']

