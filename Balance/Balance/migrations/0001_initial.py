# Generated by Django 4.0.2 on 2023-09-04 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='index_files/')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('date_time', models.DateTimeField(default='04.09.2023 14:17:20', verbose_name='Время')),
                ('rate', models.TextField(verbose_name='Тариф / стоимость')),
                ('phone', models.CharField(max_length=14, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('requisites', models.TextField(verbose_name='Реквизиты')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
                'ordering': ('-date_time',),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.TextField(verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя тарифа')),
                ('cost', models.IntegerField(verbose_name='Стоимость руб.')),
                ('mask', models.TextField(verbose_name='Маска')),
                ('files', models.ManyToManyField(blank=True, to='Balance.Files', verbose_name='Файлы для отправки')),
                ('links', models.ManyToManyField(blank=True, to='Balance.Links', verbose_name='Ссылки для отправки')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Balance.services', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
    ]
