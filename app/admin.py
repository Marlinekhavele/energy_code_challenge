from django.contrib import admin
from .models import MeterPoint, Meter, Reading

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('meter', 'value', 'date', 'flow_file')
    search_fields = ('meter__meter_point__mpan', 'meter__serial_number')
    list_filter = ('date',)

admin.site.register(MeterPoint)
admin.site.register(Meter)