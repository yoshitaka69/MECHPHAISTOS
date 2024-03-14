from django.db import models
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

    createdDay = models.DateTimeField(verbose_name='createdDay',null=True,blank=True,default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay',auto_now_add=True) 


    class Meta:
        verbose_name = 'Near Miss List'
        verbose_name_plural = 'Near Miss List'
        ordering = ('-createdDay',)

    def __str__(self):
            return f'{self.nearMissNo}'

class NeededActionItemList(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='safetyindicators_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='safetyindicators_companyName', null=True, blank=True)
    actionItems = models.IntegerField(verbose_name='actionItems',null=True,blank=True,default=0)
    solvedActionItems = models.IntegerField(verbose_name='solvedActionItems',null=True,blank=True,default=0)
    

class SafetyIndicators(models.Model):
    
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='safetyindicators_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='safetyindicators_companyName', null=True, blank=True)
    safetyIndicators = models.CharField(verbose_name='safetyIndicators', max_length=20,null=True,blank=True)
    totalOfNearMiss = models.IntegerField(verbose_name='totalOfNearMiss',null=True,blank=True,default=0)
    rateOflevelA = models.IntegerField(verbose_name='totalOfNearMiss',null=True,blank=True,default=0)
    ActionItems = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='safetyindicators_actionItems',null=True, blank=True)
    solvedActionItems = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='safetyindicators_solvedActionItems',null=True, blank=True)
    rateOfActionItems = models.IntegerField(verbose_name='totalOfNearMiss',null=True,blank=True,default=0)
    
    
    def update_total_of_near_miss(self):
        # NearMiss モデルのレコード数をカウント
        total = NearMiss.objects.filter(companyCode=self.companyCode).count()
        self.totalOfNearMiss = total
        self.save()

        #MeasuresのAの値をカウントする。
        update_rate_of_level_a(self):
        total_near_miss = NearMiss.objects.filter(companyCode=self.companyCode).count()
        if total_near_miss > 0:
            level_a_count = NearMiss.objects.filter(
                companyCode=self.companyCode,
                measures__contains='A'  # 'measures' フィールドで 'A' を含むレコードをフィルタリング
            ).count()
            self.rateOflevelA = (level_a_count / total_near_miss) * 100
        else:
            self.rateOflevelA = 0  # totalOfNearMiss が 0 の場合はレートも 0 とする
        self.save()

        #rateOfactionItemsの関数
        update_rate_of_action_items(self):
        total_action_items = ActionItems.objects.filter(companyCode=self.companyCode).count()
        solved_action_items = solvedActionItems.objects.filter(companyCode=self.companyCode).count()

        if total_action_items > 0:
            rate = (solved_action_items / total_action_items) * 100
            self.rateOfActionItems = round(rate, 2)  # 結果を四捨五入して2桁の小数点以下まで表示
        else:
            self.rateOfActionItems = 0  # トータルが0の場合は率も0とする

        self.save()

        #safetyindicatorsの指標
        get_safety_level(self):
            if self.rateOflevelA >= 40:
                return 'High'
            elif self.rateOflevelA < 40:
                if self.rateOfActionItems > 80:
                    return 'High'
                elif 40 < self.rateOfActionItems <= 80:
                    return 'Middle'
                elif 0 < self.rateOfActionItems <= 40:
                    return 'Low'
            return 'Undefined'


    
    class Meta:
        verbose_name = 'Safety Indicators'
        verbose_name_plural = 'Safety Indicators'
        ordering = ('-companyCode',)

    def __str__(self):
            return f'{self.safetyIndicators}'


