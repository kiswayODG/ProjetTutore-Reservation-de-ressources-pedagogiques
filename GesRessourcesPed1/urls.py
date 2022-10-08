"""GesRessourcesPed1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.views.generic.base import TemplateView
from srcApp import views
from schema_graph.views import Schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='registration/welcome.html'), name='home'),
    path('index/', views.home, name='accueil'),
    path('reservation/', views.reservation, name='reservation'),
    path('reservation/create_reserv', views.createReservation, name='create_reservation'),
    path('user/', views.user, name='user'),
    path('user/create_user', views.createUser, name='create_user'),
    path('user/<int:id>/change/', views.update_res, name='update_user'),
    path('user/<int:id>/delete/', views.delete_res, name='delete_user'),

    path('reservation/<int:id>/change/', views.update_res,name='update_reservation'),
    path('reservation/<int:id>/delete/', views.delete_res,name='delete_reservation'),
    path('welcome/', include("django.contrib.auth.urls")),
    path('contact-admin/', views.ContactView.as_view(), name='contactAdmin'),
    path('success/', views.ContactSuccessView.as_view(), name="success"),
    path('schema/', Schema.as_view())

]
