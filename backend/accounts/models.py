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
class Payment(models.Model):
    #ここは表に出てこないので、slugは不要
    #slug = models.SlugField()
    paymentType = models.CharField(verbose_name='paymentType',max_length=20,null=True,blank=True)
    description = models.TextField(verbose_name='description',max_length=500,null=True,blank=True)

    class Meta:
        verbose_name = 'Payment List'
        verbose_name_plural = 'Payment List'
        ordering = ('-paymentType',)
    
    def __str__(self):
        return self.paymentType


#企業情報リスト
class Company(models.Model):
    #slug = models.SlugField(null=True,blank=True)

    companyCode = models.CharField(verbose_name='companyCode',max_length=200,null=True,blank=True)

    companyListNo = models.CharField(verbose_name='companyListNo',max_length=200,null=True,blank=True)
    companyName = models.CharField(verbose_name='companyName',max_length=200,null=True,blank=True)
    country = models.CharField(verbose_name='country',max_length=200,null=True,blank=True)
    zipCode = models.CharField(verbose_name='zipCode',max_length=200,null=True,blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='company_payment',null=True, blank=True)
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
    companyName = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='customUser_companyName',null=True, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='customUser_payment',null=True, blank=True)
    communityGroup = models.CharField(verbose_name='communityGroup',max_length=200,null=True,blank=True)
    
    createdDay = models.DateTimeField(verbose_name='createdDay',default=timezone.now) 
    updateDay = models.DateTimeField(verbose_name='updateDay',default=timezone.now) 

    objects = CustomUserManager()
    USERNAME_FIELD = "email"


    class Meta:
        verbose_name_plural = 'User List'
        ordering = ('-createdDay',)

    def save(self, *args, **kwargs):
        # userNameが空の場合、firstNameとfamilyNameを組み合わせる
        if not self.userName:
            self.userName = f'{self.firstName} {self.familyName}'.strip()
        super(CustomUser, self).save(*args, **kwargs)

    #def __str__(self):
        #return self.userName


