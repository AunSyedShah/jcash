from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(default=0, max_length=11)
    balance = models.FloatField(default=0)
    image = models.ImageField(upload_to='account_images/', default='images/default.png')

    def __str__(self):
        return self.account_number
