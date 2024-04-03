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








class ActionItemList(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='actionItemList_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actionItemList_companyName', null=True, blank=True)
    actionItems = models.IntegerField(verbose_name='actionItems',null=True,blank=True,default=0)
    solvedActionItems = models.IntegerField(verbose_name='solvedActionItems',null=True,blank=True,default=0)

    
    class Meta:
        verbose_name = 'Action Item List'
        verbose_name_plural = 'Action Item List'
        ordering = ('-companyCode',)

    def __str__(self):
            return f'{self.companyCode}'

    def perform_create(self, serializer):
        action_item_instance = serializer.save()
        calculate_and_update_rate_of_action_items(action_item_instance.companyCode.id)

    def perform_update(self, serializer):
        action_item_instance = serializer.save()
        calculate_and_update_rate_of_action_items(action_item_instance.companyCode.id)





class SafetyIndicators(models.Model):
    
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='safetyIndicators_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='safetyIndicators_companyName', null=True, blank=True)
    safetyIndicators = models.CharField(verbose_name='safetyIndicators', max_length=20,null=True,blank=True)
    totalOfNearMiss = models.IntegerField(verbose_name='totalOfNearMiss',null=True,blank=True,default=0)
    rateOflevelA = models.IntegerField(verbose_name='totalOfNearMiss',null=True,blank=True,default=0)
    ActionItems = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='safetyIndicators_actionItems',null=True, blank=True)
    solvedActionItems = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='safetyIndicators_solvedActionItems',null=True, blank=True)
    rateOfActionItems = models.IntegerField(verbose_name='totalOfNearMiss',null=True,blank=True,default=0)

   
    class Meta:
        verbose_name = 'Safety Indicators'
        verbose_name_plural = 'Safety Indicators'
        ordering = ('-companyCode',)

    def __str__(self):
            return f'{self.safetyIndicators}'


    #Safety indicatorsの設定
    def calculate_safety_indicators(self):
        rate_of_level_a = self.rate_of_level_a()
        rate_of_action_items = self.rate_of_action_items()
        if rate_of_level_a >= 40:
            return 'High'
        elif rate_of_level_a < 40:
            if rate_of_action_items > 80:
                return 'High'
            elif 40 < rate_of_action_items <= 80:
                return 'Middle'
            elif 0 < rate_of_action_items <= 40:
                return 'Low'
        return 'Undefined'

