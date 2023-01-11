from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=100)  # ООО "Газпром энерго"
    branch_name = models.CharField(max_length=100)  # ИТЦ
    department_name = models.CharField(max_length=100)  # ОСЭиРЛИУС
    full_adress = models.CharField(max_length=100)

