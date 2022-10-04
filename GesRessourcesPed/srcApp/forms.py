from django import forms

from srcApp.models import Reservation

class ResrvationForm(forms.ModelForm):
   class Meta:
     model = Reservation
     fields = '__all__'