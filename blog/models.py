from enum import auto
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf.urls.static import static


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)




class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images', default='mysite\blog\static\img\bg2.png')

    class Meta:
        ordering = ['-created_on']
    class Meta:
        db_table = "myapp_image"

    def __str__(self):
        return self.title



class CommentModel(models.Model):
    your_name = models.CharField(max_length=20)
    comment_text = models.TextField()
    blog = models.ForeignKey('Post', on_delete=models.CASCADE)

    def str(self):
        return f"Comment by Name: {self.your_name}"