from django.db import models
from django.utils import timezone
from datetime import timedelta
import decimal

from accounts.models import CompanyCode,CompanyName,Plant
from ceList.models import Equipment,CeList,Machine
from spareParts.models import BomList
from taskList.models import TaskListPPM02,TaskListPPM03,TaskListAPM04,TaskListPPM05,TypicalTaskList,TaskList


class MasterDataTable(models.Model):

    #accountsから取得
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='masterDataTable_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='masterDataTable_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='masterDataTable_plant',null=True, blank=True)

    #Celist
    ceListNo = models.ForeignKey(CeList, on_delete=models.CASCADE, related_name='masterDataTable_ceListNo',null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='masterDataTable_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='masterDataTable_machineName',null=True, blank=True)

    #TaskList
    taskPM02 = models.ForeignKey(TaskListPPM02, on_delete=models.CASCADE, related_name='masterDataTable_taskPM02',null=True, blank=True)
    countOfPM02 = models.ForeignKey(TaskListPPM02, on_delete=models.CASCADE, related_name='masterDataTable_countOfPM02',null=True, blank=True)
    latestPM02 = models.ForeignKey(TaskListPPM02, on_delete=models.CASCADE, related_name='masterDataTable_latestPM02',null=True, blank=True)
    laborCostOfPM02 = models.ForeignKey(TaskListPPM02, on_delete=models.CASCADE, related_name='masterDataTable_laborCostOfPM02',null=True, blank=True)

    taskPM03 = models.ForeignKey(TaskListPPM03, on_delete=models.CASCADE, related_name='masterDataTable_taskPM03',null=True, blank=True)
    countOfPM03 = models.ForeignKey(TaskListPPM03, on_delete=models.CASCADE, related_name='masterDataTable_countOfPM03',null=True, blank=True)
    latestPM03 = models.ForeignKey(TaskListPPM03, on_delete=models.CASCADE, related_name='masterDataTable_latestPM03',null=True, blank=True)
    laborCostOfPM03 = models.ForeignKey(TaskListPPM03, on_delete=models.CASCADE, related_name='masterDataTable_laborCostOfPM03',null=True, blank=True)

    taskPM04 = models.ForeignKey(TaskListAPM04, on_delete=models.CASCADE, related_name='masterDataTable_taskPM04',null=True, blank=True)
    countOfPM04 = models.ForeignKey(TaskListAPM04, on_delete=models.CASCADE, related_name='masterDataTable_countOfPM04',null=True, blank=True)
    latestPM04 = models.ForeignKey(TaskListAPM04, on_delete=models.CASCADE, related_name='masterDataTable_latestPM04',null=True, blank=True)
    laborCostOfPM04 = models.ForeignKey(TaskListAPM04, on_delete=models.CASCADE, related_name='masterDataTable_laborCostOfPM04',null=True, blank=True)

    taskPM05 = models.ForeignKey(TaskListPPM05, on_delete=models.CASCADE, related_name='masterDataTable_taskPM05',null=True, blank=True)
    countOfPM05 = models.ForeignKey(TaskListPPM05, on_delete=models.CASCADE, related_name='masterDataTable_countOfPM05',null=True, blank=True)
    latestPM05 = models.ForeignKey(TaskListPPM05, on_delete=models.CASCADE, related_name='masterDataTable_latestPM05',null=True, blank=True)
    laborCostOfPM05 = models.ForeignKey(TaskListPPM05, on_delete=models.CASCADE, related_name='masterDataTable_laborCostOfPM05',null=True, blank=True)


    #TypicalTaskList
    typicalTaskName = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='masterDataTable_typicalTaskName',null=True, blank=True)
    typicalConstPeriod = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='masterDataTable_typicalConstPeriod',null=True, blank=True)
    typicalTaskCost = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='masterDataTable_typicalTaskCost',null=True, blank=True)
    typicalNextEventDate = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='masterDataTable_typicalNextEventDate',null=True, blank=True)
    typicalSituation = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='masterDataTable_typicalSituation',null=True, blank=True)
    multiTask = models.ForeignKey(TypicalTaskList, on_delete=models.CASCADE, related_name='masterDataTable_multiTask',null=True, blank=True)


    #BomList
    bomCode = models.ForeignKey(BomList, on_delete=models.CASCADE, related_name='masterDataTable_bomList', null=True, blank=True)
    bomCost = models.DecimalField(verbose_name='bomCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    bomStock = models.DecimalField(verbose_name='bomStock',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    maxPartsDeliveryTimeInBom = models.ForeignKey(BomList, on_delete=models.CASCADE, related_name='masterDataTable_maxPartsDeliveryTimeInBom', null=True, blank=True)

    #将来的にcalかここで計算させる。
    totalCost = models.CharField(verbose_name='totalCost', max_length=200, blank=True,null=True,)

    #Impact
    levelSetValue = models.PositiveIntegerField(verbose_name='levelSetValue', null=True,blank=True,default=0)
    mttr = models.PositiveSmallIntegerField(verbose_name='mttr',blank=True,null=True,default=0)
    possibilityOfProductionLv = models.CharField(verbose_name='possibilityOfProductionLv', max_length=200,null=True,blank=True)

    # Critical Equipment Level
    impactForProduction = models.CharField(verbose_name='impactForProduction', max_length=200, blank=True,null=True,)
    probabilityOfFailure = models.CharField(verbose_name='probabilityOfFailure', max_length=200, blank=True,null=True,)
    assessment = models.CharField(verbose_name='assessment', max_length=20, blank=True,null=True,)

    #Status of measures
    rcaOrReplace = models.BooleanField(verbose_name='rcaOrReplace',default=False)
    sparePartsOrAlternative = models.BooleanField(verbose_name='sparePartsOrAlternative',default=False)
    coveredFromTask = models.BooleanField(verbose_name='coveredFromTask',default=False)
    twoways = models.BooleanField(verbose_name='twoways',default=False)
    ceDescription = models.TextField(verbose_name='ceDescription',blank=True,null=True,max_length=1000)


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
        verbose_name = 'Master Data Table'
        verbose_name_plural = 'Master Data Table'
        ordering = ('ceListNo',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    

    def __str__(self):
        return str('Master Data Table')



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




class AlertSchedule(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='alertSchedule_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='alertSchedule_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='alertSchedule_plant',null=True, blank=True)
    partsName = models.ForeignKey(BomList, on_delete=models.CASCADE, related_name='alertSchedule_partsName',null=True, blank=True)
    eventDate = models.DateField(verbose_name='eventDate', blank=True, null=True, default=timezone.now)
    deliveryTime = models.IntegerField(verbose_name='deliveryTime',null=True,blank=True,default=0)
    orderAlertDate = models.DateField(verbose_name='orderAlertDate',blank=True,null=True)
    safetyRate = models.CharField(verbose_name='safetyRate',blank=True,null=True,max_length=100)
    location = models.ForeignKey(AreaCode,on_delete=models.CASCADE, related_name='alertSchedule_areaCode',null=True, blank=True)

    class Meta:
        verbose_name = 'AlertSchedule'
        verbose_name_plural = 'AlertSchedule'
        ordering = ('companyCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    

    def __str__(self):
        return str('AlertSchedule')

    #orderAlertDateを算出する関数 　 CHECK OK 
    def calculate_order_alert_date(self):
        if self.eventDate and self.deliveryTime is not None and self.safetyRate:
            try:
                # deliveryTime を timedelta に変換
                delivery_timedelta = timedelta(days=self.deliveryTime)

                # eventDate から deliveryTime を引く
                estimated_date = self.eventDate - delivery_timedelta

                # safetyRate を小数に変換（例: "50%" -> 0.5）
                safety_rate_decimal = decimal.Decimal(self.safetyRate.strip('%')) / 100

                # 差分日数から safetyRate 分を引く（修正された部分）
                additional_days = int(delivery_timedelta.days * safety_rate_decimal)

                # eventDate から引く（修正された部分）
                new_order_alert_date = estimated_date - timedelta(days=additional_days)

                # 新しい値を設定
                self.orderAlertDate = new_order_alert_date.strftime("%Y-%m-%d")
            except (ValueError, TypeError, decimal.InvalidOperation):
                # 変換エラーや型エラー、無効な操作の場合は何もしない（あるいはエラーログを出力）
                pass

    def save(self, *args, **kwargs):
        self.calculate_order_alert_date()
        super().save(*args, **kwargs)

    
