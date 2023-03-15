from django import forms
from Aplicacion.models import Post, Alumno, Profesor

class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = '__all__'
          

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'