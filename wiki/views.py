from django.shortcuts import render
from wiki.forms import *


def add_topic(request):

    if request.method == 'GET':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'wiki/add_topic.html', context)
