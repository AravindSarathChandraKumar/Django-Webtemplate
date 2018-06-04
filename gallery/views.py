from django.shortcuts import render
from django.http import HttpResponse
from .models import Pic

# Create your views here.
def gallery(request):
	pics=Pic.objects.all()
	return render(request,'gallery/g.html',{"pics":pics})
	