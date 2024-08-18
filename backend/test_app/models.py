from django.db import models
from django.db.models import Max, Q

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    testNo = models.PositiveIntegerField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if self.testNo is None:  # testNoが設定されていない場合
            max_test_no = Product.objects.aggregate(Max('testNo'))['testNo__max']
            if max_test_no is not None:
                self.testNo = max_test_no + 1
            else:
                self.testNo = 1  # 最初のtestNoを1に設定
        super().save(*args, **kwargs)


