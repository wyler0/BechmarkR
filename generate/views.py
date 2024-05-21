from django.shortcuts import render
from django.views import View

# Create your views here.
from generate.forms import GeneratorForm

class GenerationView(View):
    def post(self, request):
        form = GeneratorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # Handle the validated data here...
            pass
    
    def get(self, request):
        form = GeneratorForm()  # An unbound form
        return render(request, 'generate_submission.html', {'form': form})

