from django import forms

from .models import ChatGrupal


class ChatGrupalForm(forms.ModelForm):
    class Meta:
        model = ChatGrupal
        fields = ['nombre_grupo', 'creado_por']
