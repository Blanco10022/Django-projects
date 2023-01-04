from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Niveaux(models.Model):  #level
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()


    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)  
        super().save(*args, **kwargs)  


class Matiere(models.Model): #department
    matiere_id = models.CharField(unique=True, max_length=40)
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE, related_name='matiere')  #level
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)  
        super().save(*args, **kwargs)  

class Lesson(models.Model):  #course 
    lesson_id = models.CharField(unique=True, max_length=40)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    creer_par = models.ForeignKey(User, on_delete=models.CASCADE) 
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='lesson')
    nom = models.CharField(max_length=100) 
    slug = models.SlugField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(verbose_name='Year')  
    video = models.FileField(upload_to="Video", null=True, blank=True, verbose_name="Video")
    image = models.FileField(upload_to="img", null=True, blank=True, verbose_name="img")
    fpe = models.FileField(upload_to="Answers", null=True, blank=True, verbose_name="Answers")
    pdf = models.FileField(upload_to="PDF", null=True, blank=True, verbose_name="Question")
   

    class Meta:#this class is to order 
        ordering = ['position']

    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)  
        super().save(*args, **kwargs)  

    def get_absolute_url(self):
        return reverse("programmes:lessonlist", kwargs={"slug": self.matiere.slug, "niveau": self.niveau.slug})


class Commentaire(models.Model):
    nom_lesson = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE, related_name='comments')
    nom_comm = models.CharField(max_length=100, blank=True)
    # reponse = models.ForeignKey('Commentaire', null=True, blank=True, on_delete=models.CASCADE, related_name='reponses')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    corps = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.nom_comm = slugify("commented by " + str(self.auteur) + "at " + str(self.date_added) )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom_comm

    class Meta:
        ordering = ['-date_added']        


class Reponse(models.Model):
    nom_comm = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name='reponses')      
    corps = models.TextField(max_length=500)  
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to" + str(self.nom_comm.nom_comm)