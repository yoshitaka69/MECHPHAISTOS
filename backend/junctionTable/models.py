from django.db import models
from spareParts.models import SpareParts
from taskList.models import TaskList

class TaskList(models.Model):
    taskCode = models.CharField(verbose_name='taskCode', max_length=200, blank=True, null=True)

class SpareParts(models.Model):
    bomCode = models.ManyToManyField(TaskList, through='JunctionTable')

class JunctionTable(models.Model):
    slug = models.SlugField()
    
    taskCode = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    taskCost = models.DecimalField(verbose_name='taskCost', max_digits=5, decimal_places=2, blank=True, null=True, default=0.00)
    bomCode = models.ForeignKey(SpareParts, on_delete=models.CASCADE, related_name="spare_parts", null=True, blank=True)
    bomCost = models.DecimalField(verbose_name='bomCost', max_digits=5, decimal_places=2, blank=True, null=True, default=0.00)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=5, decimal_places=2, blank=True, null=True, default=0.00)

    class Meta:
        verbose_name = 'Junction Table'
        verbose_name_plural = 'Junction Tables'
        unique_together = ('taskCode', 'bomCode')
        
    #taskCode および bomCode フィールドが null と blank であることを許容し、それらが提供されない場合は "N/A" を表示する
    def __str__(self):
        return f'{self.taskCode.taskCode if self.taskCode else "N/A"} - {self.bomCode.bomCode if self.bomCode else "N/A"}'

