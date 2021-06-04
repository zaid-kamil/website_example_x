from django.shortcuts import render
from .models import HR

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
# step 3
def view_hr(request):
    hr = HR.objects.all() # all the data
    ctx = {'hr':hr}       # pack 
    return render(request,'hr/view.html',ctx) # add

def detail_hr(request,pk):
    return render(request,'hr/detail.html')