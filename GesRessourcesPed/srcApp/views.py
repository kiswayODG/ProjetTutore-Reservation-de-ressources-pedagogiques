from django.shortcuts import render

from srcApp.models import Reservation
from srcApp.forms import ResrvationForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def reservation(request):
    datas = Reservation.objects.all()

    return render(request,"reservHome.html", {'datas':datas})

def createReservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            reserv = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('reservation_detail', band.id)

    else:
        form = ReservationForm()

    return render(request,
                  'create_reservation.html',
                  {'form': form})