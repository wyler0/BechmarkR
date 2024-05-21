from django.db import models

class FileModel(models.Model):
    id = models.AutoField(primary_key=True)  # Unique identifier (Primary Key)
    created_date = models.DateTimeField(auto_now_add=True)  # Created date and time
    file_name = models.CharField(max_length=256)  # String for the file name
