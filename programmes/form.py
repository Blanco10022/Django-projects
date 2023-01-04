from django import forms
from django.forms import widgets
from .models import Lesson, Commentaire, Reponse

class LessonForm(forms.ModelForm):
    class Meta():
        model = Lesson
        fields = ('lesson_id', 'nom', 'video','image', 'fpe', 'pdf', 'position')

class ComForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('corps',)
        labels = {'corps': 'Comments'}
        widgets = {
            'corps':forms.Textarea(attrs={
                'class':'form-control',
                'rows':4,
                'cols':70,
                'placeholder':'Enter your comments here.'
            })
        }        

class RepForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ('corps',)
        labels = {'corps': 'Reply'}
        widgets = {
            'corps':forms.Textarea(attrs={
                'class':'form-control',
                'rows':2,
                'cols':10,
                'placeholder':'Reply to comment here.'
            })
        }              