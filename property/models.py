from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    pure_owners_phonenumber = PhoneNumberField(verbose_name='Нормализованный номер телефона владельца', blank=True,
                                               db_index=True)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', db_index=True, blank=True, null=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField('Новое здание', db_index=True,
                                       choices=[(True, 'Новостройка'), (False, 'Старое здание')], blank=True, null=True)
    likes = models.ManyToManyField(User, verbose_name='Кто лайкнул', related_name='liked_flats')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.OneToOneField(User, verbose_name='Кто жаловался', on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, verbose_name='На какую квартиру', on_delete=models.CASCADE)
    complaint = models.TextField('Жалоба')

    def __str__(self):
        return f'Жалоба от {self.user} на {self.flat}'

class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200)
    phone = models.CharField('Номер владельца', max_length=20)
    pure_phone = PhoneNumberField('Нормализованный номер владельца', blank=True)
    flats = models.ManyToManyField('Flat', verbose_name='Квартиры в собственности', related_name='owners', blank=True)

    def __str__(self):
        return self.name