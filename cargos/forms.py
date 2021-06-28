from django import forms
from .models import Cargo, Transfer, Rents, Roots, RootTransfers


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = [
            'cargo_owner',
            'cargo_name',
            'cargo_weight',
            'cargo_move_to',
            'cargo_move_from'
        ]
        labels = {
            'cargo_owner': 'Пользователь, который добавляет груз',
            'cargo_name': 'Наименование груза',
            'cargo_weight': 'Масса',
            'cargo_move_to': 'Куда',
            'cargo_move_from': 'Откуда'
        }


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = [
            'company_name',
            'user',
            'cargo',
            'adr_from',
            'adr_to',
            'weight',
            'shipment_date',
            'discharge_date',
            'comment_field'
        ]
        labels = {
            'company_name': 'Юридическое название заказчика',
            'user': 'Пользователь системы',
            'cargo': 'Груз',
            'adr_from': 'Место загрузки',
            'adr_to': 'Место разгрузки',
            'weight': 'Масса',
            'shipment_date': 'Дата загрузки',
            'discharge_date': 'Дата разгрузки',
            'comment_field': 'Дополнительный пожелания'
        }


class RentsForm(forms.ModelForm):
    class Meta:
        model = Rents
        fields = [
            'username',
            'mark',
            'days',
            'total_price'
        ]
        labels = {
            'username': 'Имя пользователя',
            'mark': 'Марка машины',
            'days': 'Количество дней',
            'total_price': 'Стоимость'
        }


class RootTrForm(forms.ModelForm):
    class Meta:
        model = RootTransfers
        fields = [
            'usr',
            'user_root',
            'cargo',
            'crg_weight',
            'start',
            'end'
        ]
        labels = {
            'usr': 'Имя пользователя',
            'user_root': 'Маршрут',
            'cargo': 'Груз',
            'crg_weight': 'Вес',
            'start': 'Загрузка',
            'end': 'Разрузка'
        }
