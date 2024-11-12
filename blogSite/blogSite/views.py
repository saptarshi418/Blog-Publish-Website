from django.http import HttpResponse
from django.shortcuts import render , redirect
from blogapp.models import Categories
from textwriter.models import Textwriter
from textwriter.forms import BlogForm
def indexPage(request):
    categoryData = Categories.objects.all().order_by('id')
    
    blog_article = Textwriter.objects.all()
   
    data={
        'catagory' : categoryData,
        'blog_article': blog_article,
    }
    return render (request,'index.html',data)


   
   

def createblog(request):
    catagoryData = Categories.objects.all().order_by('id')
    fm = BlogForm()
    data={
        'catagory' : catagoryData,
        'BlogForm' : fm,
    }
    
    return render(request, 'createblog.html',data)