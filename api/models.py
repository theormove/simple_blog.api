from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    last_activity = models.DateTimeField(null=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        unique_together = ('user', 'post',)
    
    def __str__(self):
        return 'post ' + str(self.post) + ' like by ' + str(self.user)    