from django.db import models
from datetime import date
#create custommanager 
class EmployeeManager(models.Manager):
    def active(self):#costume method inside manager
        return self.filter(is_active=True)# says to go to the database and filter all employee record where is-active=True


# Create your models here.
class Company(models.Model):
    Company_name=models.CharField(max_length=70)
    location=models.CharField(max_length=100)
    established_year=models.PositiveIntegerField()
     

    def __str__(self):
        return self.Company_name

    @property
    def age(self):
        return date.today(). year - self.established_year

class Employee(models.Model):
    name=models.CharField(max_length=70) 
    position=models.CharField(max_length=80)
    Company=models.ForeignKey(Company,on_delete=models.CASCADE)#connecting it with the company model whwre cascade means it will delete all the list of the employee when company is deleted
    joined_at=models.DateField() 
    objects =EmployeeManager()

    @property
    def experienced_year(self):
         return date.today().year-self.joined_at.year

    def __str__(self):
         return self.name