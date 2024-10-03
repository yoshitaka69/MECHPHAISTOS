from django.db import models
from accounts.models import CompanyCode
from ceList.models import Equipment,Machine,CeList
from django.utils import timezone
from datetime import date



# Reliability
#-------------------------------------------------------------------------------------------------------------------------------------
from django.db import models
from datetime import date

class Reliability(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='reliability_companyCode', null=True, blank=True)
    ceListNo = models.ForeignKey(CeList, on_delete=models.CASCADE, related_name='reliability_ceListNo', null=True, blank=True)
    plant = models.CharField(max_length=100, verbose_name='Plant', null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='reliability_equipment', null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='reliability_machine', null=True, blank=True)
    maintenanceTitle = models.CharField(max_length=200, verbose_name='Maintenance Title', null=True, blank=True)  # Maintenance Title フィールド

    failureType = models.IntegerField(
        choices=[
            (1, 'Electrical'),
            (2, 'Mechanical'),
            (3, 'Software'),
            (4, 'Building'),
            (5, 'Utility')
        ],
        null=True, blank=True,
        verbose_name='Failure Type'
    )

    # 補足説明用のテキストフィールド
    failureTypeDetail = models.TextField(
        verbose_name='Failure Type Detail',
        null=True, blank=True
    )

    operationalCondition = models.IntegerField(
        choices=[
            (0, 'Normal Operation (正常運転)'),
            (1, 'Abnormal Operation (異常運転)'),
            (2, 'Stopped (停止)'),
            (3, 'Maintenance Ongoing (保全中)'),
            (4, 'Under Investigation (調査中)')
        ],
        null=True, blank=True,
        verbose_name='Operational Conditions'
    )

    # 補足説明用のテキストフィールド
    operationalConditionDetail = models.TextField(
        verbose_name='Operational Condition Detail',
        null=True, blank=True
    )


    PMType = models.IntegerField(
        choices=[
            (1, 'PM01: Inspection (検査)'),
            (2, 'PM02: Preventive Maintenance (予防保全)'),
            (3, 'PM03: Corrective Maintenance (修正保全)'),
            (4, 'PM04: Breakdown Maintenance (緊急保全)'),
            (5, 'PM05: Improvement (改善改造)'),
            (6, 'PM06'),
            (7, 'PM07'),
            (8, 'PM08'),
            (9, 'PM09'),
            (10, 'PM10')
        ],
        null=True, blank=True,
        verbose_name='PM Type'
    )



    maintenanceMethod = models.IntegerField(
        choices=[
            (1, 'Inspection (点検)'),
            (2, 'Lubrication (潤滑)'),
            (3, 'Adjustment (調整)'),
            (4, 'Replacement (交換)'),
            (5, 'Cleaning (清掃)'),
            (6, 'Repair (修理)'),
            (7, 'Regular Maintenance (定期保全)'),
            (8, 'Overhaul (オーバーホール)'),
            (9, 'Improvement (改善)'),
            (10, 'New Installation (新規設置)'),
            (11, 'Other (その他)')
        ],
        null=True, blank=True,
        verbose_name='Maintenance Method'
    )

    # 補足説明用のテキストフィールド
    maintenanceMethodDetail = models.TextField(
        verbose_name='Maintenance Method Detail',
        null=True, blank=True
    )

    maintenanceFrequency = models.IntegerField(verbose_name='maintenanceFrequency', null=True, blank=True)


    failureMode = models.IntegerField(
        choices=[
            (1, 'Wear (摩耗)'),
            (2, 'Fatigue Failure (疲労破壊)'),
            (3, 'Corrosion (腐食)'),
            (4, 'Overheating (過熱)'),
            (5, 'Inadequate Lubrication (潤滑不足)'),
            (6, 'Seal Failure (シール破損)'),
            (7, 'Overload (過負荷)'),
            (8, 'Vibration (振動)'),
            (9, 'Electrical Insulation Failure (絶縁破壊)'),
            (10, 'Short Circuit (短絡)'),
            (11, 'Mechanical Shock (機械的衝撃)'),
            (12, 'Thermal Fatigue (熱疲労)'),
            (13, 'Cavitation (キャビテーション)'),
            (14, 'Frictional Wear (摩擦摩耗)'),
            (15, 'Stress Corrosion Cracking (応力腐食割れ)'),
            (16, 'Erosion (浸食)'),
            (17, 'Oxidation (酸化)'),
            (18, 'Cable Breakage (ケーブル断線)'),
            (19, 'Bearing Failure (ベアリング破損)'),
            (20, 'Electronic Component Failure (電子部品故障)'),
            (21, 'Piping Leak (配管漏れ)'),
            (22, 'Piping Blockage (配管閉塞)'),
            (23, 'Building Structural Failure (建物の構造的問題)'),
            (24, 'Utility Failure (ユーティリティ故障)'),
            (25, 'Other (その他)')
        ],
        null=True, blank=True,
        verbose_name='Failure Mode'
    )

    # 補足説明用のテキストフィールド
    failureModeDetail = models.TextField(
        verbose_name='Failure Mode Detail',
        null=True, blank=True
    )



    failureCause = models.IntegerField(
        choices=[
            (1, 'Human Error (人的ミス)'),
            (2, 'Fatigue Failure (疲労破壊)'),
            (3, 'Overheating/Overload (過熱 / 過負荷)'),
            (4, 'Misuse (誤使用)'),
            (5, 'Operational Error (操作ミス)'),
            (6, 'Manufacturing Defect (製造欠陥)'),
            (7, 'Inadequate Maintenance (不適切な保守)'),
            (8, 'Improper Installation (不適切な設置)'),
            (9, 'Material Issue (材料の問題)'),
            (10, 'Progressive Damage (進行的な損傷)'),
            (11, 'Corrosion (腐食)'),
            (12, 'Control System Failure (制御系の異常)'),
            (13, 'Process Defect (工程の欠陥)'),
            (14, 'External Factor (外部要因)'),
            (15, 'Natural Disaster (天変地異)'),
            (16, 'Other (その他)')
        ],
        null=True, blank=True,
        verbose_name='Failure Cause'
    )

    # 補足説明用のテキストフィールド
    failureCauseDetail = models.TextField(
        verbose_name='Failure Cause Detail',
        null=True, blank=True
    )

    componentCondition = models.IntegerField(
        choices=[
            (1, 'Partial Replacement (一部交換)'),
            (2, 'Full Replacement (全部交換)'),
            (3, 'Continue Using Without Replacement (交換せずに継続使用)')
        ],
        null=True, blank=True,
        verbose_name='Component Condition'
    )

    # 補足説明用のテキストフィールド
    componentConditionDetail = models.TextField(
        verbose_name='Component Condition Detail',
        null=True, blank=True
    )

    
    mttr = models.IntegerField(verbose_name='MTTR', null=True, blank=True)
    mtbf = models.IntegerField(verbose_name='MTBF', null=True, blank=True)
    mttf = models.IntegerField(verbose_name='MTTF', null=True, blank=True)
    totalOperatingTime = models.FloatField(verbose_name='Total Operating Time', null=True, blank=True)
    failureCount = models.IntegerField(verbose_name='Failure Count', null=True, blank=True)
    failureDate = models.DateField(verbose_name='Failure Date', null=True, blank=True)
    

    remark = models.TextField(verbose_name='Remark', null=True, blank=True)  # Remark フィールド
    record_date = models.DateField(verbose_name='Record Date', default=date.today)

    class Meta:
        ordering = ['-mttr']




