from django.db import models
from django.utils import timezone
from accounts.models import CompanyCode,CompanyName,Plant
from ceList.models import Equipment,Machine

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum


class BomList(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='bomList_companyCode', null=True, blank=True)
    bomCode = models.CharField(verbose_name='bomCode', max_length=50,blank=True,null=True)
    bomCost = models.DecimalField(verbose_name='bomCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    maxPartsDeliveryTimeInBom = models.IntegerField(verbose_name='maxPartsDeliveryTimeInBom', default=0, null=True, blank=True)
     
    class Meta:
        verbose_name = 'Bom List'
        verbose_name_plural = 'Bom List'
        ordering = ('bomCode',) 

    def __str__(self):
        return f'{self.bomCode}'





class SpareParts(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='spareParts_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='spareParts_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='spareParts_plant', null=True, blank=True)

    #CeListより
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='spareParts_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='spareParts_machineName',null=True, blank=True)

    partsNo = models.CharField(verbose_name='partsNo', max_length=20,blank=True,null=True)

    #画像
    image = models.ImageField(verbose_name='image',null=True,blank=True)

    #parts 基本情報
    bomCode = models.ForeignKey(BomList, on_delete=models.CASCADE, related_name='spareParts_bomCode', null=True, blank=True)

    partsName = models.CharField(verbose_name='partsName', max_length=100,blank=True,null=True)
    partsModel = models.CharField(verbose_name='partsModel',max_length=50,blank=True,null=True)
    serialNumber = models.CharField(verbose_name='serialNumber',max_length=30,blank=True,null=True)
    category = models.CharField(verbose_name='category',max_length=50,blank=True,null=True)

    #部品コスト
    partsCost = models.DecimalField(verbose_name='partsCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    numberOf = models.PositiveIntegerField(verbose_name='numberOf', blank=True,null=True,default=0)
    summedPartsCost = models.DecimalField(verbose_name='summedPartsCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.000)
    unit = models.CharField(verbose_name='unit',max_length=20,blank=True,null=True)

    taskCode = models.CharField(verbose_name='taskCode', max_length=20,blank=True,null=True)

    #物理的な状況
    location = models.CharField(verbose_name='location',max_length=200,blank=True,null=True)
    stock = models.CharField(verbose_name='stock', max_length=200,null=True,blank=True)
    partsDeliveryTime = models.PositiveIntegerField(verbose_name='partsDeliveryTime', blank=True,null=True,default=0)
    orderAlert = models.CharField(verbose_name='order',max_length=20,blank=True,null=True)
    orderSituation = models.BooleanField(verbose_name='orderSituation', default=False)

    #部品の説明
    classification = models.CharField(verbose_name='classification',max_length=100,blank=True,null=True)
    
    partsDescription = models.TextField(verbose_name='partsDescription',max_length=1000,blank=True,null=True,)



    def save(self, *args, **kwargs):
        # partsNoが未設定の場合、新しいpartsNoを生成
        if not self.partsNo:
            last_part = SpareParts.objects.order_by('partsNo').last()
            self.partsNo = f"{int(last_part.partsNo) + 1:05d}" if last_part else '0001'

        # partsCostとnumberOfが設定されていればsummedPartsCostを計算
        if self.partsCost is not None and self.numberOf is not None:
            self.summedPartsCost = self.partsCost * self.numberOf

        # ベースクラスのsaveメソッドを呼び出して、変更をデータベースに保存
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Spare Parts List'
        verbose_name_plural = 'Spare Parts List'
        ordering = ('partsName',)

    def __str__(self):
        return f'{self.partsName}'


   


class SparePartsManagement(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='sparePartsManagement_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='sparePartsManagement_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='sparePartsManagement_plant', null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='sparePartsManagement_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='sparePartsManagement_machineName',null=True, blank=True)

    totalSparePartsCost = models.DecimalField(verbose_name='totalSparePartsCost',max_digits=10,decimal_places=2,blank=True,null=True,default=0.000)
    inventoryTurnover = models.CharField(verbose_name='inventoryTurnover',max_length=30,blank=True,null=True)

    class Meta:
        verbose_name = 'Spare Parts Management'
        verbose_name_plural = 'Spare Parts Management'
        ordering = ('companyCode',) 

    def __str__(self):
        return f'{self.companyCode}'
    

    @receiver(post_save, sender=SpareParts)
    def update_total_spare_parts_cost(sender, instance, **kwargs):
        # SpareParts が保存されたときに関連する SparePartsManagement の totalSparePartsCost を更新
        if instance.companyCode and instance.plant:
            # companyCode と plant でフィルタリング
            related_spare_parts = SpareParts.objects.filter(
                companyCode=instance.companyCode,
                plant=instance.plant
            )
            total_cost = related_spare_parts.aggregate(Sum('summedPartsCost'))['summedPartsCost__sum'] or 0

            # Debug output
            print(f"Total cost calculated: {total_cost} for companyCode: {instance.companyCode} and plant: {instance.plant}")

            # 対応する SparePartsManagement を取得または作成
            spare_parts_management, created = SparePartsManagement.objects.get_or_create(
                companyCode=instance.companyCode,
                plant=instance.plant,
                defaults={'totalSparePartsCost': total_cost}
            )

            # 既存の場合は更新
            if not created:
                spare_parts_management.totalSparePartsCost = total_cost
                spare_parts_management.save()

            # Debug output for created or updated instance
            print(f"Spare Parts Management {('created' if created else 'updated')} with total cost: {spare_parts_management.totalSparePartsCost}")