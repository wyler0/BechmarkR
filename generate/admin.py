from django.contrib import admin
from generate.models import GeneratedQuestionsModel, GenerateExecutionModel

class GenerateExecutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_model_instance', 'created_date', 'generation_type')

class GeneratedQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'generate_execution_instance', 'question_text', 
                    'question_text_context', 'answer_text', 'created_date', 
                    'updated_date')

# Register your models here.
admin.site.register(GenerateExecutionModel, GenerateExecutionAdmin)
admin.site.register(GeneratedQuestionsModel, GeneratedQuestionsAdmin)
