from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Like

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):

        new_user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return new_user
    
    class Meta:
        model = User
        fields = ("id","username","password") 

class PostSerializer(serializers.ModelSerializer):
    likes = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
           
