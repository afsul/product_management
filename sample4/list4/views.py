from django.shortcuts import render
from . models import list4

# Create your views here.
def index(request):
    list = list4.objects.all()
    
    return render(request, 'index.html',{'ls':list})
