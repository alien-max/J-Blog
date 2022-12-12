from django.shortcuts import render, redirect
from categories.models import Categories
from blogs.models import Blogs
from ads.models import Ads
from bs4 import BeautifulSoup

def main(request):
    ads = Ads.objects.all()
    categories = Categories.objects.all()
    blogs = Blogs.objects.all()
    blog_list = []
    for i in blogs:
        excerpt_text = BeautifulSoup(i.remark, 'html.parser').get_text()
        excerpt_list = excerpt_text.split(' ')
        excerpt_part = excerpt_list[:25]
        excerpt = ' '.join(excerpt_part)
        item = {
            'title': i.title,
            'thumbnail': i.thumbnail.url,
            'excerpt': excerpt,
            'pk': i.pk
        }
        blog_list.append(item)
    context = {
        'ads': ads,
        'categories': categories,
        'blogs': blog_list
    }
    return render(request, 'index.html', context=context)


def post(request, pk):
    ads = Ads.objects.all()
    categories = Categories.objects.all()
    blog = Blogs.objects.get(id=pk)
    context = {
        'ads': ads,
        'categories': categories,
        'blog': blog
    }
    return render(request, 'single.html', context=context)


def cat(request, pk):
    ads = Ads.objects.all()
    categories = Categories.objects.all()
    category = Categories.objects.get(id=pk)
    posts = Blogs.objects.filter(دسته__name=category)
    blog_list = []
    for i in posts:
        excerpt_text = BeautifulSoup(i.remark, 'html.parser').get_text()
        excerpt_list = excerpt_text.split(' ')
        excerpt_part = excerpt_list[:25]
        excerpt = ' '.join(excerpt_part)
        item = {
            'title': i.title,
            'thumbnail': i.thumbnail.url,
            'excerpt': excerpt,
            'pk': i.pk
        }
        blog_list.append(item)
    context = {
        'ads': ads,
        'categories': categories,
        'category': category,
        'posts': blog_list
    }
    return render(request, 'category.html', context=context)


def search(request):
    if request.method == 'POST':
        ads = Ads.objects.all()
        categories = Categories.objects.all()
        blog_list = []
        query = request.POST.get('q')
        if query:
            blogs = Blogs.objects.filter(title__contains=query)
            for i in blogs:
                excerpt_text = BeautifulSoup(i.remark, 'html.parser').get_text()
                excerpt_list = excerpt_text.split(' ')
                excerpt_part = excerpt_list[:25]
                excerpt = ' '.join(excerpt_part)
                item = {
                    'title': i.title,
                    'thumbnail': i.thumbnail.url,
                    'excerpt': excerpt,
                    'pk': i.pk
                }
                blog_list.append(item)

            context = {
                'ads': ads,
                'categories': categories,
                'blogs': blog_list
            }
            return render(request, 'search.html', context=context)
        return redirect('/')
    return redirect('/')
