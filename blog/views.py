from django.http import JsonResponse
from django.shortcuts import render

from blog.models import Post


def blog_view(request):
    return render(request, 'blog/blog-home.html')


def blog_single(request):
    return render(request, 'blog/blog-single.html')

def test(request):
    post_list = list(Post.objects.filter(status=True).values())
    return render(request,"post.html", context={"post_list":post_list})
