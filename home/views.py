from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import JsonResponse
from django.shortcuts import get_object_or_404 
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "home/index.html"
    paginate_by = 20
    
def index(request):
    posts = Post.objects.all()
    return render(request, 'home/index.html', {'posts': posts})

@login_required
def vote(request, post_id, vote_type):
    post = get_object_or_404(Post, id=post_id)

    if vote_type == 'upvote':
        post.upvotes += 1
    elif vote_type == 'downvote':
        post.downvotes += 1
    else:
        return JsonResponse({'error': 'Invalid vote type'}, status=400)

    post.save()

    return JsonResponse({
        'upvotes': post.upvotes,
        'downvotes': post.downvotes,
    })