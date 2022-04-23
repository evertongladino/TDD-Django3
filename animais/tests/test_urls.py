from django.test import RequestFactory, TestCase
from django.urls import reverse
from animais.views import index

class AnimaisURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        """Teste se a home utiliza a função index da view"""
        request = self.factory.get('/')
        with self.assertTemplateUsed('animais/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)