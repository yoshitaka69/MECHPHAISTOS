from django.db import models
from django.db.models import Count

from django.utils import timezone
from accounts.models import CompanyCode,CompanyName,CustomUser



class NearMiss(models.Model):

    #on_delete は一応 PROTECT にしておく。ビッグデータは財産として残したいがプライバシーポリシーとも相談になる。
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='nearMiss_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='nearMiss_companyName', null=True, blank=True)

    nearMissNo = models.CharField(verbose_name='nearMissNo', max_length=50, null=True, blank=True)
    userName = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='nearMiss_userName', null=True, blank=True)
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='nearMiss_email', null=True, blank=True)
    department = models.CharField(verbose_name='department', max_length=200, null=True, blank=True)
    dateOfOccurrence = models.DateField(verbose_name='dateOfOccurrence', null=True, blank=True, default=timezone.now)
    placeOfOccurrence = models.CharField(verbose_name='placeOfOccurrence', max_length=200, null=True, blank=True)
    typeOfAccident = models.CharField(verbose_name='typeOfAccident', max_length=200, null=True, blank=True)
    description = models.TextField(verbose_name='description', max_length=1000, null=True, blank=True)
    factor = models.CharField(verbose_name='factor', max_length=200, null=True, blank=True)
    injuredLv = models.CharField(verbose_name='injuredLv', max_length=200, null=True, blank=True)
    equipmentDamageLv = models.CharField(verbose_name='equipmentDamageLv', max_length=200, null=True, blank=True)
    affectOfEnviroment = models.CharField(verbose_name='affectOfEnviroment', max_length=200, null=True, blank=True)
    newsCoverage = models.CharField(verbose_name='newsCoverage', max_length=200, null=True, blank=True)
    measures = models.CharField(verbose_name='measures', max_length=200, null=True, blank=True)
    actionItems = models.CharField(verbose_name='actionItems', max_length=200, null=True, blank=True)
    solvedActionItems = models.BooleanField(verbose_name='solvedActionItems', default=False)

    createdDay = models.DateTimeField(verbose_name='createdDay', null=True, blank=True, default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay', auto_now_add=True) 

    class Meta:
        verbose_name = 'Near Miss List'
        verbose_name_plural = 'Near Miss List'
        ordering = ('-createdDay',)

    def __str__(self):
        return f"{self.companyCode}"

    # saveメソッドをオーバーライドして、nearMissNoが未設定の場合に自動的に番号を生成する
    def save(self, *args, **kwargs):
        if not self.nearMissNo:
            # 既存の NearMissNo を取得し、番号を自動生成するロジック
            existing_near_miss_nos = NearMiss.objects.filter(companyCode=self.companyCode).values_list('nearMissNo', flat=True).order_by('nearMissNo')

            # 未使用の番号を探す
            used_numbers = set(int(nm.split('-')[-1]) for nm in existing_near_miss_nos if nm.split('-')[-1].isdigit())
            new_number = None

            # 未使用の番号を探す
            for i in range(1, len(used_numbers) + 2):
                if i not in used_numbers:
                    new_number = i
                    break

            # 最大の番号を取得し、その次の番号を生成
            if new_number is None:
                new_number = max(used_numbers) + 1 if used_numbers else 1

            # 番号をフォーマットして設定
            self.nearMissNo = f"NearMissNo-{str(new_number).zfill(5)}"

        # オーバーライドしたsaveメソッドで親クラスのsaveも実行
        super(NearMiss, self).save(*args, **kwargs)

        

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
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






class TrendSafetyIndicators(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='trendSafetyIndicators_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE,related_name='trendSafetyIndicators_companyName', null=True, blank=True)

    safetyIndicators = models.ForeignKey(SafetyIndicators, on_delete=models.CASCADE,related_name='trendSafetyIndicators_companyName', null=True, blank=True)
    lastUpdateDay = models.DateField(verbose_name='lastUpdateDay', null=True,blank=True, default=timezone.now)



    class Meta:
        verbose_name = 'Trend Safety Indicators'
        verbose_name_plural = 'Trend Safety Indicators'
        ordering = ('companyCode',)

    def __str__(self):
        return f"{self.companyCode}"






#------------------------------------------------------------------#
# update_total_of_near_miss 関数
# この関数はモデルの外部に配置し、スタンドアローンの関数として扱います。 CHECK OK
#------------------------------------------------------------------#
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




#------------------------------------------------------------------#
#action itemsのトータル数をカウントする。 CHECK OK
#------------------------------------------------------------------#
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




#------------------------------------------------------------------#
#solved action itemsのトータル数をカウントする。 CHECK OK
#------------------------------------------------------------------#
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



#-----------------------------------------------------------------------------------------------------#
# この関数は SafetyIndicators モデルの外部に配置し、スタンドアローンの関数として扱います。 CHECK OK
#-----------------------------------------------------------------------------------------------------#
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





#-----------------------------------------------------------------------------------------------------#
#danger Area 算出関数　CHECK OK
#-----------------------------------------------------------------------------------------------------#
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






