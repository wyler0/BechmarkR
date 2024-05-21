from django.urls import path
from .views import IngestPDFView  # assuming you have an 'IngestPDFView' in your views.py

urlpatterns = [
    path('ingest_pdf/', IngestPDFView.as_view(), name='ingestpdf'),
]

