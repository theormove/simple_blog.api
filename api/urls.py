from django.urls import path
from .user_views import CreateUserView, UserActivityView
from .post_views import  CreatePostView, ListPostView, PostLikeView, LikeAnalyticsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
	path('register', CreateUserView.as_view()),
    path('post/create', CreatePostView.as_view()),
    path('posts', ListPostView.as_view()),
    path('post/<int:id>/like', PostLikeView.as_view()),
    path('activity/<str:username>', UserActivityView.as_view()), 
    path('analytics', LikeAnalyticsView.as_view()),   
    path('analytics/', LikeAnalyticsView.as_view()),     
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]    