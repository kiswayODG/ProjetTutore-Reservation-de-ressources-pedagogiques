from django.shortcuts import render

from srcApp.models import Reservation


# Create your views here.
def home(request):
    return render(request, 'index.html')

def reservation(request):
    datas = Reservation.objects.all()

    return render(request,"reservHome.html", {'datas':datas})
