from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path(
        'post/<int:post_id>/vote/<str:vote_type>/',
        views.vote_post, name='vote_post'),
]