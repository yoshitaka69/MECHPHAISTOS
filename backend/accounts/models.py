from django.db import models
from django.utils import timezone

#企業情報リスト
class Company(models.Model):
    slug = models.SlugField()

    companyListNo = models.IntegerField(verbose_name='companyListNo', default=0)
    companyName = models.IntegerField(verbose_name='companyName', default=0)
    country = models.IntegerField(verbose_name='country', default=0)
    zipCode = models.IntegerField(verbose_name='zipCode', default=0)
    accountType = models.IntegerField(verbose_name='accountType', default=0)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 


class Meta:
    verbose_name_plural = 'Accounts List'
    ordering = ('-date_added',)


#ユーザーリスト
class User(models.Model):
    slug = models.SlugField()

    userName = models.IntegerField(verbose_name='userName', default=0)
    firstName = models.IntegerField(verbose_name='firstName', default=0)
    familyName = models.IntegerField(verbose_name='familyName', default=0)
    email = models.EmailField(verbose_name='email',)
    phoneNumber = models.IntegerField(verbose_name='phoneNumber', default=0)

    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 


class Payment(models.Model):
    slug = models.SlugField()

    companyCode = models.IntegerField(verbose_name='companyCode', default=0)
    companyName = models.IntegerField(verbose_name='companyName', default=0)
    country = models.IntegerField(verbose_name='country', default=0)
    zipCode = models.EmailField(verbose_name='zipCode',)
    accountType = models.IntegerField(verbose_name='accountType', default=0)

    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 
    
