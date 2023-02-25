from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.models import Guestbook


def index_view(request: WSGIRequest):
    records = Guestbook.objects.exclude(status='blocked').exclude(is_deleted=True).order_by('-created_at')
    context = {
        'records': records
    }
    return render(request, 'index.html', context=context)
