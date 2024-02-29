from django.db import models
from django.utils import timezone

#企業情報リスト
class Company(models.Model):
    slug = models.SlugField()

    companyListNo = models.CharField(verbose_name='companyListNo',max_length=200,null=True,blank=True)
    companyName = models.CharField(verbose_name='companyName',max_length=200,null=True,blank=True)
    country = models.CharField(verbose_name='country',max_length=200,null=True,blank=True)
    zipCode = models.CharField(verbose_name='zipCode',max_length=200,null=True,blank=True)
    accountType = models.CharField(verbose_name='accountType',max_length=200,null=True,blank=True)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 


class Meta:
    verbose_name_plural = 'Accounts List'
    ordering = ('-date_added',)


#ユーザーリスト
class User(models.Model):
    slug = models.SlugField()

    userName = models.CharField(verbose_name='userName',max_length=200,null=True,blank=True)
    firstName = models.CharField(verbose_name='firstName',max_length=200,null=True,blank=True)
    familyName = models.CharField(verbose_name='familyName',max_length=200,null=True,blank=True)
    email = models.EmailField(verbose_name='email',)
    phoneNumber = models.CharField(verbose_name='phoneNumber',max_length=200,null=True,blank=True)

    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 


class Payment(models.Model):
    slug = models.SlugField()

    companyCode = models.CharField(verbose_name='companyCode',max_length=200,null=True,blank=True)
    companyName = models.CharField(verbose_name='companyName',max_length=200,null=True,blank=True)
    country = models.CharField(verbose_name='country',max_length=200,null=True,blank=True)
    zipCode = models.EmailField(verbose_name='zipCode',max_length=200,null=True,blank=True)
    accountType = models.CharField(verbose_name='accountType',max_length=200,null=True,blank=True)

    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 
    
