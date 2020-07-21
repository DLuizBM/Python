from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    # name = forms.CharField(help_text='Insert name', max_length=20)

    class Meta:
        model = Reservation
        fields = [
            'name', 
            'reservation_date', 
            'hour', 
            'people', 
            #'date_made', essa variável não pode ser editada (auto_now_add=True faz editable=False), por isso não dever ser declarada no forms.
            'observations'
            ]

