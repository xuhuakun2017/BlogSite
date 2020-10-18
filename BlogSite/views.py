from django.shortcuts import render
from Blog.models import Nav,Blog,MyInfo,Type
def index(request):
    nav = Nav.objects.all()
    blog = Blog.objects.all()
    myinfo = MyInfo.objects.all()
    types = Type.objects.all()
    context = {}
    context['types'] = types
    context['navs'] = nav
    context['blogs'] = blog
    context['infos'] = myinfo
    return render(request, 'index.html', context) # 响应
