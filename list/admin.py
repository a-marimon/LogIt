from django.contrib import admin

from list.models import List, ListItem
from utils.CustomModelAdmin import CustomModelAdmin


class ListItemInline(admin.TabularInline):
    model = ListItem
    extra = 0

@admin.register(List)
class ListAdmin(CustomModelAdmin):
    list_display = ('title', 'is_checklist', 'user__username')
    readonly_fields = ('user',)
    inlines = (ListItemInline, )





