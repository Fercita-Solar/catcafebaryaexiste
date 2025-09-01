from django.test import TestCase
from django.urls import reverse

class MainViewsTests(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')

    def test_quienes_somos_view(self):
        response = self.client.get(reverse('quienes_somos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/quienes_somos.html')

    def test_noticias_ofertas_view(self):
        response = self.client.get(reverse('news_sales'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/news_sales.html')

    def test_galeria_view(self):
        response = self.client.get(reverse('galeria'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/galeria.html')