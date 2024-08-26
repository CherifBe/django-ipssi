from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article, Comment

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'articles']

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'comments', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    article = serializers.ReadOnlyField(source='article.title')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'article', 'created_at']
