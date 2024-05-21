from django.contrib import admin
from ingest.models import FileModel

@admin.register(FileModel)
class FileModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'created_date')  # fields to display in the admin panel
