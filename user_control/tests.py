from django.test import TestCase
from django.urls import reverse


class TestView(TestCase):
    def test_registration(self):
        c = self.client
        r = c.post(reverse('registration'), {
            'username': 'test',
            'email': 'test@mail.ru',
            'password1': '1q2s3e4f',
            'password2': '1q2s3e4f'
        }, follow=True)

        self.assertEqual(r.context['user'].username, 'test')
        c.get(reverse('logout'))
        r = c.post(reverse('login'), {'username': 'test', 'password': '1q2s3e4f'}, follow=True)
        self.assertEqual(r.context['user'].username, 'test')
