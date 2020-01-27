from django import forms
from .models import Order

# Payment form for checkout view
class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

# First order form for User data
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name')

# Second order from for UserProfile data
class SecondOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('phone_number', 'street_address1', 'street_address2', 'postcode', 'town_or_city', 'county', 'country')