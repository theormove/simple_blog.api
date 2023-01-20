from rest_framework import permissions
from rest_framework.generics import CreateAPIView 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny# Or anon users can't register
    ]
    serializer_class = UserSerializer


        
class UserActivityView(APIView):
    def get(self,request, **kwargs):
        username = kwargs["username"]
        user = User.objects.filter(username=username).first()
        if user:
            activity = {
                "username": username,
                "last_activity": user.last_activity,
                "last_login": user.last_login
            }
            return Response(activity)
        else:
            return Response(f'No users with username: {username}')    

