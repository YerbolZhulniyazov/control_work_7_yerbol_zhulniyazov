from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    ACTIVE = 'active', 'Активно'
    BLOCKED = 'blocked', 'Заблокировано'


# Create your models here.

class Guestbook(models.Model):
    status = models.CharField(verbose_name='Статус', choices=StatusChoice.choices, max_length=20,
                              default=StatusChoice.ACTIVE)
    author_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Автор записи")
    author_email = models.EmailField(max_length=100, null=False, blank=False, verbose_name="Почта автора записи")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Текст записи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        return f"{self.author_name} - {self.text}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
