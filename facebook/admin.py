from django.contrib import admin

# Register your models here.
from facebook.models import Article
admin.site.register(Article)
#모델 불러 연결 2줄

from facebook.models import Comment
admin.site.register(Comment)