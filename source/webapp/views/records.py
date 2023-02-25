from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import GuestbookForm
from webapp.models import Guestbook


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = GuestbookForm()
        return render(request, 'record_create.html', context={'form': form})

    form = GuestbookForm(data=request.POST)
    if form.is_valid():
        Guestbook.objects.create(
            author_name=form.cleaned_data['author_name'],
            author_email=form.cleaned_data['author_email'],
            text=form.cleaned_data['text'])
        return redirect('index')
    else:
        return render(request, 'record_create.html', context={'form': form})


def update_view(request, pk):
    record = get_object_or_404(Guestbook, pk=pk)
    if request.method == 'GET':
        form = GuestbookForm(initial={
            'author_name': record.author_name,
            'author_email': record.author_email,
            'text': record.text,
        })
        return render(request, 'record_update.html', context={'form': form, 'record': record})
    form = GuestbookForm(data=request.POST)
    if form.is_valid():
        record.author_name = form.cleaned_data['author_name']
        record.author_email = form.cleaned_data['author_email']
        record.text = form.cleaned_data['text']
        record.save()
        return redirect('index')
    else:
        return render(request, 'record_update.html', context={'form': form, 'record': record})


def delete_view(request, pk):
    record = get_object_or_404(Guestbook, pk=pk)
    return render(request, 'confirm_delete.html', context={'record': record})


def confirm_delete(request, pk):
    record = get_object_or_404(Guestbook, pk=pk)
    record.delete()
    return redirect('index')
