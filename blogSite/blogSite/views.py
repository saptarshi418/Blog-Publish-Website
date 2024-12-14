from django.http import HttpResponse
from django.shortcuts import render , redirect
from blogapp.models import Categories
from textwriter.models import Textwriter
from textwriter.forms import BlogForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def indexPage(request):
    categoryData = Categories.objects.all().order_by('id')
    
    blog_article = Textwriter.objects.all()
   
    data={
        'catagory' : categoryData,
        'blog_article': blog_article,
    }
    return render (request,'index.html',data)


 
   



def createblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            print("sfkjhkg")
            instance = form.save()
            print(instance.title)
            return redirect('home')  # Success
        else:
            print(form.errors)  # Log errors
    else:
        form = BlogForm()
    return render(request,'createblog.html', {'form':form})
