from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category=category_id, status='Published')    
    category = get_object_or_404(Category,pk=category_id)

    context = {
        'posts': posts,
        'category':category,
    }
    return render(request, 'posts_by_category.html', context)

def blog_page(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method =='POST':
        comments = Comment()
        comments.user = request.user
        comments.blog = single_blog
        comments.comment = request.POST['comment']
        comments.save()
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context={
        'single_blog':single_blog,
        'comments':comments,
        'comment_count':comment_count
    }
    return render(request, 'blog.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context={
        'blogs': blogs,
        'keyword':keyword,
    }
    return render(request, 'search.html', context)