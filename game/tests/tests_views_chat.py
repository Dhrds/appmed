from django.test import TestCase
from django.urls import reverse


class JogoAdivinhacaoViewTest(TestCase):
    def test_get_request(self):
        # Testa se a view responde corretamente a uma requisição GET
        response = self.client.get(reverse('jogo_adivinhacao'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Olá, meu nome é José e tenho 50 anos.')

    def test_post_request(self):
        # Testa se a view responde corretamente a uma requisição POST
        data = {'mensagem': 'Sim, estou com febre.', 'reiniciar': False}
        response = self.client.post(reverse('jogo_adivinhacao'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Olá, meu nome é José e tenho 50 anos.')

    def test_reiniciar(self):
        # Testa se a view reinicia corretamente o jogo
        data = {'reiniciar': True}
        response = self.client.post(reverse('jogo_adivinhacao'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Olá, meu nome é José e tenho 50 anos.')
