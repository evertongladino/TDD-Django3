from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

class indexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_retorna_caracteristicas_do_animal(self):
        """Teste que verifica se a index retorna as caracteristica do animal pesquisado"""
        