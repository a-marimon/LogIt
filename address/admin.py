from django.contrib import admin

from address.models import Address
from job.admin import JobInline
from utils.CustomModelAdmin import CustomModelAdmin


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ['address']

    list_display = ('address', 'last_update',)
    readonly_fields = ('last_update',)
    inlines = (JobInline,)

    def has_delete_permission(self, request, obj = ...):
        return False

    def has_change_permission(self, request, obj = ...):
        return False

