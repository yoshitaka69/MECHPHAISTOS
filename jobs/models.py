from django.db import models

# Create your models here.


class JobOffer(models.Model):

    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_tittle = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.PositiveBigIntegerField()
    prefecture = models.CharField(max_length=100)
    city = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.company_name

