from django.contrib import admin
from .models import HitCount, AllRecords


class HitCountAdmin(admin.ModelAdmin):
	list_display = ('url', 'hits')


class AllRecordsAdmin(admin.ModelAdmin):
	list_display = ('created', 'url', 'ip', 'browser', 'os', 'device', 'count')

admin.site.register(HitCount, HitCountAdmin)
admin.site.register(AllRecords, AllRecordsAdmin)
