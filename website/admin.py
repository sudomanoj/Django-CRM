from django.contrib import admin
from website.models import Record
# Register your models here.

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass

# or admin.site.register(Record)