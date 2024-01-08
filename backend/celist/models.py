from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models



class Company(models.Model):
   company_name = models.CharField(max_length=255)
   company_code = models.CharField(max_length=100)
   slug = models.SlugField()

   class Meta:
      ordering = ('company_name',)


   def __str__(self):
     return self.company_name

   def get_absolute_url(self):
      return f'/{self.slug}/'



class CeList(models.Model):
    company = models.ForeignKey(Company, related_name='celist', on_delete=models.CASCADE)

    company_code = models.CharField(max_length=100)
    slug = models.SlugField()


    plant = models.CharField(verbose_name='プラント名', max_length=200)
    equipment = models.CharField(verbose_name='設備名称', max_length=200)
    function = models.CharField(verbose_name='機能場所', max_length=200)
    setting_value_impact = models.CharField(verbose_name='impactへの設定値', max_length=200)
    construction_period = models.CharField(verbose_name='工期', max_length=200)
    parts_deliver_date = models.CharField(verbose_name='部品納期', max_length=200)
    mttr = models.CharField(verbose_name='MTTR', max_length=200)


    number_pm02 = models.CharField(verbose_name='PM02回数', max_length=200,blank=True, null=True)
    latest_pm02 = models.CharField(verbose_name='直近のPM02', max_length=200,blank=True, null=True)
    number_pm03 = models.CharField(verbose_name='PM03回数', max_length=200,blank=True, null=True)
    latest_pm03 = models.CharField(verbose_name='直剣のPM03', max_length=200,blank=True, null=True)
    number_pm04 = models.CharField(verbose_name='PM04回数', max_length=200,blank=True, null=True)
    latest_pm04 = models.CharField(verbose_name='直近のPM04', max_length=200,blank=True, null=True)


    impact_production = models.CharField(verbose_name='生産へのimpact', max_length=200)
    possibility_of_failure = models.CharField(verbose_name='故障の可能性', max_length=200)
    assessment = models.CharField(verbose_name='評価', max_length=200)


    task_pm02 = models.CharField(verbose_name='PM02タスク名称', max_length=200)
    cost_of_task = models.CharField(verbose_name='推定コスト', max_length=200)
    period_of_task = models.CharField(verbose_name='周期', max_length=200)
    next_event = models.CharField(verbose_name='次回の発生日', max_length=200)
    situation_for_pm02 = models.CharField(verbose_name='周期超過の有無', max_length=200)


    """test用でimage挿入"""
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)


    """記入した日付を記入してくれる"""
    date_added = models.DateTimeField(auto_now_add=True)



class Meta:
    verbose_name_plural = 'Critical Equipment'
    ordering = ('-date_added',)

def __str__(self):
    return self.company_name

#一旦コメントアウト　companyには2つの項目がある。20240108 y.noto
#def get_absolute_url(self):
    #return f'/{self.company.slug}/{self.slug}/'

def get_image(self):
   if self.image:
      return 'http://127.0.0.1:8000' + self.image.url
   return ''

def get_thumbnail(self):
   if self.thumbnail:
      return 'http://127.0.0.1:8000' + self.thumbnail.url
   else:
      if self.image:
         self.thumbnail = self.make_thumbnail(self.image)
         self.save()

         return 'http://127.0.0.1:8000' + self.thumbnail.url
      else:
         return ''
    
def make_thumbnail(self, image, size=(300,200)):
   img = Image.open(image)
   img.convert('RGB')
   img.thumbnail(size)


   thumb_io = BytesIO()
   img.save(thumb_io, 'JPEG', quality=85)

   thumbnail = File(thumb_io, name=image.name)

   return thumbnail