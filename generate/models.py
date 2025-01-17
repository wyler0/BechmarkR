from django.db import models
from ingest.models import FileModel

generate_execution_types = (
    ('MCQ', 'Multiple Choice Questions'),
    ('FRQ', 'Free Response Questions'),
)

class GenerateExecutionModel(models.Model):
    id = models.AutoField(primary_key=True) 
    file_model_instance = models.ForeignKey(FileModel, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    generation_type = models.CharField(max_length=3, choices=generate_execution_types)


class GeneratedQuestionsModel(models.Model):
    id = models.AutoField(primary_key=True)
    generate_execution_instance = models.ForeignKey(GenerateExecutionModel, on_delete=models.CASCADE)
    question_text = models.TextField(null=True)
    question_text_context = models.TextField(null=True)
    answer_text = models.JSONField(default=dict)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
