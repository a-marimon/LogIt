from datetime import timezone, datetime, timedelta, date
from sqlite3 import Date

from django.contrib import admin

from equipment.admin import EquipmentInline
from job.models import Job, JobType
from utils.CustomModelAdmin import CustomModelAdmin


class TimeLineFilter(admin.SimpleListFilter):
    title = 'Timeline'
    parameter_name = 'created_at'

    def lookups(self, request, model_admin):
        return (
            ('today', 'Today'),
            ('this_week', 'This Week'),
        )

    def queryset(self, request, qs):

        if self.value() == 'today':
            return qs.filter(created_at=Date.today())
        if self.value() == 'this_week':
            today = datetime.today()
            weekday = datetime.today().weekday()
            # days_to_subtract = weekday-1
            qs = qs.filter(created_at__range=(today - timedelta(days=weekday), today))

        return qs

# Register your models here.
class JobInline(admin.TabularInline):
    model = Job
    extra = 0
    fields = ['job_number', 'user', 'created_at']
    readonly_fields = ['created_at', 'user', 'job_number']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False



@admin.register(Job)
class JobAdmin(CustomModelAdmin):
    search_fields = ['job_number', 'address__address', 'user__username']
    list_filter = (TimeLineFilter,)
    list_display = (
        'job_number',
        'user',
        'created_at',
        'type',
        'time_frame',
        'address',
        'notes',
    )
    readonly_fields = ('user',)
    inlines = (EquipmentInline,)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user

        super().save_model(request, obj, form, change)

@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'compensation',
    )

