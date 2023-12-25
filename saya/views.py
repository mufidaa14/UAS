from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import DaftarForm


# Create your views here.

def pendaftaran_form(request):
    context = {}
    context['form']= DaftarForm() 
    return render(request, "pendaftaran_form.html", context) 
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


    # return render(request, 'pendaftara-form.html', context)