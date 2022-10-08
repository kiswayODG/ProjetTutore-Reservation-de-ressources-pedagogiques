from django.shortcuts import render
from django.http import HttpResponse
from srcApp.models import Reservation
from srcApp.forms import ReservationForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from srcApp.forms import ContactAdminForm
from srcApp.forms import UserForm
from srcApp.models import Personnel
from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView
from srcApp.forms import ContactAdminForm
from django.urls import reverse_lazy
is_send=True

# Create your views here.
def welcome(request):
    return render(request, 'registration/welcome.html')
def home(request):
    return render(request, 'index.html')

def reservation(request):
    datas = Reservation.objects.all()

    return render(request,"reservHome.html", {'datas':datas})

def createReservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            res = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('reservation')

    else:
        form = ReservationForm()

    return render(request,
                  'create_reservation.html',
                  {'form': form})


def update_res(request, id):
    reserv = Reservation.objects.get(id=id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reserv)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('reservation')
    else:
        form = ReservationForm(instance=reserv)

        return render(request,
                'update_reserv.html',
                {'form': form})

def delete_res(request, id):
    reserv = Reservation.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        reserv.delete()
        # rediriger vers la liste des groupes
        return redirect('reservation')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'delete_reserv.html',
                    {'reserv': reserv})


## users view
def user(request):
    datas = Personnel.objects.all()

    return render(request,"userHome.html", {'datas':datas})

def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            res = form.save()
            return redirect('user')
    else:
        form = UserForm()

        return render(request,
                  'create_user.html',
                  {'form': form})


def update_user(request, id):
    user = Personnel.objects.get(id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('/user')
    else:
        form = UserForm(instance=user)

        return render(request,
                'update_user.html',
                {'form': form})

def delete_user(request, id):
    user = Personnel.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        user.delete()
        # rediriger vers la liste des groupes
        return redirect('/user')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'delete_user.html',
                    {'user': user})



class ContactView(FormView):
    template_name = 'contactAdmin.html'
    form_class = ContactAdminForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # Calls the custom send method
        #form.send()
        if(is_send):
            return redirect('mailSuccess')
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'success.html'

def mailS(request):
    return render(request, 'success.html')