
from operator import mod
from django.db import models
# Create your models here.


class Address(models.Model):
    name = models.CharField(max_length=80, blank=False)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=200, default="No address given")
    postcode = models.CharField(max_length=25, default="00000")

    class Meta:
        verbose_name = "address book"
        verbose_name_plural = "Address's"
        db_table = 'address_book'

    def __str__(self):
        return f"Address for {self.name}"

