from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    password = models.TextField()

    def __str__(self):
        return self.email

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    stock_name  = models.TextField()
    post = models.TextField()
    image_url = models.TextField()
    
    def __str__(self):
        return self.post

# 1 para, refer to User class object
# 2 para, if user deleted, user's comment will get deleted
# 3 para, user.comments.all allow to see all comment made by that user
#       comments is the name in DB
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment  = models.TextField()
    
    def __str__(self):
        return self.comment
