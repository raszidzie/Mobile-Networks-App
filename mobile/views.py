from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,get_list_or_404
from .models import *
from django.utils.text import slugify
# Create your views here.



def operator_detail(request, slug):
    detail = get_object_or_404(Operators, slug=slug)
    context={
        'detail':detail,
        
    }
    template="operator_detail.html"
    return render(request, template, context)

def operators(request, slug):
    country = get_object_or_404(Countries, slug=slug)
    operators = Operators.objects.filter(slug=slug)
    context = {
     
        'country':country,
        'operators':operators,
    }
    template="operators.html"
    return render(request, template, context)

def countries(request):
    countries = Countries.objects.all()
    context = {
        'countries':countries,
    }
    template = "country.html"
    return render(request, template, context)

def welcome(request):
    template = "welcome.html"
    return render(request, template )                      