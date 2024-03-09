from django.db import models
from django.utils import timezone
from accounts.models import Company

class NearMiss(models.Model):

    #slug = models.SlugField()

    #on_delateはいちよPROTECTにしておく。ビッグデータは財産として残したいがプライバシーポリシーとも相談になる。
    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    nearMissListNo = models.IntegerField(null=True, blank=True)
    userName = models.CharField(verbose_name='userName', max_length=200,null=True,blank=True)
    department = models.CharField(verbose_name='department', max_length=200,null=True,blank=True)
    dateOfOccurrence = models.DateField(verbose_name='dateOfOccurrence', default=timezone.now)
    placeOfOccurrence = models.CharField(verbose_name='placeOfOccurrence', max_length=200,null=True,blank=True)
    typeOfAccident = models.CharField(verbose_name='typeOfAccident', max_length=200,null=True,blank=True)
    description = models.TextField(verbose_name='description', max_length=1000,null=True,blank=True)
    factor = models.CharField(verbose_name='factor', max_length=200,null=True,blank=True)
    injuredLv = models.CharField(verbose_name='injuredLv', max_length=200,null=True,blank=True)
    equipmentDamageLv = models.CharField(verbose_name='equipmentDamageLv', max_length=200,null=True,blank=True)
    affectOfEnviroment = models.CharField(verbose_name='affectOfEnviroment', max_length=200,null=True,blank=True)
    newsCoverage = models.CharField(verbose_name='newsCoverage', max_length=200,null=True,blank=True)
    safetyIndicater = models.CharField(verbose_name='safetyIndicater', max_length=200,null=True,blank=True)
    measures = models.CharField(verbose_name='measures', max_length=200,null=True,blank=True)

    totalOfNearMiss = models.IntegerField(null=True,blank=True,default=0)

    createdDay = models.DateTimeField(verbose_name='createdDay',default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay',auto_now_add=True) 


    class Meta:
        verbose_name = 'Near Miss List'
        verbose_name_plural = 'Near Miss List'
        ordering = ('-createdDay',)

    def __str__(self):
            return self.nearMissListNo