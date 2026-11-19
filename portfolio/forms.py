
from django import forms
from .models import Projet


class ProjetForm(forms.ModelForm):

    class Meta:
        model = Projet

        fields = [
            'nom',
            'description',
            'technologie',
            'competences'
        ]

        widgets = {
            'nom': forms.TextInput(attrs={
                'placeholder': 'Nom du projet',
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Décris ton projet...',
                'rows': 4,
                'class': 'form-control'
            }),

            'technologie': forms.TextInput(attrs={
                'placeholder': 'Python, Django, HTML...',
                'class': 'form-control'
            }),
        }

    def clean_nom(self):
        nom = self.cleaned_data['nom']

        if len(nom.strip()) < 3:
            raise forms.ValidationError(
                "Le nom doit contenir au moins 3 caractères."
            )

        return nom
