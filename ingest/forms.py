from django import forms

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField()
    
    def clean(self):
        cleaned_data = super(PDFUploadForm, self).clean()

        pdf_file = cleaned_data.get('pdf_file', None)
        if not pdf_file:
            raise forms.ValidationError("No file was uploaded.")
        
        if not pdf_file.content_type == 'application/pdf':
            raise forms.ValidationError("Only .pdf files are allowed.")

    