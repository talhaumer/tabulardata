from django.db import models

# Create your models here.

# class Expense(models.Model):
#     amount = models.FloatField()
#     payable_date = models.DateField()
#     month_and_year = models.DateField()
#     payable_to = models.CharField(max_length=30)
#     status = models.IntegerField(default=1)
#     created_at = models.DateField(auto_now=True)
#     updated_at = models.DateField(auto_now_add=True)
#
#     class Meta:
#         db_table = "Expense"


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'Person'
