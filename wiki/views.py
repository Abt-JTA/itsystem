from django.shortcuts import render, redirect
from wiki.forms import *


def add_topic(request):
    if request.method == 'GET':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('edit_topic', t_slug=instance.slug)

    context = {'form': form}
    return render(request, 'wiki/add_topic.html', context)


def edit_topic(request, t_slug):
    topic = Topic.objects.get(slug=t_slug)
    success = False
    if request.method == 'GET':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            success = True

    context = {'form': form, 'success': success}

    return render(request, 'wiki/edit_topic.html', context)
