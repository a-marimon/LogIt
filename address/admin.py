from django.contrib import admin

from address.models import Address
from job.admin import JobInline
from utils.CustomModelAdmin import CustomModelAdmin


# Register your models here.
@admin.register(Address)
class AddressAdmin(CustomModelAdmin):
    search_fields = ['address']

    list_display = ('address', 'last_update',)
    inlines = (JobInline,)


