from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from user_control.models import User


class TestViews(TestCase):
    def setUp(self):
        u = User(username='test')
        u.set_password('1234')
        u.save()
        self.client.post(reverse('login'), {'username': 'test', 'password': '1234'})

    def test_actions(self):
        r = self.client.post('/', {'original_url': 'google.com'})  # Создание
        r = self.client.get('/')
        self.assertEqual(len(r.context['urls']), 1)

        short_url_code = r.context['urls'][0]['short_url']  # перенаправление на исходный урл
        r = self.client.get(f'/{short_url_code}/')
        self.assertEqual(r.url, 'http://google.com')

        r = self.client.get('/')  # кол-во визитов
        self.assertEqual(r.context['urls'][0]['number_of_visits'], 1)

        r = self.client.post(reverse('remove_url'), {'name': short_url_code})  # удаление
        r = self.client.get('/')
        self.assertEqual(len(r.context['urls']), 0)
        r = self.client.get(f'/{short_url_code}/')
        self.assertEqual(r.status_code, 404)

    def test_len_short_url(self):
        for i in range(1000):
            r = self.client.post('/', {'original_url': f'google{i}.com'}, follow=True)
            self.assertEqual(len(r.context['urls'][0]['short_url']), settings.LENGTH_SHORT_URL, f'iter: {i}')




