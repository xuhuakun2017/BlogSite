from django.shortcuts import render
from .models import Blog, Type,Nav
from django.core.paginator import Paginator
import markdown
# Create your views here.
def blog_detail(request, blog_pk):
    blog = Blog.objects.get(pk=blog_pk)
    nav = Nav.objects.all()
    context = {}
    context['blog'] = blog
    context['blog'].body = markdown.markdown(
        context['blog'].body,
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    context['navs'] = nav
    return render(request, 'blog/blog_detail.html', context) # 响应
