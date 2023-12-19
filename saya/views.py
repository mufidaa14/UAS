from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import DaftarForm


# Create your views here.

def haii(request):
    template = loader.get_template('haii.html')
    return HttpResponse(template.render())

def pendaftaran_form(request):
    context = {}
    context['form']= DaftarForm() 
    return render(request, "pendaftaran_form.html", context) 


    # return render(request, 'pendaftara-form.html', context)