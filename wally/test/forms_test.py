from django.test import TestCase
from base.forms import ContactoForm
from base.models import Contacto
from django.core.files.uploadedfile import SimpleUploadedFile

class ContactoFormsTest(TestCase):
    def test_valid_form(self):
        c = Contacto.objects.create(name='Prueba1', summary='Prueba')
        data = {'name': c.name, 'summary': c.summary,}
        form = ContactoForm(data=data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_form(self):
        c = Contacto.objects.create(name='', summary='Prueba')
        data = {'name': c.name, 'summary': c.summary,}
        form = ContactoForm(data=data)
        self.assertFalse(form.is_valid())
