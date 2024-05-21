# tasks.py
from celery import shared_task
from .models import FileModel

@shared_task
def handle_pdf_upload(file_name):
    """ Handle the PDF upload by saving the file name to the database and beginning file processing."""
    new_file = FileModel(file_name=file_name)
    new_file.save()

