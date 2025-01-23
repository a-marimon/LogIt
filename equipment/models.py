from django.db import models


# Create your models here.
class EquipmentTypeChoices(models.TextChoices):
    COAX_MODEM = "COAX MODEM"
    FIBER_MODEM = "FIBER MODEM"
    ROUTER_6 = "ROUTER 6"
    ROUTER_6E = "ROUTER 6E"
    ROUTER_7 = "ROUTER 7"
    WIB = "WIB"
    HD = 'HD'
    DVR = 'DVR'
    XUMO = 'XUMO'


class Equipment(models.Model):
    type = models.CharField(max_length=100, choices=EquipmentTypeChoices.choices, null=True, blank=False)
    identifier = models.CharField(max_length=100, unique=True)
    is_return = models.BooleanField(default=False)
    job = models.ForeignKey(
        "job.Job",
        on_delete=models.CASCADE,
        related_name='equipments',
    )

    def __str__(self):
        return self.identifier
