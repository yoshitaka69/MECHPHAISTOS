from django.db import models
from accounts.models import CompanyCode, CompanyName,Plant


class WorkOrder(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workOrder_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='workOrder_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='workOrder_plant', null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)

    workOrderNo  = models.CharField(max_length=100, null=True, blank=True)
    workOrderDesc = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    

    class Meta:
        verbose_name_plural = 'Work Order'
        ordering = ('companyCode',)
    def __str__(self):
        return str('work order')
    


class WorkPermission(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workPermission_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='workPermission_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='workPermission_plant', null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)

    workOrderNo = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='workPermission_workOrder', null=True, blank=True)
    workPermissionNo = models.CharField(max_length=100, null=True, blank=True)
    workPermissionDesc = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Work Permission'
        ordering = ('workOrderNo',)
    def __str__(self):
        return str('work permission')




class WorkOrderManagement(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workOrderManagement_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='workOrderManagement_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='workOrderManagement_plant', null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Work Order Management'
        ordering = ('companyCode',)
    def __str__(self):
        return str('Work Order Management')
