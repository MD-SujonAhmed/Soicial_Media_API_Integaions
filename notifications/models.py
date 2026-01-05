from django.db import models

# Create your models here.
class Post(models.Model)  :
    title = models.CharField(max_length=200)
    body=models.TextField()
    author=models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='posts')
    likes=models.ManyToManyField('users.User', related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title