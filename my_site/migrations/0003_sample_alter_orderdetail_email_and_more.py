# Generated by Django 4.0.4 on 2022-06-28 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0002_alter_orderdetail_options_orderdetail_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('published_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата публикации примера работ')),
            ],
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='phone',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Мобильный телефон заказчика'),
        ),
    ]
