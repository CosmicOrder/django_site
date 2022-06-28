from django.db import models
from django.utils import timezone


class OrderDetail(models.Model):
    name = models.CharField('ФИО', max_length=100)
    email = models.EmailField('Электронная почта', max_length=100)
    phone = models.CharField(
        'Мобильный телефон заказчика',
        max_length=100,
        db_index=True,
    )
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField(
        'Когда создан запрос',
        default=timezone.now,
        db_index=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Детали запроса'
        verbose_name_plural = 'Детали запроса'
