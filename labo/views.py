from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    comment = Comment.objects.all()

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'comments': comment, 'form': form}
    return render(request, 'index/index.html', context)


def update_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'comment': comment}
    return render(request, 'index/update.html', context)


def delete_comment(request, pk):
    item = Comment.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'index/delete.html', context)








