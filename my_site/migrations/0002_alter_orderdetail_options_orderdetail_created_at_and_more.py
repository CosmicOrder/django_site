# Generated by Django 4.0.4 on 2022-06-28 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetail',
            options={'verbose_name': 'Детали запроса', 'verbose_name_plural': 'Детали запроса'},
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Когда создан запрос'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='phone',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Мобильный телефон заказчика'),
        ),
    ]
