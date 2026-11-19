from django.db import models

class Projet (models.Model):
    nom= models.CharField(max_length=100)
    description = models.TextField()
    technologie = models.CharField(max_length=150)
    date_creation = models.DateField(auto_now_add =True)

    competences = models.ManyToManyField('Competence', blank= True, related_name= 'projets')
    date_creation= models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nom

class Competence(models.Model):

    nom = models.CharField(max_length= 100)
    niveau = models.CharField(max_length= 50)
    description= models.TextField()
    def __str__(self):
        return self.nom

class Experience(models.Model):

    poste = models.CharField(max_length=150)
    entreprise = models.CharField(max_length=50)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(
        null=True,
        blank=True
    )
    def __str__(self):
        return self.poste

