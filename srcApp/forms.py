from django import forms
from srcApp.models import Reservation
from crispy_forms.helper import FormHelper
from django.core.mail import send_mail
from django.conf import settings
from srcApp.models import Personnel
from django.forms import ModelForm
from srcApp.models import Ressource

class ReservationForm(forms.ModelForm):
    date_de_reservation = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}), input_formats=['%d/%m/%Y','%d-%m-%Y','%Y-%m-%d'])

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

class ContactAdminForm(forms.Form):

   nom = forms.CharField(max_length=120)
   email = forms.EmailField()
   Objet = forms.CharField(max_length=70)
   message = forms.CharField(widget=forms.Textarea)

   def get_info(self):
       """
       Method that returns formatted information
       :return: subject, msg
       """
       # Cleaned data
       cl_data = super().clean()

       name = cl_data.get('nom').strip()
       from_email = cl_data.get('email')
       subject = cl_data.get('objet')

       msg = f'{name} with email {from_email} said:'
       msg += f'\n"{subject}"\n\n'
       msg += cl_data.get('message')

       return subject, msg

   def send(self):
       subject, msg = self.get_info()

       send_mail(
           subject=subject,
           message=msg,
           from_email=settings.EMAIL_HOST_USER,
           recipient_list=[settings.RECIPIENT_ADDRESS]
       )

class ressourceCreateForm(ModelForm):
    class Meta:
        model = Ressource
        fields = '__all__'