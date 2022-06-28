from django.db import models
from django.utils import timezone


class OrderDetail(models.Model):
    name = models.CharField('ФИО', max_length=200)
    email = models.EmailField('Электронная почта', max_length=200)
    phone = models.CharField(
        'Мобильный телефон заказчика',
        max_length=200,
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


class Sample(models.Model):
    REVERSE = 'Реверсивный инжиниринг'
    DRAFTS = 'Конструкторская документация'
    VISUALIZE = '3д моделирование/визуализация'
    CATEGORIES = [
        ('REVERSE', REVERSE),
        ('DRAFTS', DRAFTS),
        ('VISUALIZE', VISUALIZE),
    ]
    category = models.CharField(
        'Категория',
        max_length=200,
        choices=CATEGORIES,
    )
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение')
    published_at = models.DateTimeField(
        'Дата публикации примера работ',
        default=timezone.now,
        db_index=True,
    )

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'
