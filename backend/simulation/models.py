from django.db import models
from accounts.models import CompanyCode


class No1Simulation(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='no1Simulation_companyCode', null=True, blank=True)
    taskListNo = models.CharField(max_length=255, null=True, blank=True)  # TaskListNoフィールド
    typicalTaskName = models.CharField(max_length=255, null=True, blank=True)  # タスク名
    plant = models.CharField(max_length=255, null=True, blank=True)  # プラント名
    equipment = models.CharField(max_length=255, null=True, blank=True)  # 設備名
    machineName = models.CharField(max_length=255, null=True, blank=True)  # 機械名
    PMType = models.CharField(max_length=255, null=True, blank=True)  # PMタイプ
    maintenanceType = models.CharField(max_length=255, null=True, blank=True)  # 機械名
    typicalLatestDate = models.DateField(null=True, blank=True)  # 最終日付
    taskOfPeriod = models.IntegerField(null=True, blank=True)  # 期間タスク
    totalLaborCost = models.FloatField(null=True, blank=True)  
    bomCode = models.IntegerField(null=True, blank=True)  # BOMコード
    bomCost = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return self.typicalTaskName if self.typicalTaskName else "No Name"


class No2Simulation(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='no2Simulation_companyCode', null=True, blank=True)
    taskListNo = models.CharField(max_length=255, null=True, blank=True)  # TaskListNoフィールド
    typicalTaskName = models.CharField(max_length=255, null=True, blank=True)  # タスク名
    plant = models.CharField(max_length=255, null=True, blank=True)  # プラント名
    equipment = models.CharField(max_length=255, null=True, blank=True)  # 設備名
    machineName = models.CharField(max_length=255, null=True, blank=True)  # 機械名
    PMType = models.CharField(max_length=255, null=True, blank=True)  # PMタイプ
    maintenanceType = models.CharField(max_length=255, null=True, blank=True)  # 機械名
    typicalLatestDate = models.DateField(null=True, blank=True)  # 最終日付
    taskOfPeriod = models.IntegerField(null=True, blank=True)  # 期間タスク
    totalLaborCost = models.FloatField(null=True, blank=True)  
    bomCode = models.IntegerField(null=True, blank=True)  # BOMコード
    bomCost = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return self.typicalTaskName if self.typicalTaskName else "No Name"


class No3Simulation(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='no3Simulation_companyCode', null=True, blank=True)
    taskListNo = models.CharField(max_length=255, null=True, blank=True)  # TaskListNoフィールド
    typicalTaskName = models.CharField(max_length=255, null=True, blank=True)  # タスク名
    plant = models.CharField(max_length=255, null=True, blank=True)  # プラント名
    equipment = models.CharField(max_length=255, null=True, blank=True)  # 設備名
    machineName = models.CharField(max_length=255, null=True, blank=True)  # 機械名
    PMType = models.CharField(max_length=255, null=True, blank=True)  # PMタイプ
    maintenanceType = models.CharField(max_length=255, null=True, blank=True)  # 機械名
    typicalLatestDate = models.DateField(null=True, blank=True)  # 最終日付
    taskOfPeriod = models.IntegerField(null=True, blank=True)  # 期間タスク
    totalLaborCost = models.FloatField(null=True, blank=True)  
    bomCode = models.IntegerField(null=True, blank=True)  # BOMコード
    bomCost = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return self.typicalTaskName if self.typicalTaskName else "No Name"
