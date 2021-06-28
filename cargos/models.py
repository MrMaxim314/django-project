from datetime import date, timezone

from django.db import models


class Сonveyor(models.Model):
    name = models.CharField(max_length=65, unique=True)
    country = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    type_of_transport = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cargo(models.Model):
    cargo_owner = models.CharField(max_length=100)
    cargo_name = models.CharField(max_length=70)
    cargo_weight = models.IntegerField()
    cargo_move_to = models.CharField(max_length=100)
    cargo_move_from = models.CharField(max_length=100)

    def __str__(self):
        return self.cargo_name


class Transfer(models.Model):
    company_name = models.CharField(max_length=100)
    user = models.CharField(max_length=77)
    cargo = models.CharField(max_length=100)
    adr_from = models.CharField(max_length=200)
    adr_to = models.CharField(max_length=200)
    weight = models.IntegerField()
    shipment_date = models.DateTimeField(auto_now_add=False)
    discharge_date = models.DateTimeField(auto_now_add=False)
    comment_field = models.TextField()
    transporter_field = models.CharField(max_length=140, default='name')
    status = models.CharField(max_length=100, default='принято')
    price = models.IntegerField(default=34)
    car_number = models.CharField(max_length=15, default='-')
    driver_surname = models.CharField(max_length=123, default='-')

    def __str__(self):
        return self.company_name


class Auto(models.Model):
    car_owner = models.CharField(max_length=100)
    car_name = models.CharField(max_length=123)
    car_type = models.CharField(max_length=100)
    price_per_day = models.IntegerField()
    number = models.CharField(max_length=100)


class Rents(models.Model):
    username = models.CharField(max_length=70)
    mark = models.CharField(max_length=77)
    days = models.IntegerField()
    total_price = models.IntegerField()


class Roots(models.Model):
    root = models.CharField(max_length=200)
    distance = models.IntegerField()
    stops = models.IntegerField(default='2')


class RootTransfers(models.Model):
    usr = models.CharField(max_length=110)
    user_root = models.CharField(max_length=200)
    cargo = models.CharField(max_length=150)
    crg_weight = models.CharField(max_length=7)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)



