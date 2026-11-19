from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .forms import ProjetForm
from .models import Projet, Competence

class AcceuilView(ListView):
    model= Projet
    template_name= 'portfolio/acceuil.html'
    context_object_name= 'projets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['competences'] = Competence.objects.all()
        return context

class AjouterProjetView(CreateView):
    model= Projet
    form_class = ProjetForm
    template_name= 'portfolio/ajouter_projet.html'
    success_url= reverse_lazy('acceuil')
    
