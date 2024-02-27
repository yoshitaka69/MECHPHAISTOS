from django.db import models
from django.utils import timezone

class NearMiss(models.Model):

    slug = models.SlugField()

    nearMissListNo = models.CharField(verbose_name='NearMissListNo', max_length=200,null=True,blank=True)
    userName = models.CharField(verbose_name='userName', max_length=200,null=True,blank=True)
    department = models.CharField(verbose_name='department', max_length=200,null=True,blank=True)
    dateOfOccurrence = models.DateField(verbose_name='dateOfOccurrence', default=timezone.now)
    placeOfOccurrence = models.CharField(verbose_name='placeOfOccurrence', max_length=200,null=True,blank=True)
    typeOfAccident = models.CharField(verbose_name='typeOfAccident', max_length=200,null=True,blank=True)
    description = models.CharField(verbose_name='description', max_length=500,null=True,blank=True)
    factor = models.CharField(verbose_name='factor', max_length=200,null=True,blank=True)
    injuredLv = models.CharField(verbose_name='injuredLv', max_length=200,null=True,blank=True)
    equipmentDamageLv = models.CharField(verbose_name='equipmentDamageLv', max_length=200,null=True,blank=True)
    affectOfEnviroment = models.CharField(verbose_name='affectOfEnviroment', max_length=200,null=True,blank=True)
    newsCoverage = models.CharField(verbose_name='newsCoverage', max_length=200,null=True,blank=True)
    safetyIndicater = models.CharField(verbose_name='safetyIndicater', max_length=200,null=True,blank=True)
    measures = models.CharField(verbose_name='measures', max_length=200,null=True,blank=True)

    createdDay = models.DateTimeField(verbose_name='createdDay',default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay',auto_now_add=True) 

class Meta:
    verbose_name_plural = 'Near Miss List'
    ordering = ('-date_added',)

