from django.db import models

class EmpModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    salary = models.IntegerField()
    occupation = models.CharField(max_length=100)

    class Meta:
        db_table="employee"