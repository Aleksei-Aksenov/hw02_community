from django.shortcuts import get_object_or_404, render

from .models import Group, Post

LIMIT_POSTS = 10


def index(request):
    posts = Post.objects.select_related('author').all()[:LIMIT_POSTS]
    return render(request, 'posts/index.html',
                  {'posts': posts, }
                  )


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.post_group.all()[:LIMIT_POSTS]
    return render(request, "posts/group_list.html",
                  {"group": group,
                   "posts": posts, }
                  )
