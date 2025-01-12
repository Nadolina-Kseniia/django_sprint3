from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from blog.models import Post, Category

from datetime import datetime

def posts():
    """Получение постов из БД"""
    return Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    )


def index(request):
    template_name = 'blog/index.html'
    context = {'post_list': posts()[:5]}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        posts(),
        pk=id
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.values('title'),
        slug=category_slug,
        is_published=True
    )

    context = {'category': category,
               'post_list': posts().filter(category__slug=category_slug)}
    return render(request, template_name, context)
