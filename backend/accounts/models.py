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
class UserInfo(models.Model):
    slug = models.SlugField()

    userName = models.CharField(verbose_name='userName',max_length=200,null=True,blank=True)
    firstName = models.CharField(verbose_name='firstName',max_length=200,null=True,blank=True)
    familyName = models.CharField(verbose_name='familyName',max_length=200,null=True,blank=True)
    email = models.EmailField(verbose_name='email',)
    phoneNumber = models.CharField(verbose_name='phoneNumber',max_length=200,null=True,blank=True)

    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 


#payment方法
class Payment(models.Model):
    slug = models.SlugField()

    companyCode = models.CharField(verbose_name='companyCode',max_length=200,null=True,blank=True)
    companyName = models.CharField(verbose_name='companyName',max_length=200,null=True,blank=True)
    country = models.CharField(verbose_name='country',max_length=200,null=True,blank=True)
    zipCode = models.EmailField(verbose_name='zipCode',max_length=200,null=True,blank=True)
    accountType = models.CharField(verbose_name='accountType',max_length=200,null=True,blank=True)

    createdDay = models.DateTimeField(auto_now_add=True) 
    updateDay = models.DateTimeField(auto_now_add=True) 



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True)
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"


