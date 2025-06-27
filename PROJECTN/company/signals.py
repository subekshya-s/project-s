from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee

@receiver(post_save,sender=Employee)
def after_employee_created(sender,instance,created,**kwargs):
    if created:
        printF("Namaste{instance.name},welcome to the company")