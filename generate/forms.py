from django import forms
from ingest.models import FileModel
from generate.models import generate_execution_types

class GeneratorForm(forms.Form):
    file_options = forms.ChoiceField()
    generation_type = forms.ChoiceField(choices=generate_execution_types)
    number_of_questions = forms.IntegerField(min_value=1, max_value=10)
    
    def get_file_options(self):
        choices = FileModel.objects.all().order_by('-created_date', ).values_list('id', 'file_name', 'created_date')
        return [(choice[0], f"{choice[1]} – ({choice[2]})") for choice in choices]
        
    def __init__(self, *args, **kwargs):
        super(GeneratorForm, self).__init__(*args, **kwargs)
        self.fields['file_options'] = forms.ChoiceField(
            choices=self.get_file_options(),
        )
