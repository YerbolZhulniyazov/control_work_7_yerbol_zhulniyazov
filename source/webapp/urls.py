from django.urls import path

from webapp.views.records import add_view, update_view, delete_view, confirm_delete
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
    path("guestbook/", index_view),
    path('record/add', add_view, name='add_record'),
    path('record/<int:pk>/update/', update_view, name='record_update'),
    path('record/<int:pk>/delete/', delete_view, name='record_delete'),
    path('record/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete')
]
