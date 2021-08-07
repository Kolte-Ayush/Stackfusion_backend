from django.db import models


# Create your models here.

class UserForm(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    email = models.EmailField()
    mobile_Number = models.CharField(max_length=15)

    class Meta:
        db_table = "User-form"
