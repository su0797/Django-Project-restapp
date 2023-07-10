from rest_framework import serializers
from .models import Post, Comment, HashTag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' # model에 있는 모든 필드를 사용한다는 뜻


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'