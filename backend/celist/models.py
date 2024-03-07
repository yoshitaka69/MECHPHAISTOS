from django.db import models
from django.utils import timezone
from datetime import timedelta
from accounts.models import Company


#Critical equipment は親。<<Ce>>　>　Task　> SpareParts
class CeList(models.Model):
    slug = models.SlugField()

    #accountsから取得
    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    
    #Celistメインの項目
    ceListNo = models.PositiveIntegerField(verbose_name='ceListNo', null=True,blank=True,default=0)
    plant = models.CharField(verbose_name='plant', max_length=200,null=True,blank=True)
    equipment = models.CharField(verbose_name='equipment', max_length=200,null=True,blank=True)
    function = models.CharField(verbose_name='function', max_length=200,null=True,blank=True)
    locationNo = models.CharField(verbose_name='locationNo', max_length=200,null=True,blank=True)#いつか設置されている場所を指定する場合のため
    #Task List
    taskListNo = models.CharField(verbose_name='taskListNo', max_length=200,null=True,blank=True)
    #Impact
    levelSetValue = models.PositiveIntegerField(verbose_name='levelSetValue', null=True,blank=True,default=0)
    mttr = models.PositiveSmallIntegerField(verbose_name='mttr',blank=True,null=True,default=0)
    possibilityOfProductionLv = models.CharField(verbose_name='possibilityOfProductionLv', max_length=200,null=True,blank=True)
    # Critical Equipment Level
    impactForProduction = models.CharField(verbose_name='impactForProduction', max_length=200, blank=True,null=True,)
    probabilityOfFailure = models.CharField(verbose_name='probabilityOfFailure', max_length=200, blank=True,null=True,)
    assessment = models.CharField(verbose_name='assessment', max_length=20, blank=True,null=True,)
    #Spare parts
    bomNo = models.CharField(verbose_name='bomNo', max_length=200,null=True,blank=True)
    #Status of measures
    rcaOrReplace = models.BooleanField(verbose_name='rcaOrReplace',default=False)
    sparePartsOrAlternative = models.BooleanField(verbose_name='sparePartsOrAlternative',default=False)
    coveredFromTask = models.BooleanField(verbose_name='coveredFromTask',default=False)
    twoways = models.BooleanField(verbose_name='twoways',default=False)
    ceDescription = models.TextField(verbose_name='ceDescription',blank=True,null=True,max_length=1000)


    #以下はSparePartsからJunctionTableで加工して取得
    #partsDeliveryTime = models.DateField(verbose_name='partsDeliveryTime',blank=True,null=True,default=timezone.now)
    #category = models.ForeignKey(SpareParts, on_delete=models.PROTECT, null=True, blank=True)
    #stock = models.ForeignKey(SpareParts, on_delete=models.PROTECT, null=True, blank=True)
    #totalBomCost = models.DecimalField(verbose_name='totalBomCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00,)

    #以下はtaskListからJunctionTableで加工して取得
    #Probability of failure
    #constructionPeriod = models.DateField(verbose_name='constructionPeriod',blank=True,null=True,default=timezone.now)
    # PM02
    #countOfPM02 = models.PositiveSmallIntegerField(verbose_name='countOfPM02',blank=True,null=True,default=0)
    #latestPM02 = models.DateField(verbose_name='latestPM02',blank=True,null=True)
    # PM03
    #countOfPM03 = models.PositiveSmallIntegerField(verbose_name='countOfPM03',blank=True,null=True,default=0)
    #latestPM03 = models.DateField(verbose_name='latestPM03',blank=True,null=True)
    #taskOfPM03 = models.CharField(verbose_name='taskOfPM03', max_length=200)
    # PM04
    #countOfPM04 = models.PositiveSmallIntegerField(verbose_name='countOfPM04',blank=True,null=True,default=0)
    #latestPM04 = models.DateField(verbose_name='latestPM04', blank=True,null=True)
    #taskOfPM04 = models.CharField(verbose_name='taskOfPM04', max_length=200,blank=True,null=True)
    # PM005
    #countOfPM05 = models.PositiveSmallIntegerField(verbose_name='countOfPM05', blank=True,null=True,default=0,)
    #latestPM05 = models.DateField(verbose_name='latestPM05', blank=True,null=True)
    #taskOfPM05 = models.CharField(verbose_name='taskOfPM05', max_length=200,blank=True,null=True)
    #taskOfPM
    #taskOfPM02 = models.CharField(verbose_name='taskOfPM02', max_length=200)#これはいつかForeignKeyで結びつける。そのためTask側で代表的な値を決めさせるメソッドを組む必要あり。
    #laborOfPM02 = models.DecimalField(verbose_name='laborOfPM02',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00,)#↑と同じ
    #periodOfPM02 = models.DateField(verbose_name='periodOfPM02', blank=True,null=True,default=timezone.now)#↑と同じ
    #nextEventDate = models.DateField(verbose_name='nextEventDate', blank=True,null=True,default=timezone.now)
    #situation = models.CharField(verbose_name='situation', max_length=200,null=True,blank=True)    

class Meta:
    verbose_name = 'Critical equipment list'
    verbose_name_plural = 'Critical equipment list'
    ordering = ('ceListNo',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。

def __str__(self):
        return self.CeListNo






