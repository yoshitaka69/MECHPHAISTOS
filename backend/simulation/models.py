from django.db import models
from accounts.models import CompanyCode,CompanyName,Plant


class BaseSimulation(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='baseSimulation_companyCode', null=True, blank=True)
    taskListNo = models.CharField(max_length=255)  # TaskListNoフィールド
    typicalTaskName = models.CharField(max_length=255)  # タスク名
    plant = models.CharField(max_length=255)  # プラント名
    equipment = models.CharField(max_length=255)  # 設備名
    machineName = models.CharField(max_length=255)  # 機械名
    typicalLatestDate = models.DateField()  # 最終日付
    multiTasking = models.BooleanField()  # 複数タスク
    totalCost = models.FloatField()  # 合計コスト
    taskOfPeriod = models.IntegerField()  # 期間タスク
    typicalNextEventDate = models.CharField(max_length=255, editable=False)  # 次のイベント日（読み取り専用）
    typicalSituation = models.CharField(max_length=255, editable=False)  # 現状（読み取り専用）
    
    # 次年以降のチェックボックス
    thisYear = models.BooleanField(editable=False)  # 読み取り専用
    thisYear1Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear2Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear3Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear4Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear5Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear6Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear7Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear8Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear9Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear10Later = models.BooleanField(editable=False)  # 読み取り専用


    def __str__(self):
        return self.typicalTaskName
    


class No1Simulation(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='no1Simulation_companyCode', null=True, blank=True)
    taskListNo = models.CharField(max_length=255)  # TaskListNoフィールド
    typicalTaskName = models.CharField(max_length=255)  # タスク名
    plant = models.CharField(max_length=255)  # プラント名
    equipment = models.CharField(max_length=255)  # 設備名
    machineName = models.CharField(max_length=255)  # 機械名
    typicalLatestDate = models.DateField()  # 最終日付
    multiTasking = models.BooleanField()  # 複数タスク
    totalCost = models.FloatField()  # 合計コスト
    taskOfPeriod = models.IntegerField()  # 期間タスク
    typicalNextEventDate = models.CharField(max_length=255, editable=False)  # 次のイベント日（読み取り専用）
    typicalSituation = models.CharField(max_length=255, editable=False)  # 現状（読み取り専用）
    
    # 次年以降のチェックボックス
    thisYear = models.BooleanField(editable=False)  # 読み取り専用
    thisYear1Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear2Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear3Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear4Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear5Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear6Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear7Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear8Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear9Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear10Later = models.BooleanField(editable=False)  # 読み取り専用


    def __str__(self):
        return self.typicalTaskName
    


class No2Simulation(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='no2Simulation_companyCode', null=True, blank=True)
    taskListNo = models.CharField(max_length=255)  # TaskListNoフィールド
    typicalTaskName = models.CharField(max_length=255)  # タスク名
    plant = models.CharField(max_length=255)  # プラント名
    equipment = models.CharField(max_length=255)  # 設備名
    machineName = models.CharField(max_length=255)  # 機械名
    typicalLatestDate = models.DateField()  # 最終日付
    multiTasking = models.BooleanField()  # 複数タスク
    totalCost = models.FloatField()  # 合計コスト
    taskOfPeriod = models.IntegerField()  # 期間タスク
    typicalNextEventDate = models.CharField(max_length=255, editable=False)  # 次のイベント日（読み取り専用）
    typicalSituation = models.CharField(max_length=255, editable=False)  # 現状（読み取り専用）
    
    # 次年以降のチェックボックス
    thisYear = models.BooleanField(editable=False)  # 読み取り専用
    thisYear1Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear2Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear3Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear4Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear5Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear6Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear7Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear8Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear9Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear10Later = models.BooleanField(editable=False)  # 読み取り専用


    def __str__(self):
        return self.typicalTaskName
    



class No3Simulation(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='no3Simulation_companyCode', null=True, blank=True)
    taskListNo = models.CharField(max_length=255)  # TaskListNoフィールド
    typicalTaskName = models.CharField(max_length=255)  # タスク名
    plant = models.CharField(max_length=255)  # プラント名
    equipment = models.CharField(max_length=255)  # 設備名
    machineName = models.CharField(max_length=255)  # 機械名
    typicalLatestDate = models.DateField()  # 最終日付
    multiTasking = models.BooleanField()  # 複数タスク
    totalCost = models.FloatField()  # 合計コスト
    taskOfPeriod = models.IntegerField()  # 期間タスク
    typicalNextEventDate = models.CharField(max_length=255, editable=False)  # 次のイベント日（読み取り専用）
    typicalSituation = models.CharField(max_length=255, editable=False)  # 現状（読み取り専用）
    
    # 次年以降のチェックボックス
    thisYear = models.BooleanField(editable=False)  # 読み取り専用
    thisYear1Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear2Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear3Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear4Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear5Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear6Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear7Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear8Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear9Later = models.BooleanField(editable=False)  # 読み取り専用
    thisYear10Later = models.BooleanField(editable=False)  # 読み取り専用


    def __str__(self):
        return self.typicalTaskName