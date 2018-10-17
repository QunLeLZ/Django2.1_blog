from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Tag
from comment.forms import CommentForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.conf import settings
from django.db.models.aggregates import Count

# Create your views here.
categories = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
tags = Tag.objects.all()
dates = Post.objects.datetimes('created_time','month',order='DESC')
new_list = Post.objects.order_by('-created_time')[:5]

def index(request):
    posts = Post.objects.all().order_by('-created_time')
    paginator = Paginator(posts, settings.PAGE_NUM)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'blog/index.html',context={'post_list':post_list,'category_list':categories,'tag_list':tags,'date_list':dates,'new_list':new_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.increase_views()
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post':post,'category_list':categories,'tag_list':tags,'date_list':dates,'form':form,'comment_list':comment_list,'new_list':new_list}
    return render(request,'blog/detail.html',context=context)

def archives(request,year,month):
    posts = Post.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
    paginator = Paginator(posts, settings.PAGE_NUM)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'blog/archives.html',{'post_list':post_list,'category_list':categories,'tag_list':tags,'date_list':dates,'new_list':new_list})

def search_category(request,id):
    posts = Post.objects.filter(category_id=str(id))
    paginator = Paginator(posts, settings.PAGE_NUM)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'blog/category.html',{'post_list':post_list,'category_list':categories,'tag_list':tags,'date_list':dates,'new_list':new_list})

def search_tag(request,tag):
    posts = Post.objects.filter(tags__name__contains=tag)
    paginator = Paginator(posts, settings.PAGE_NUM)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'blog/tag.html',{'post_list':post_list,'category_list':categories,'tag_list':tags,'date_list':dates,'new_list':new_list})

def about_me(request):
    return render(request,'blog/about.html',{'category_list':categories,'tag_list':tags,'date_list':dates})