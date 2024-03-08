from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin,)
from django.db import models
from django.utils import timezone


#admin用
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


#payment方法
#class Payment(models.Model):
    #slug = models.SlugField()
    #freeUser = models.BooleanField(default=False)
    #lightUser = models.BooleanField(default=False)
    #middleUser = models.BooleanField(default=False)
    #specialUser = models.BooleanField(default=False)
    #premiumUser = models.BooleanField(default=False)


#企業情報リスト
class Company(models.Model):
    slug = models.SlugField()

    companyCode = models.CharField(verbose_name='companyCode',max_length=200,null=True,blank=True)

    companyListNo = models.CharField(verbose_name='companyListNo',max_length=200,null=True,blank=True)
    companyName = models.CharField(verbose_name='companyName',max_length=200,null=True,blank=True)
    country = models.CharField(verbose_name='country',max_length=200,null=True,blank=True)
    zipCode = models.CharField(verbose_name='zipCode',max_length=200,null=True,blank=True)
    payment = models.CharField(verbose_name='payment',max_length=200,null=True,blank=True)
    communityGroup = models.CharField(verbose_name='communityGroup',max_length=200,null=True,blank=True)
    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name_plural = 'Company List'
        ordering = ('-createdDay',)
    
    def __str__(self):
        return self.companyName

class CustomUser(AbstractBaseUser, PermissionsMixin):

    firstName = models.CharField(verbose_name='firstName',max_length=200,null=True,blank=True)
    familyName = models.CharField(verbose_name='familyName',max_length=200,null=True,blank=True)

    userName = models.CharField(verbose_name='userName',max_length=200,null=True,blank=True)

    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(verbose_name='phoneNumber',max_length=200,null=True,blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    companyName = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='view_companyName',null=True, blank=True)
    payment = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='view_payment',null=True, blank=True)
    communityGroup = models.CharField(verbose_name='communityGroup',max_length=200,null=True,blank=True)
    
    createdDay = models.DateTimeField(verbose_name='createdDay',default=timezone.now) 
    updateDay = models.DateTimeField(verbose_name='updateDay',default=timezone.now) 

    objects = CustomUserManager()
    USERNAME_FIELD = "email"


    class Meta:
        verbose_name_plural = 'User List'
        ordering = ('-createdDay',)
    
    def __str__(self):
        return self.userName


