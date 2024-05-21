from django.db import models

file_model_status_choices = (
    ('0', 'Processing'),
    ('1', 'Complete'),
    ('2', 'Failed'),
)

class FileModel(models.Model):
    id = models.AutoField(primary_key=True)  # Unique identifier (Primary Key)
    created_date = models.DateTimeField(auto_now_add=True)  # Created date and time
    file_name = models.CharField(max_length=250)  # String for the file name
    file_path = models.CharField(max_length=250)  # String for the file path
    tesseract_text = models.TextField(null=True)  # Text extracted from Tesseract
    status = models.IntegerField(choices=file_model_status_choices, default=0)  # Status of the file processing
    error = models.CharField(max_length=250, null=True)  # Error message if processing failed
