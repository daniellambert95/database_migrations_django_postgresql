
from django.db import models
# Create your models here.


class Address(models.Model):
    name = models.CharField(max_length=80, blank=False)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=200,  blank=False)

    class Meta:
        verbose_name = "address book"
        verbose_name_plural = "Address's"
        db_table = 'address_book'

    def __str__(self):
        return f"Address for {self.name}"

