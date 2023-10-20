from django.db import models

class CeList(models.Model):
    book_name = models.CharField(verbose_name='本の名前', max_length=200)
    author = models.CharField(verbose_name='作者', max_length=200)
    publisher = models.CharField(verbose_name='出版社', max_length=200)
    price = models.CharField(verbose_name='価格', max_length=200)

class Meta:
    verbose_name_plural = 'Critical Equipment'

    def __str__(self):
     return self.book_name


