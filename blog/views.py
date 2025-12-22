from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def blog_list(request):
    """
    Display all published blog posts
    """
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blogs/blog_list.html', {
        'posts': posts
    })


def blog_detail(request, slug):
    """
    Display a single blog post with ordered content blocks
    """
    post = get_object_or_404(
        BlogPost,
        slug=slug,
        published=True
    )

    blocks = post.blocks.all().order_by('order')

    return render(request, 'blogs/blog_detail.html', {
        'post': post,
        'blocks': blocks
    })
