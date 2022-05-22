from django.core.validators import RegexValidator
from django.db import models


class OrderDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phoneNumberRegex],
                             max_length=16, unique=True)
    comment = models.TextField(blank=True)

