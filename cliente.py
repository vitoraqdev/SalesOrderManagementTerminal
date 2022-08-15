import requests
import unittest


class Cliente:
    """Classe para chamar funções APIs no escopo dos clientes"""

    @staticmethod
    def cliente_existe(nome_cliente: str) -> bool:
        """
        Verifica se o cliente existe.
        """
        url = f"http://localhost:8000/customer/{nome_cliente}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False


class TesteCliente(unittest.TestCase):
    """Classe para testar a classe Cliente"""

    def test_positive(self) -> None:
        """Verifica que o cliente de teste 'Vitor' existe"""
        self.assertTrue(Cliente.cliente_existe("Vitor"), "Cliente 'Vitor' não existe.")

    def test_negative(self) -> None:
        """Verifica que o cliente 'abcdef' não existe"""
        self.assertFalse(Cliente.cliente_existe("abcdef"), "Cliente 'abcdef' existe.")


if __name__ == '__main__':
    unittest.main()
