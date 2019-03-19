from django.shortcuts import render

from django.http import HttpResponse


def blog_index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


def site_index(request):
    return render(request, 'blog/index.html')
