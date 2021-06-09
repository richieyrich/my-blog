
from django.shortcuts import render, get_object_or_404
from .models import post
from django.utils import timezone
# Create your views here.

def post_list(request):
    posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})


def post_details(request, pk):
    post_item = get_object_or_404(post, pk=pk)
    return render(request, 'blog/post_details.html', {'post_item': post_item} )