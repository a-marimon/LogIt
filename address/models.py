from django.db import models


# Create your models here.
class Address(models.Model):
    address = models.TextField()
    last_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.address