from django.apps import AppConfig


class ComapnyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'company'

def ready(self):
     import company.signals