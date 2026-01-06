from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name']

class PostSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)
    author =serializers.SerializerMethodField()
    # title=serializers.CharField(max_length=200)
    like_count=serializers.SerializerMethodField()
    is_liked=serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'likes', 'author', 'like_count', 'is_liked']

    def get_author(self, obj):
        return obj.author.full_name
    
    def get_like_count(self,obj):
        return len(obj.likes.all())
    
    # def serializers coustom field add korta hova .. .. ..
    # syntax : field_name=serializers.SerializerMethodField()
    # def get_field_name(self, obj):
    #     return ...
    # example is shown in get_author method .. .. ...
    def get_is_liked(self, obj):
        user=self.context['request'].user
        return True if user in obj.likes.all() else False        
         
    

    