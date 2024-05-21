from django.shortcuts import render, redirect
from django.views import View

from ingest.forms import PDFUploadForm
from ingest.tasks import handle_pdf_upload

class IngestPDFView(View):
    def get(self, request):
        form = PDFUploadForm()
        return render(request, 'pdf_upload.html', {'form': form})  
    
    def post(self, request):
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            
            # Call the async task to handle the uploaded PDF file
            handle_pdf_upload.delay(pdf_file.name)
        
            #return render(request, 'success.html')  # Replace with your success page
            return redirect('success')  # Redirect to success URL or view name
        else:
            return render(request, 'pdf_upload.html', {'form': form})
