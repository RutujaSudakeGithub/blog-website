from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Blog,Category



def post_by_category(request,category_id):
    posts=Blog.objects.filter(status='Published',category=category_id)
    # category_name = Category.objects.get(pk=category_id)

    #use try and except when we want to do some action when category is not present

    # try:
    #     category_name = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    
    #use get_object_or_404 when we want to do show 404 error page when category is not present
    category_name = get_object_or_404(Category,pk=category_id)
    
    context ={
        'posts':posts,
        'category_name':category_name
    }

    return render(request,'post_by_category.html',context)

# Create your views here.


