from django.utils import timezone

from .models import User


class UpdateLastActivityMiddleware():
    def __init__(self, get_response):
        self._get_response = get_response
    def __call__(self,request):
        response = self._get_response(request) 
        if request.user.is_authenticated:
            User.objects.filter(id=request.user.id).update(last_activity=timezone.now())
        return response    