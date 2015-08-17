from django.shortcuts import render
from wiki.forms import *


def add_topic(request):

    form = TopicForm()
    context = {'form': form}

    return render(request, 'wiki/add_topic.html', context)
