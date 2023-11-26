from django.db import models
from django.utils.timezone import now

class Client(models.Model):
    full_name = models.CharField(max_length=500, verbose_name="ФИО")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона")
    contract_number = models.CharField(max_length=30, verbose_name="Номер контракта")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'client'


class Apartment(models.Model):
    STATUS = [
        ("active", "Активный"),
        ("reservation", "Бронь"),
        ("purchased", "Куплено"),
        ("installment", "Рассрочка"),
        ("barter", "Бартер"),
    ]

    name = models.CharField(max_length=255, verbose_name="Название")
    apart_no = models.CharField(max_length=100, verbose_name="Номер")
    floor = models.IntegerField(verbose_name="Этаж")
    area = models.DecimalField(verbose_name="Площадь", decimal_places=1, max_digits=5   )
    date = models.DateField(verbose_name="Дата")
    status = models.CharField(choices=STATUS, max_length=20, verbose_name="Статус")
    price = models.PositiveIntegerField(verbose_name="Цена")
    client = models.ForeignKey(Client, verbose_name="Клиент", on_delete=models.DO_NOTHING)
    pur_status = models.CharField(max_length=255, verbose_name="Статус покупки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
        db_table = 'apartment'


class Manager(models.Model):
    full_name = models.CharField(max_length=500, verbose_name='ФИО')
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Почта")
    created_date = models.DateField(default=now, editable=False, verbose_name="Дата создания")
    deals_count = models.PositiveIntegerField(verbose_name="Количество сделок")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'
        db_table = 'manager'

