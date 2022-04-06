from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views

posts = [
    {
        'author': 'CoreyMS',
        'title': "blog post 1",
        'content': 'First post content',
        'date_posted': 'Aug 27, 2018',
    },
    
    {        
        'author': 'GIjane',
        'title': "blog post 2",
        'content': 'second post content',
        'date_posted': 'Aug 28, 2018',       
    },
]


def home(request):
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html', context)

def about(request):
    
    return render(request, 'blog/about.html', {'title': 'About'})