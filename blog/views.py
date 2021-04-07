from django.shortcuts import render
from django.http import HttpResponse #Find what is this

# Create your views here.
posts = [
	{
		'author':'King',
		'title': 'Blog post 1',
		'content': 'Sun of Pride',
		'date_posted': 'August 27, 2018'
	},
	{
		'author':'Queen',
		'title': 'Blog post 2',
		'content': 'Twinkle Queen',
		'date_posted': 'August 27, 2021'
	},
	
]
def home(request):
	context = {
		'posts':posts
	}
	return render(request, 'blog/home.html',context)

def about(request):
	return render(request, 'blog/about.html')