#-------------------------------------------------------------------------------------------------------------------------------------







# 故障履歴モデル(PrecisionAndAccuracy)
#-------------------------------------------------------------------------------------------------------------------------------------
class TroubleHistory(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='troubleHistory_companyCode', null=True, blank=True)
    ceListNo = models.ForeignKey(CeList, on_delete=models.CASCADE, related_name='troubleHistory_ceListNo',null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='troubleHistory_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='troubleHistory_machine',null=True, blank=True)

    date = models.DateField(verbose_name='date', null=True, blank=True, default=timezone.now)
    pmType = models.CharField(verbose_name='pmType', max_length=50, null=True, blank=True)
    failureContent = models.TextField(verbose_name='failureContent', max_length=1000, null=True, blank=True)
    failureType = models.CharField(verbose_name='failureType', max_length=50, null=True, blank=True)
    repairMethod = models.TextField(verbose_name='repairMethod', max_length=1000, null=True, blank=True)
    repairCost = models.DecimalField(verbose_name='repairCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    rootCause = models.TextField(verbose_name='rootCause', max_length=1000, null=True, blank=True)

    class Meta:
        ordering = ['-date']


#-------------------------------------------------------------------------------------------------------------------------------------



# 故障予測ポイントモデル(PrecisionAndAccuracy)
#-------------------------------------------------------------------------------------------------------------------------------------
class FailurePredictionPoint(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='failurePredictionPoint_companyCode', null=True, blank=True)
    ceListNo = models.CharField(verbose_name='ceListNo', max_length=100,blank=True,null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='failurePredictionPoint_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='failurePredictionPoint_machine',null=True, blank=True)

    date = models.DateField(verbose_name='date', null=True, blank=True, default=timezone.now)
    pmType = models.CharField(verbose_name='pmType', max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['-date']


#-------------------------------------------------------------------------------------------------------------------------------------







