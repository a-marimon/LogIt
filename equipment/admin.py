from django.contrib import admin

from equipment.models import Equipment
from utils.CustomModelAdmin import CustomModelAdmin


# Register your models here.
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ('identifier', )
    list_display = ('identifier',  'type', 'is_return', 'job',)
    list_filter = ('is_return',)


class EquipmentInline(admin.TabularInline):
    model = Equipment
    extra = 0