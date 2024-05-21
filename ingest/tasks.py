import os

from celery import shared_task

import nougat
import pytesseract
from pdf2image import convert_from_path


from ingest.models import FileModel


@shared_task
def handle_pdf_upload(file_path: str):
    """ Handle the PDF upload by saving the file name to the database and beginning file processing."""
    # Create the model entry
    # get filename from file path using os.path library
    _, file_name = os.path.split(file_path)
    file_model_instance = FileModel(file_name=file_name.split('.')[:-1], file_path=file_path, status=0)
    file_model_instance.save()
    
    try:
        # Process with Tesseract
        tesseract_results = process_tesseract(file_path)
        file_model_instance.tesseract_text = '\n****NEW PAGE****\n'.join(tesseract_results)
        file_model_instance.save()

        # Process with Nougat
        # process_nougat(file_name)
        
    except Exception as e:
        file_model_instance.error = str(e)
        file_model_instance.status = 2
        file_model_instance.save()
        return "error"
    
    file_model_instance.status = 1
    file_model_instance.save()
    return "success"
    
def process_tesseract(file_path) -> list[str]:
    """ Given a PDF file, extract images of each page then pipe through tesseract for OCR.
    
    Returns:
        list[str]: A list of strings representing the text extracted for each page.
    """
    # Convert to Images
    images = convert_from_path(file_path)
    
    # Extract text from each image
    tesseract_results = []
    for i, img in enumerate(images):
        text = pytesseract.image_to_string(img)  # Applying OCR on image
        tesseract_results.append(text)
        print(f"Page {i+1}: {text}")
    
    # Return the list of text
    return tesseract_results
    
    
def process_nougat(file_name):
    raise NotImplementedError("This function is not yet implemented")

    

