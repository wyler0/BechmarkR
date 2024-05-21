from django.urls import path
from .views import GenerationView  # assuming you have an 'IngestPDFView' in your views.py

urlpatterns = [
    path('generate-submission/', GenerationView.as_view(), name='generate'),
]

