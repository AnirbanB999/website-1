#!/usr/bin/python  
# -*- coding:utf-8 -*-  
from rest_framework import serializers
from .models import Article_add, Category_Article,Article_Comment
from apps.user.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','user_imag',)


class Category_ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Article
        fields = ('name',)


class Article_CommentSerializerAdd(serializers.ModelSerializer):

    class Meta:
        model = Article_Comment
        fields = '__all__'


class Article_CommentSerializer1(serializers.ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Article_Comment
        fields = '__all__'






class Article_CommentSerializer(serializers.ModelSerializer):
    # def to_representation(self, instance):
    #     res=super().to_representation(instance=instance)
    #     if res['aomments_id'] is None:
    #         print(res)
    #         return res
    #     else:
    #         print('ok')
    #         pass
    #         return
    #sub_cat = Article_CommentSerializer1(many=True)
    user = UserSerializer()
    class Meta:
        model = Article_Comment
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    authors = UserSerializer()
    category = Category_ArticleSerializer()
    article_comment_set = Article_CommentSerializer(many=True)
    class Meta:
        model = Article_add
        fields = '__all__'

