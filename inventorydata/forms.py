from django.forms import ModelForm
from .models import Item, Checkout

ITEM_LOCATIONS = (('Storage Unit', 'Storage Unit'), ('NSP Office', 'NSP Office'))
ITEM_CLASSIFICATION = (('Technology', 'Technology'), ('Not Technology', 'Not Technology'))

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_text', 'description', 'quantity',
         'relative_location', 'site', 'tech_classification', 'checkoutable']

class PartialCheckoutForm(ModelForm):
    class Meta:
        model = Checkout
        exclude = ['item', 'return_date']
        # fields = ['item', 'first_name', 'last_name', 'checkout_date', 'return_date']



# class CheckoutForm(forms.Form):
#     item = forms.ModelChoiceField(empty_label=None, to_field_name="item") #Come back to this in form
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     checkout_date = forms.DateTimeField('Date Checked Out', default=timezone.now)
#     return_date = forms.DateTimeField('Date Returned', empty_value=None, blank=True)

# class ItemForm(forms.ModelForm):
#     item_text = forms.CharField(max_length=200)
#     description = forms.CharField(max_length=200)
#     quantity = forms.IntegerField()
#     relative_location = forms.CharField(max_length=100)
#     site = forms.CharField(
#         max_length=30, 
#         widget=forms.Select(choices=ITEM_LOCATIONS),
#     )
#     tech_classification = forms.CharField(
#         max_length=30,
#         widget=forms.Select(choices=ITEM_CLASSIFICATION),
#     )
#     checkoutable = forms.BooleanField()