# Generated by Django 4.2.7 on 2023-11-22 15:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=500, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('contract_number', models.CharField(max_length=30, verbose_name='Номер контракта')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=500, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('created_date', models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания')),
                ('deals_count', models.PositiveIntegerField(verbose_name='Количество сделок')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
                'db_table': 'manager',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('apart_no', models.CharField(max_length=100, verbose_name='Номер')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('area', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Площадь')),
                ('date', models.DateField(verbose_name='Дата')),
                ('status', models.CharField(choices=[('active', 'Активный'), ('reservation', 'Бронь'), ('purchased', 'Куплено'), ('installment', 'Рассрочка'), ('barter', 'Бартер')], max_length=20, verbose_name='Статус')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('pur_status', models.CharField(max_length=255, verbose_name='Статус покупки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
                'db_table': 'apartment',
            },
        ),
    ]
