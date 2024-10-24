from django.db import models
from django.db.models import Max, Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from accounts.models import CompanyCode, CompanyName, Plant
from ceList.models import Equipment, Machine


class BomList(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='bomList_companyCode', null=True, blank=True)
    bomCode = models.CharField(verbose_name='bomCode', max_length=50, blank=True, null=True)
    bomCost = models.DecimalField(verbose_name='bomCost', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    maxPartsDeliveryTimeInBom = models.IntegerField(verbose_name='maxPartsDeliveryTimeInBom', default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Bom List'
        verbose_name_plural = 'Bom List'
        ordering = ('bomCode',)

    def __str__(self):
        return f'{self.bomCode}'


class SpareParts(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='spareParts_companyCode', null=True, blank=True)
    companyName = models.CharField(verbose_name='companyName', max_length=200, blank=True, null=True)
    plant = models.CharField(verbose_name='plant', max_length=200, blank=True, null=True)
    equipment = models.CharField(verbose_name='equipment', max_length=200, blank=True, null=True)
    machineName = models.CharField(verbose_name='machineName', max_length=200, blank=True, null=True)
    partsNo = models.CharField(verbose_name='partsNo', max_length=20, blank=True, null=True, unique=True)
    image = models.ImageField(verbose_name='image', null=True, blank=True)
    bomCode = models.CharField(verbose_name='bomCode', max_length=100, blank=True, null=True)
    partsName = models.CharField(verbose_name='partsName', max_length=100, blank=True, null=True)
    partsModel = models.CharField(verbose_name='partsModel', max_length=50, blank=True, null=True)
    serialNumber = models.CharField(verbose_name='serialNumber', max_length=30, blank=True, null=True)
    category = models.CharField(verbose_name='category', max_length=50, blank=True, null=True)
    manufacturer = models.CharField(verbose_name='manufacturer', max_length=100, blank=True, null=True)
    partsCost = models.DecimalField(verbose_name='partsCost', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    numberOf = models.PositiveIntegerField(verbose_name='numberOf', blank=True, null=True, default=0)
    summedPartsCost = models.DecimalField(verbose_name='summedPartsCost', max_digits=10, decimal_places=2, blank=True, null=True, default=0.000)
    unit = models.CharField(verbose_name='unit', max_length=20, blank=True, null=True)
    taskListNo = models.CharField(verbose_name='taskListNo', max_length=20, blank=True, null=True)
    location = models.CharField(verbose_name='location', max_length=200, blank=True, null=True)
    stock = models.CharField(verbose_name='stock', max_length=200, null=True, blank=True)
    partsDeliveryTime = models.PositiveIntegerField(verbose_name='partsDeliveryTime', blank=True, null=True, default=0)
    orderAlert = models.CharField(verbose_name='orderAlert', max_length=20, blank=True, null=True)
    orderSituation = models.BooleanField(verbose_name='orderSituation', default=False)
    classification = models.CharField(verbose_name='classification', max_length=100, blank=True, null=True)
    partsDescription = models.TextField(verbose_name='partsDescription', max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Spare Parts List'
        verbose_name_plural = 'Spare Parts List'
        ordering = ('partsName',)

    def __str__(self):
        return f'{self.partsName}'

    def save(self, *args, **kwargs):
        if not self.partsNo:  # partsNoが指定されていない場合、自動生成
            max_parts_no = SpareParts.objects.aggregate(Max('partsNo'))['partsNo__max']
            if max_parts_no:
                self.partsNo = str(int(max_parts_no) + 1).zfill(5)  # 5桁のゼロ埋めで次の番号を設定
            else:
                self.partsNo = '00001'  # 最初のレコードの場合、'00001'から開始
        super(SpareParts, self).save(*args, **kwargs)




class SparePartsManagement(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='sparePartsManagement_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='sparePartsManagement_companyName', null=True, blank=True)
    plant = models.CharField(verbose_name='plant', max_length=200, blank=True, null=True)  # CharFieldに変更
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='sparePartsManagement_equipment', null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='sparePartsManagement_machineName', null=True, blank=True)
    totalSparePartsCost = models.DecimalField(verbose_name='totalSparePartsCost', max_digits=10, decimal_places=2, blank=True, null=True, default=0.000)
    inventoryTurnover = models.CharField(verbose_name='inventoryTurnover', max_length=30, blank=True, null=True)


    class Meta:
        verbose_name = 'Spare Parts Management'
        verbose_name_plural = 'Spare Parts Management'
        ordering = ('companyCode',)

    def __str__(self):
        return f'{self.companyCode}'



@receiver(post_save, sender=SpareParts)
def update_total_spare_parts_cost(sender, instance, **kwargs):
    if instance.companyCode and instance.plant:
        # フィルタリング条件の詳細ログを出力
        print(f"Updating total spare parts cost for companyCode: {instance.companyCode} and plant: {instance.plant}")

        # 関連する SpareParts を取得し、デバッグ出力
        related_spare_parts = SpareParts.objects.filter(
            companyCode=instance.companyCode,
            plant=instance.plant
        )
        
        # 取得したレコードの詳細を出力
        print(f"Found {related_spare_parts.count()} spare parts for companyCode: {instance.companyCode}, plant: {instance.plant}")
        
        for part in related_spare_parts:
            print(f"Part: {part.partsName}, Summed Cost: {part.summedPartsCost}")

        # 合計コストを計算し、詳細ログを出力
        total_cost = related_spare_parts.aggregate(Sum('summedPartsCost'))['summedPartsCost__sum'] or 0
        print(f"Calculated total cost: {total_cost} for plant: {instance.plant}")

        # SparePartsManagement を取得または作成し、デバッグ出力
        spare_parts_management, created = SparePartsManagement.objects.get_or_create(
            companyCode=instance.companyCode,
            plant=instance.plant,
            defaults={'totalSparePartsCost': total_cost}
        )
        print(f"SparePartsManagement {'created' if created else 'found'} for companyCode: {instance.companyCode}, plant: {instance.plant}")

        # 既存の場合は更新し、デバッグ出力
        if not created:
            print(f"Updating SparePartsManagement: {spare_parts_management} with new total cost: {total_cost}")
            spare_parts_management.totalSparePartsCost = total_cost
            spare_parts_management.save()
            print(f"Updated total cost in SparePartsManagement: {spare_parts_management.totalSparePartsCost}")
        else:
            print(f"Created new SparePartsManagement with total cost: {spare_parts_management.totalSparePartsCost}")