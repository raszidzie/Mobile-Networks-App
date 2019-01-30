from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,get_list_or_404
from .models import *
# Create your views here.



def operator_detail(request, id):
    detail = get_object_or_404(Operators, id=id)
    context={
        'detail':detail,
        
    }
    template="operator_detail.html"
    return render(request, template, context)

def operators(request, id):
    country = get_object_or_404(Countries, id=id)
    operators = Operators.objects.filter(id=id)
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