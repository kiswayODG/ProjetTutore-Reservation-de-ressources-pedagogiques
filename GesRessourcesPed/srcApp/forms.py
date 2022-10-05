from django import forms
from srcApp.models import Reservation
from crispy_forms.helper import FormHelper

from srcApp.models import Personnel


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


#users
class UserForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()