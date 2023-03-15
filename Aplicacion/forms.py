from django import forms
from Aplicacion.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
         