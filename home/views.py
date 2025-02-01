from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Post
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Post, Vote
from django.views.decorators.http import require_POST

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "home/index.html"
    paginate_by = 5


def index(request):
    posts = Post.objects.all()
    return render(request, 'home/index.html', {'posts': posts})


@require_POST  # Ensure only POST requests are allowed
def vote_post(request, post_id, vote_type):
    if not request.user.is_authenticated:
        return JsonResponse(
            {'success': False, 'error':
                'You must be logged in to vote.'}, status=403)

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse(
            {'success': False, 'error': 'Post not found.'}, status=404)

    # Check if the user has already voted
    existing_vote = Vote.objects.filter(user=request.user, post=post).first()

    if existing_vote:
        if existing_vote.vote_type == vote_type:
            # User is trying to vote the same way again, so remove the vote
            existing_vote.delete()
            action = 'removed'
        else:
            # User is changing their vote
            existing_vote.vote_type = vote_type
            existing_vote.save()
            action = 'changed'
    else:
        # User is voting for the first time
        Vote.objects.create(user=request.user, post=post, vote_type=vote_type)
        action = 'added'

    # Update the vote counts
    upvotes = post.total_upvotes()
    downvotes = post.total_downvotes()

    return JsonResponse({
        'success': True,
        'action': action,
        'upvotes': upvotes,
        'downvotes': downvotes,
    })
