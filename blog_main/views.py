from django.shortcuts import render,get_object_or_404
from blogs.models import Category,Blog
from about.models import About

def home(request):
    # categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True).order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False,status='Published')

    try:
        about = get_object_or_404(About)
    except:
        about=None

    
    context ={
        # 'categories':categories,
        'featured_post':featured_post,
        'posts' : posts,
        'about':about,
    }

        
    return render(request,'home.html',context)

# context 