from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

from address.models import Address


# CHOICES TABLES
# class JobTypeChoices(models.IntegerChoices):
#     NC_SINGLE = 1
#     NC_DOUBLE = 2
#     NC_TRIPLE = 3
#     RC_SINGLE = 4
#     RC_DOUBLE = 5
#     RC_TRIPLE = 6
#     RES_SINGLE = 7
#     RES_DOUBLE = 8
#     RES_TRIPLE = 9
#     TROUBLE_CALL = 10
#     DOWN_DROP = 11
#     SB_NC_SINGLE = 12
#     SB_NC_DOUBLE = 13
#     SB_NC_TRIPLE = 14
#     SB_RC_SINGLE = 15
#     SB_RC_DOUBLE = 16
#     SB_RC_TRIPLE = 17


class JobType(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    compensation = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.title


class Job(models.Model):
    # Keeping TimeFrameChoices old version do to the new version format does not support using numeric labels
    TimeFrameChoices = [
        ('8-9AM', '8:00 AM - 9:00 AM'),
        ('9-10AM', '9:00 AM - 10:00 AM'),
        ('10-11AM', '10:00 AM - 11:00 AM'),
        ('11AM-12PM', '11:00 AM - 12:00 PM'),
        ('12-1PM', '12:00 PM - 1:00 PM'),
        ('1-2PM', '1:00 PM - 2:00 PM'),
        ('2-3PM', '2:00 PM - 3:00 PM'),
        ('3-4PM', '3:00 PM - 4:00 PM'),
        ('4-5PM', '4:00 PM - 5:00 PM'),
        ('5-6PM', '5:00 PM - 6:00 PM'),
        ('6-7PM', '6:00 PM - 7:00 PM'),
        ('7-8PM', '7:00 PM - 8:00 PM'),
        ('8-9PM', '8:00 PM - 9:00 PM'),
    ]

    job_number = models.CharField(unique=True, max_length=10, null=False, blank=False)
    type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    time_frame = models.CharField(
        max_length=100,
        choices=TimeFrameChoices,
        default='0',
        null=True,
        blank=True
    )
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='jobs'
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        null=True,
        related_name='job',
    )

    def __str__(self):
        return self.job_number