from django import forms

from .const import invalid_words
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price_sale', 'publish_status']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите наименование товара'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание товара'})
        self.fields['price_sale'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену товара'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        # invalid_words = [
        #     'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        # ]
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in invalid_words:
            if word.upper() in str(name).upper() :
                self.add_error('name',word + ' недопустимо')
            if word.upper() in str(description).upper():
                self.add_error('description',word + ' недопустимо')

        return cleaned_data

    def clean_price_sale(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price_sale')
        if price <= 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price
