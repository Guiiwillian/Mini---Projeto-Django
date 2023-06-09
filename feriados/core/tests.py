from django.test import TestCase

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/natal')

    def test_200_response(self):
        self.assertEqual(200,self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp,'natal')

    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'natal.html')

class TiradentesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tiradentes')

    def test_200_response(self):
        self.assertEqual(200,self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp,'Tiradentes')

    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'tiradentes.html')


# Create your tests here.
