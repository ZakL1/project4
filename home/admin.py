from django.contrib import admin
from .models import Post, Review
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Post)

#class PostAdmin(SummernoteModelAdmin):

#    list_display = ('title', 'slug', 'status')
#    search_fields = ['title']
#    list_filter = ('status',)
#    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Review)