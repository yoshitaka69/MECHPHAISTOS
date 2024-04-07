from django.db import models
from django.db.models import Count

from django.utils import timezone
from accounts.models import CompanyCode,CompanyName,CustomUser



class NearMiss(models.Model):

    #on_delateはいちよPROTECTにしておく。ビッグデータは財産として残したいがプライバシーポリシーとも相談になる。
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='nearMiss_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE,related_name='nearMiss_companyName', null=True, blank=True)

    nearMissNo = models.CharField(verbose_name='nearMissNo', max_length=50,null=True,blank=True)
    userName = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='nearMiss_userName', null=True, blank=True)
    department = models.CharField(verbose_name='department', max_length=200,null=True,blank=True)
    dateOfOccurrence = models.DateField(verbose_name='dateOfOccurrence', null=True,blank=True, default=timezone.now)
    placeOfOccurrence = models.CharField(verbose_name='placeOfOccurrence', max_length=200,null=True,blank=True)
    typeOfAccident = models.CharField(verbose_name='typeOfAccident', max_length=200,null=True,blank=True)
    description = models.TextField(verbose_name='description', max_length=1000,null=True,blank=True)
    factor = models.CharField(verbose_name='factor', max_length=200,null=True,blank=True)
    injuredLv = models.CharField(verbose_name='injuredLv', max_length=200,null=True,blank=True)
    equipmentDamageLv = models.CharField(verbose_name='equipmentDamageLv', max_length=200,null=True,blank=True)
    affectOfEnviroment = models.CharField(verbose_name='affectOfEnviroment', max_length=200,null=True,blank=True)
    newsCoverage = models.CharField(verbose_name='newsCoverage', max_length=200,null=True,blank=True)
    measures = models.CharField(verbose_name='measures', max_length=200,null=True,blank=True)
    actionItems = models.CharField(verbose_name='actionItems', max_length=200,null=True,blank=True)
    solvedActionItems = models.BooleanField(verbose_name='solvedActionItems',default=False)

    createdDay = models.DateTimeField(verbose_name='createdDay',null=True,blank=True,default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay',auto_now_add=True) 


    class Meta:
        verbose_name = 'Near Miss List'
        verbose_name_plural = 'Near Miss List'
        ordering = ('-createdDay',)

    def __str__(self):
        return f"{self.companyCode}"
    

    def save(self, *args, **kwargs):
        # nearMissNo がまだ設定されていない場合のみ生成
        if not self.nearMissNo:
            last_instance = NearMiss.objects.filter(companyCode=self.companyCode).order_by('nearMissNo').last()
            if last_instance:
                try:
                    last_number = int(last_instance.nearMissNo.split('-')[-1])
                    new_number = last_number + 1
                except ValueError:
                    # last_instance.nearMissNo の形式が期待と異なる場合のエラーハンドリング
                    new_number = 1
            else:
                new_number = 1
            self.nearMissNo = f"{self.companyCode}-{str(new_number).zfill(3)}"

        super().save(*args, **kwargs)

        # 追加の処理を呼び出し
        update_total_of_near_miss(self.companyCode_id)
        update_total_of_action_items(self.companyCode_id)
        update_total_of_solved_action_items(self.companyCode_id)
        update_count_of_level_a(self.companyCode_id)
        update_danger_area(self.companyCode_id)




class SafetyIndicators(models.Model):
    
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='safetyIndicators_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='safetyIndicators_companyName', null=True, blank=True)
    safetyIndicators = models.CharField(verbose_name='safetyIndicators', max_length=20,null=True,blank=True)
    dangerArea = models.CharField(verbose_name='dangerArea', max_length=20,null=True,blank=True)
    totalOfNearMiss = models.IntegerField(verbose_name='totalOfNearMiss',null=True,blank=True,default=0)
    countOfLevelA = models.IntegerField(verbose_name='countOfLevelA',null=True,blank=True,default=0)
    rateOflevelA = models.IntegerField(verbose_name='rateOflevelA',null=True,blank=True,default=0)
    countOfActionItems = models.IntegerField(verbose_name='countOfActionItems',null=True,blank=True,default=0)
    countOfSolvedActionItems = models.IntegerField(verbose_name='countOfSolvedActionItems',null=True,blank=True,default=0)
    rateOfActionItems = models.IntegerField(verbose_name='rateOfActionItems',null=True,blank=True,default=0)

   
    class Meta:
        verbose_name = 'Safety Indicators'
        verbose_name_plural = 'Safety Indicators'
        ordering = ('-companyCode',)

    def __str__(self):
            return f'{self.safetyIndicators}'
    

    def save(self, *args, **kwargs):
        # rateOfActionItemsの計算
        if self.countOfActionItems > 0:
            self.rateOfActionItems = (self.countOfSolvedActionItems / self.countOfActionItems) * 100
        else:
            self.rateOfActionItems = 0

        # rateOflevelAの計算
        if self.totalOfNearMiss > 0:
            self.rateOflevelA = (self.countOfLevelA / self.totalOfNearMiss) * 100
        else:
            self.rateOflevelA = 0

        # safetyIndicatorsの計算
        if self.rateOflevelA >= 40:
            self.safetyIndicators = 'High'
        elif self.rateOflevelA < 40:
            if self.rateOfActionItems > 80:
                self.safetyIndicators = 'High'
            elif 40 < self.rateOfActionItems <= 80:
                self.safetyIndicators = 'Middle'
            elif 0 < self.rateOfActionItems <= 40:
                self.safetyIndicators = 'Low'
        else:
            self.safetyIndicators = 'Undefined'

        super().save(*args, **kwargs)



# update_total_of_near_miss 関数
# この関数はモデルの外部に配置し、スタンドアローンの関数として扱います。
def update_total_of_near_miss(company_code_id):
    total_near_miss_count = NearMiss.objects.filter(companyCode_id=company_code_id).count()
    safety_indicator, created = SafetyIndicators.objects.get_or_create(
        companyCode_id=company_code_id,
        defaults={'totalOfNearMiss': total_near_miss_count}
    )
    if not created:
        safety_indicator.totalOfNearMiss = total_near_miss_count
        safety_indicator.save()
    print(f"Updated SafetyIndicators for CompanyCode {company_code_id}: Total of Near Miss = {total_near_miss_count}")




#action itemsのトータル数をカウントする。
def update_total_of_action_items(company_code_id):
    action_items_count = NearMiss.objects.filter(companyCode_id=company_code_id).count()
    safety_indicator, created = SafetyIndicators.objects.get_or_create(
        companyCode_id=company_code_id,
        defaults={'countOfActionItems': action_items_count}  # ここを修正
    )
    if not created:
        safety_indicator.countOfActionItems = action_items_count
        safety_indicator.save()
    print(f"Updated SafetyIndicators for CompanyCode {company_code_id}: Action Items = {action_items_count}")




#solved action itemsのトータル数をカウントする。
def update_total_of_solved_action_items(company_code_id):
    # ここでのカウントロジックは、NearMissのsolvedActionItemsをどのように扱っているかによります
    # 例えば、solvedActionItemsがブール値フィールドであれば、filter()で条件を指定する
    solved_action_items_count = NearMiss.objects.filter(companyCode_id=company_code_id, solvedActionItems=True).count()
    safety_indicator, created = SafetyIndicators.objects.get_or_create(
        companyCode_id=company_code_id,
        defaults={'solvedActionItems': solved_action_items_count}
    )
    if not created:
        safety_indicator.countOfSolvedActionItems = solved_action_items_count
        safety_indicator.save()
    print(f"Updated SafetyIndicators for CompanyCode {company_code_id}: Solved Action Items = {solved_action_items_count}")



# この関数は SafetyIndicators モデルの外部に配置し、スタンドアローンの関数として扱います。
def update_count_of_level_a(company_code_id):
    level_a_count = NearMiss.objects.filter(companyCode_id=company_code_id, measures='A').count()
    safety_indicator, created = SafetyIndicators.objects.get_or_create(
        companyCode_id=company_code_id,
        defaults={'countOfLevelA': level_a_count}
    )
    if not created:
        safety_indicator.countOfLevelA = level_a_count
        safety_indicator.save()
    print(f"Updated SafetyIndicators for CompanyCode {company_code_id}: Count of Level A = {level_a_count}")


def update_danger_area(company_code_id):
    # companyCodeに基づいてNearMissインスタンスのplaceOfOccurrenceを集計
    most_common_place = NearMiss.objects.filter(companyCode_id=company_code_id) \
                        .values('placeOfOccurrence') \
                        .annotate(count=Count('placeOfOccurrence')) \
                        .order_by('-count') \
                        .first()

    if most_common_place:
        # SafetyIndicatorsモデルのインスタンスを取得または作成
        safety_indicator, created = SafetyIndicators.objects.get_or_create(
            companyCode_id=company_code_id,
            defaults={'dangerArea': most_common_place['placeOfOccurrence']}
        )
        if not created:
            safety_indicator.dangerArea = most_common_place['placeOfOccurrence']
            safety_indicator.save()
        print(f"Updated SafetyIndicators for CompanyCode {company_code_id}: Danger Area = {most_common_place['placeOfOccurrence']}")
