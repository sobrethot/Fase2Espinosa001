from django.test import TestCase
from base.models import Autor,Post

class AutorModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Autor.objects.create(name='Accion', summary='Prueba')
    
    def test_name_label(self):
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_summary_label(self):
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')
    
    def test_name_max_length(self):
        autor=Autor.objects.get(id=1)
        max_length = autor._meta.get_field('name').max_length
        self.assertEquals(max_length,100)
    
    def test_summary_max_length(self):
        autor=Autor.objects.get(id=1)
        max_length = autor._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)
        
    def test_get_absolute_url(self):
        autor=Autor.objects.get(id=1)
        self.assertEquals(autor.get_absolute_url(), '/base/autor/')


