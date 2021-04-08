from django.shortcuts import render
from django.http import HttpResponse #Find what is this
from .models import post
# Create your views here.
def home(request):
	context = {
		'posts':post.objects.all()
	}
	return render(request, 'blog/home.html',context)

def about(request):
	return render(request, 'blog/about.html')