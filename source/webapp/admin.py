from django.contrib import admin

from webapp.models import Guestbook


# Register your models here.
class GuestbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_email', 'text', 'status', 'created_at', 'updated_at',
                    'is_deleted', 'deleted_at')
    list_filter = ('id', 'author_name', 'text', 'status', 'created_at', 'updated_at',
                   'is_deleted', 'deleted_at')
    search_fields = ('author_name', 'text', 'created_at', 'updated_at', 'is_deleted', 'deleted_at')
    fields = ('author_name', 'author_email', 'text', 'status')
    readonly_fields = ('id', 'created_at')


admin.site.register(Guestbook, GuestbookAdmin)
