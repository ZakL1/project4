from django import template

register = template.Library()

@register.filter(name='vote_count')
def vote_count(post, vote_type):
    return post.vote_set.filter(vote_type=vote_type).count()