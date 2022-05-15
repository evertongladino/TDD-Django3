from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTestCase(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(nome_animal = 'Leão', predador = True, venenoso = False, domestico = False)

    def test_animal_cadastrado_com_caracteristicas(self):
        self.assertEqual(self.animal.nome_animal, 'Leão')