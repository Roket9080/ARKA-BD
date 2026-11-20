from django.test import TestCase
from django.urls import reverse

from .models import Profesional


class InicioTests(TestCase):
    def test_inicio_redirige_al_formulario_de_registro(self):
        response = self.client.get('/', follow=True)

        self.assertRedirects(response, reverse('registro_profesional'))
        self.assertTemplateUsed(response, 'app_sebas/registro_profesional.html')


class EditarProfesionalTests(TestCase):
    def setUp(self):
        self.profesional = Profesional.objects.create(
            identificador='profesional-01',
            contrasena='clave-privada',
            nombres='Ana',
            apellidos='García',
            correo='ana@example.com',
            telefono='5551234',
            contacto_emergencia='5559876',
            disponibilidad_horarios='Lunes a viernes',
            direccion='Calle Principal 123',
        )

    def test_formulario_edicion_muestra_datos_sin_revelar_contrasena(self):
        response = self.client.get(
            reverse('editar_profesional', args=[self.profesional.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'value="profesional-01"')
        self.assertContains(response, 'value="Ana"')
        self.assertContains(response, 'value="García"')
        self.assertContains(response, 'value="ana@example.com"')
        self.assertNotContains(response, 'value="clave-privada"')

    def test_editar_sin_contrasena_conserva_la_actual(self):
        response = self.client.post(
            reverse('editar_profesional', args=[self.profesional.pk]),
            {
                'identificador': 'profesional-01',
                'contrasena': '',
                'nombres': 'Ana María',
                'apellidos': 'García',
                'correo': 'ana.maria@example.com',
                'telefono': '5551234',
                'contacto_emergencia': '5559876',
                'disponibilidad_horarios': 'Lunes a viernes',
                'direccion': 'Calle Principal 123',
            },
        )

        self.assertRedirects(response, reverse('lista_profesional'))
        self.profesional.refresh_from_db()
        self.assertEqual(self.profesional.nombres, 'Ana María')
        self.assertEqual(self.profesional.correo, 'ana.maria@example.com')
        self.assertEqual(self.profesional.contrasena, 'clave-privada')

# Create your tests here.
