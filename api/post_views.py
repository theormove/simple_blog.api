from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import  PostSerializer
from .models import Post, Like



class CreatePostView(CreateAPIView):  
    #need to auto add logined user as author
    model = Post
    serializer_class = PostSerializer

class ListPostView(ListAPIView):  
    queryset = Post.objects.all()
    serializer_class = PostSerializer    


class PostLikeView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            return Response("You need to login to like posts")
        post_id = kwargs["id"]
        old_like = Like.objects.filter(user=user,post_id=post_id) 
        if not old_like:
            new_like = Like.objects.create(user = user, post_id = post_id)
            return Response("liked")
        else:
            old_like.delete()
            return Response("unliked")
         

class LikeAnalyticsView(APIView):
    def get(self,request, **kwargs):
        #would be more reasonable to get analytics about specific post or author
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')     
        if date_from and date_to:
            number_of_likes = Like.objects.filter(date__range=[date_from,date_to]).count()
            return Response(str(number_of_likes))
        return Response("Need to provide date_from=YYYY-MM-DD and date_to=YYYY-MM-DD parameters in your request")