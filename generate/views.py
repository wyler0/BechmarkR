from django.shortcuts import render
from django.views import View

# Create your views here.
from generate.forms import GeneratorForm
from generate.tasks import generate_questions

class GenerationView(View):
    def post(self, request):
        form = GeneratorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            
            task = generate_questions.delay(form.cleaned_data['file_options'], form.cleaned_data['generation_type'], form.cleaned_data['number_of_questions'])
            
            flower_url = "http://localhost:5555/task/%s" % task.id
            return render(request, 'generate_success.html', {"task_url": flower_url})  # Redirect to success URL or view name
    
    def get(self, request):
        form = GeneratorForm()  # An unbound form
        return render(request, 'generate_submission.html', {'form': form})

