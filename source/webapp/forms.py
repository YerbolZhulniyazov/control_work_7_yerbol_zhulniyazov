from django import forms
from django.forms import widgets


class GuestbookForm(forms.Form):
    author_name = forms.CharField(max_length=50, required=True, label='Автор записи')
    author_email = forms.CharField(max_length=100, required=True, label='Почта автора записи')
    text = forms.CharField(max_length=1000, required=True, label='Текст записи', widget=widgets.Textarea)
