from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

#부가적 admin 페이지에서 다름 해도되고 안해도 됨
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commnets')
    author = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)