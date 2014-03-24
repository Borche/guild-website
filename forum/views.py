
from django.http import HttpResponse
from django.shortcuts import render

from forum.models import Forum, Thread, Comment

# Create your views here.

def forums(request):
    all_forums = Forum.objects.all()
    response = {'forums': all_forums}
    return render(request, 'forum/forums.html', response)

def threads(request, f_id):
    all_threads = Thread.objects.filter(forum_id=f_id)
    response = {'f_id': f_id, 'threads': all_threads}
    return render(request, 'forum/threads.html', response)

def comments(request, t_id):
    all_comments = Comment.objects.filter(thread_id=t_id).order_by('number')
    response = {'t_id': t_id, 'comments': all_comments}
    return render(request, 'forum/comments.html', response)

def new_comment(request, t_id):
    print t_id
    response = { 't_id': t_id }
    return render(request, 'forum/new_comment.html', response)
        