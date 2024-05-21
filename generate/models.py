from django.db import models
from ingest.models import FileModel

generate_execiton_types = (
    ('MCQ', 'Multiple Choice Questions'),
    ('FRQ', 'Free Response Questions'),
)

class GenerateExecutionModel(models.Model):
    id = models.AutoField(primary_key=True) 
    file_model_instance = models.ForeignKey(FileModel, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    generation_type = models.CharField(max_length=3, choices=generate_execiton_types)


class GeneratedQuestionsModel(models.Model):
    id = models.AutoField(primary_key=True)
    generate_execution_instance = models.ForeignKey(GenerateExecutionModel, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.JSONField(default=dict)
    correct_answer = models.JSONField(default=dict)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
