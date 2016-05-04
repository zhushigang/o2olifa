from django import forms
from .models import Order

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('first_name','last_name', 'address1','address2','mobile_number', 'gender', 'date', 'time')

#    name = forms.CharField(label='Name', max_length=100)
#    address = forms.CharField(label='Address', max_length=200)
