from django.db import models
from django.contrib.auth.models import User 
from mdeditor.fields import MDTextField
# Create your models here.
# 文章分类
class Commend(models.Model):
    name = models.CharField('推荐位',max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):  
        return self.name


class Tag(models.Model):
    name = models.CharField('文章标签',max_length=100)
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
# 文章标签
class Type(models.Model):
    name = models.CharField('博客分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
# 文章内容
class MyInfo(models.Model):
    name = models.CharField('昵称', max_length=100)
    img = models.ImageField(upload_to='head-img', verbose_name='头像', blank=True, null=True)
    told =  models.CharField('签名', max_length=100)
    verbose_name = '昵称'
    verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField('标题', max_length=70)
    abstract = models.TextField('摘要', max_length=200, blank=True)
    types = models.ForeignKey(Type, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    #使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag,verbose_name='标签', blank=True)
    #使用外键关联标签表与标签是多对多关系
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    body = MDTextField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    #"""
    #  文章作者，这里User是从django.contrib.auth.models导入的。
    #  这里我们通过 ForeignKey 把文章和 User 关联了起来。
    #  """
    views = models.PositiveIntegerField('阅读量', default=0)
    commend= models.ForeignKey(Commend, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    def __str__(self):
        return self.title
# 导航栏
class Nav(models.Model):
    name = models.TextField('导航',max_length=70)
    class Meta:
        verbose_name = '导航'
        verbose_name_plural = '导航'
    def __str__(self):
        return self.name
# 友情链接
# 关于我
# 轮播图