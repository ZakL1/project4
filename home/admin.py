from django.contrib import admin
from .models import Post, Review
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Post)


# Register your models here.
admin.site.register(Review)