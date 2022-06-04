from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    #template = 'posts/index.html'
    #title = 'Главная страница'
    context  = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request, slug):
    template = 'posts/groups_list.html' 
    title = 'Здесь будет информация о группах проекта Yatube'
    context  = {'title': title}
    return render(request, template, context) 



# Create your views here.
