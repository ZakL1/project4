from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    class Meta:
        ordering = ["-created_on"]

    def total_upvotes(self):
        return self.votes.filter(vote_type='upvote').count()

    def total_downvotes(self):
        return self.votes.filter(vote_type='downvote').count()

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="votes")
    vote_type = models.CharField(max_length=10, choices=[('upvote', 'Upvote'), ('downvote', 'Downvote')])

    class Meta:
        unique_together = ('user', 'post')  # Makes sure a user can only vote once per post

    def __str__(self):
        return f"{self.user.username} {self.vote_type}d {self.post.title}"
        