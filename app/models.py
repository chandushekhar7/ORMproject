from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.AutoField(primary_key = True)
    ename = models.CharField(max_length = 30)
    eaddr = models.CharField(max_length = 30)
    esalary = models.IntegerField()

    def __str__(self):
        return self.ename

    class Meta:
        db_table = 'Employee_Details'
        managed = True
