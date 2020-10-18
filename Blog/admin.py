from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Blog,Tag,Type,Commend, Nav, MyInfo
#导入需要管理的数据库表

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id',  'title', 'commend', 'user', 'views', 'created_time')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    #后台数据列表排序方式
    list_display_links = ('id', 'title')
    # 设置哪些字段可以点击进入编辑界面

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
@admin.register(Nav)
class NavAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
@admin.register(Commend)
class CommendAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')    
@admin.register( MyInfo)
class CommendAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  