from django.contrib import admin
from .models import MeterPoint, Meter, Reading

@admin.register(MeterPoint)
class MeterPointAdmin(admin.ModelAdmin):
    search_fields = ['mpan']

@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    search_fields = ['serial_number']

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('meter', 'value', 'date', 'filename')
    list_filter = ('date',)