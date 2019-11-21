import unittest
from Consulta import consulta, normalizar_str, retorno_chat




class ConsultaTestCase(unittest.TestCase):

    def test_resultado_consulta(self):
        resultado = consulta('Napoleão')

        # testa se o valor retornado não é None.
        self.assertNotEqual(resultado, 'Desculpe, não entendi')

    def test_chat(self):
        resultado = retorno_chat('Quem é Napoleão')

        # testa se o valor retornado não é None.
        self.assertNotEqual(resultado, 'Desculpe, não entendi')

    def test_chat_resposta_invalida(self):
        resultado = retorno_chat('ola')

        # testa se o valor retornado não é None.
        self.assertEqual(str(resultado), 'ola, tudo bem?')

    def test_normalizacao(self):
        query = "Quem foi Napoleão"
        self.assertEqual(normalizar_str(query), 'napoleão')



if __name__ == "__main__":
     unittest.main()
