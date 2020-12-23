from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('M', 'Lipa na Mpesa'),
    ('C', 'Credit card'),
    ('P', 'Paypal'),
    ('S', 'Stripe'),
)

class PaymentForm(forms.Form):
    county = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'County Address'
    }))
    street_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Street Address'
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100',
        'id': 'zip'
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)