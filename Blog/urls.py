from django.urls import path
from . import views
# 地址：http://127.0.0.1:8000/blog
# start with blog
urlpatterns = [
    # http://localhost:8000/blog/
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
]