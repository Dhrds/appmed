from django.test import TestCase
from ..models import Doenca, Paciente


class DoencaTestCase(TestCase):
    def setUp(self):
        self.doenca = Doenca.objects.create(nome='dengue',
                                            sintomas='febre',
                                            descricao='teste')

    def test_doenca_nome(self):
        self.assertEqual(self.doenca.nome, 'dengue')
        self.assertEqual(self.doenca.sintomas, 'febre')
        self.assertEqual(self.doenca.descricao, 'teste')


class PacienteTestCase(TestCase):
    def setUp(self):
        self.paciente = Paciente.objects.create(
            nome='teste', sexo='masculino', idade=20,
            naturalidade='teste', onde_mora='teste',
            profissao='teste', doenca=Doenca.objects.create(
                nome='dengue', sintomas='febre', descricao='teste'))

    def test_paciente_nome(self):
        self.assertEqual(self.paciente.nome, 'teste')
