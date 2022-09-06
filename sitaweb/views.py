import sys
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from orders.models import Data, Status
from orders.forms import DataForm
def add_orders(request):
    form = DataForm
    submitted = False
    if request.method == "POST": 
        form = DataForm(request.POST or None)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/order?submitted=True')
        else: 
            form = DataForm
            if 'submitted' in request.GET: 
                submitted = True
    
    return  render(request,'order.html',{'form': form, 'submitted':submitted}) 

def LandingPages(request):
    status_list = Status.objects.all()
    data_list = Data.objects.all()
    # status_list = Status.objects.all()
    return  render(request,'index.html',{'status_list': status_list, 'data_list': data_list})
def orderpage(request):
    return render(request, 'order.html' ,{})
def Login(request): 
    return render(request, 'login.html',{})

