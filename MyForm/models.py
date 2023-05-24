from django.db import models

# Create your models here.
class MyForm(models.Model) :
    name = models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=60)