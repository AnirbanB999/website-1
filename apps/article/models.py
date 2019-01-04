import uuid
from datetime import datetime


from django.db import models

from apps.user.models import User
# Create your models here.


class Category_Article(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=100)
    add_time = models.DateTimeField(default=datetime.now)


class Article_add(models.Model):
    """文章"""
    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    authors = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    category = models.ForeignKey(Category_Article,on_delete=models.CASCADE,verbose_name='分类')
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200,blank=True,null=True)
    desc = models.CharField(max_length=400,blank=True,null=True)
    list_pic = models.ImageField(upload_to='article/%Y%m%d',blank=True,null=True)
    content = models.TextField()
    click_nums = models.IntegerField(default=0,verbose_name='阅读数量')
    add_time = models.DateTimeField(auto_now_add=True)


class Article_Comment(models.Model):
    """"评论"""
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    article =models.ForeignKey(Article_add,verbose_name='文章',on_delete=models.CASCADE,null=True,blank=True)
    comments = models.TextField(verbose_name='评论')
    aomments_id = models.ForeignKey('self',on_delete=models.CASCADE,related_name='sub_cat',null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name ='文章评论'
        verbose_name_plural=verbose_name