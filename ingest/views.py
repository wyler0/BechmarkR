import os

from django.shortcuts import render, redirect
from django.views import View

from ingest.forms import PDFUploadForm
from ingest.tasks import handle_pdf_upload


uploads_dir = "data/uploads"
outputs_dir = "data/ingestion_outputs"

if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

if not os.path.exists(outputs_dir):
    os.makedirs(outputs_dir)
    
class IngestPDFView(View):
    def get(self, request):
        form = PDFUploadForm()
        return render(request, 'pdf_upload.html', {'form': form})  
    
    def post(self, request):
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            file_path = f"{uploads_dir}/{pdf_file.name}"
            with open(file_path, "wb") as f:
                for chunk in pdf_file.chunks():
                    f.write(chunk)
            
            
            # Call the async task to handle the uploaded PDF file
            task = handle_pdf_upload.delay(file_path)
        
            #return render(request, 'success.html')  # Replace with your success page
            flower_url = "http://localhost:5555/task/%s" % task.id
            return render(request, 'success.html', {"task_url": flower_url})  # Redirect to success URL or view name
        else:
            return render(request, 'pdf_upload.html', {'form': form})
