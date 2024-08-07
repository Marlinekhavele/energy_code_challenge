from django.contrib import admin
from .models import MeterPoint, Meter, Reading

# Register your models here.
admin.site.register(MeterPoint)
admin.site.register(Meter)
admin.site.register(Reading)
