from django.urls import path
from .views import AcceuilView, AjouterProjetView
urlpatterns =[
    path('',AcceuilView.as_view(), name='acceuil'),
    path('projet/ajouter/', AjouterProjetView.as_view(), name= 'ajouter_projet'),
]