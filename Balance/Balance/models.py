from django.db import models
from django.utils import timezone

class Purchases(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=255, null=False, blank=False)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, null=False, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255, null=False, blank=True)
    date_time = models.DateTimeField(verbose_name='Время', default=timezone.now())
    rate = models.TextField(verbose_name='Тариф / стоимость', null=False, blank=False)
    phone = models.CharField(verbose_name='Номер телефона', max_length=14, null=False, blank=False)
    email = models.EmailField(verbose_name='Email', null=False, blank=False)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ('-date_time', )

class Services(models.Model):
    services = models.TextField(verbose_name='Услуги', null=False, blank=False)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self) -> str:
        return f'Пакет услуг №{self.pk}'

class Rates(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Услуги')
    name = models.CharField(verbose_name='Имя тарифа', max_length=255, null=False, blank=False)
    cost = models.IntegerField(verbose_name='Стоимость руб.', null=False, blank=False)
    mask = models.TextField(verbose_name='Маска', null=False, blank=False)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'