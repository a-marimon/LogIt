from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

class List(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    is_checklist = models.BooleanField(default=False)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lists',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

class ListItem(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    item = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.item

