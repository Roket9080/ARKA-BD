from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        label="Nombre completo",
        widget=forms.TextInput(attrs={"placeholder": "Ej. Miguel Ángel"})
    )
    email = forms.EmailField(
        required=True,
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"placeholder": "correo@ejemplo.com"})
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nombre de usuario"
        self.fields["username"].widget.attrs["placeholder"] = "Ej. miguel_arka"
        self.fields["password1"].label = "Contraseña"
        self.fields["password1"].widget.attrs["placeholder"] = "Mínimo 8 caracteres"
        self.fields["password2"].label = "Confirmar contraseña"
        self.fields["password2"].widget.attrs["placeholder"] = "Repite tu contraseña"