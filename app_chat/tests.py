from django.test import TestCase
from django.urls import reverse

from app_sebas.models import Profesional
from .models import ChatGrupal


class CrearChatTests(TestCase):
    def setUp(self):
        self.profesional = Profesional.objects.create(
            identificador='profesional-chat-01',
            contrasena='clave-privada',
            nombres='Ana',
            apellidos='García',
            correo='ana@example.com',
            telefono='5551234',
            contacto_emergencia='5559876',
            disponibilidad_horarios='Lunes a viernes',
            direccion='Calle Principal 123',
        )

    def test_formulario_muestra_campos_necesarios_para_crear_chat(self):
        response = self.client.get(reverse('crear_chat'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="nombre_grupo"')
        self.assertContains(response, 'name="creado_por"')

    def test_crear_chat_guarda_el_nombre_y_el_profesional(self):
        response = self.client.post(
            reverse('crear_chat'),
            {
                'nombre_grupo': 'Equipo de guardia',
                'creado_por': self.profesional.pk,
            },
        )

        self.assertRedirects(response, reverse('lista_chats'))
        self.assertEqual(ChatGrupal.objects.count(), 1)
        chat = ChatGrupal.objects.get()
        self.assertEqual(chat.nombre_grupo, 'Equipo de guardia')
        self.assertEqual(chat.creado_por, self.profesional)

    def test_datos_incompletos_muestran_errores_sin_crear_chat(self):
        response = self.client.post(reverse('crear_chat'), {'nombre_grupo': ''})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'aria-invalid="true"')
        self.assertEqual(ChatGrupal.objects.count(), 0)
