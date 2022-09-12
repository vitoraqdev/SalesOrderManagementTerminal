import requests
import unittest
from typing import Any

"""
           clientes
-----------------------------
1. Adicionar cliente
2. Editar cliente
3. Remover cliente
4. Listar clientes
5. Voltar


      Adicionar cliente
-----------------------------
Nome:
Telefone:
ID do endereço:
Deseja adicionar outro cliente? (s/n)


        Editar cliente
-----------------------------
(listar clientes)
ID do cliente:
Nome:
Telefone:
ID do endereço:
Deseja editar outro cliente? (s/n)


        Remover cliente
-----------------------------
(listar clientes)
ID do cliente:
Deseja remover o cliente? (s/n)


        Listar clientes
-----------------------------
[1] João - (11) 99999-9999 - 1
[2] Maria - (11) 99999-9999 - 2
"""
class Customer:
    """Classe para chamar funções APIs no escopo dos clientes"""

    @staticmethod
    def exists(customer_id: str) -> bool:
        """
        Verifica se o cliente existe.
        """
        url = f"http://localhost:8000/customer/{customer_id}"
        response = requests.get(url)
        return response.ok

    @staticmethod
    def get(customer_id: int) -> Any:
        """
        Retorna o cliente.
        """
        url = f"http://localhost:8000/customer/{customer_id}"
        response = requests.get(url)
        return response.json()

    @staticmethod
    def create(data: dict) -> Any:
        """
        Adiciona um cliente.
        """
        url = f"http://localhost:8000/customer/"
        request = requests.post(url, data=data)
        return request.json()

    @staticmethod
    def edit(customer_id: int, data: dict) -> None:
        """Edita um cliente."""
        url = f"http://localhost:8000/customer/{customer_id}"
        requests.put(url, data=data)

    @staticmethod
    def delete(customer_id: int) -> bool:
        """Removes a customer"""
        url = f"http://localhost:8000/customer/{customer_id}"
        request = requests.delete(url)
        return request.ok

    @staticmethod
    def list() -> None:
        """Lista todos os clientes"""
        url = f"http://localhost:8000/customer/"
        response = requests.get(url)
        if response.ok:
            for customer in response.json():
                print(customer)


class CustomerTerminal:
    """Classe para chamar funções de terminal no escopo dos clientes"""
    
    def __init__(self) -> None:
        print("------------------------------")
        print("           Clientes           ")
        print("------------------------------")
        print("1. Adicionar cliente")
        print("2. Editar cliente")
        print("3. Remover cliente")
        print("4. Listar clientes")
        print("5. Voltar")
        print("------------------------------")
        
        option = input("Digite a opção desejada: ")
        if option == "1":
            self.add()
        elif option == "2":
            self.edit()
        elif option == "3":
            self.remove()
        elif option == "4":
            self.list()
        else:
            return

    @staticmethod
    def add() -> None:
        """Adiciona um cliente"""
        print("------------------------------")
        print("     Adicionar cliente       ")
        print("------------------------------")
        name = input("Nome: ")
        phone = input("Telefone: ")
        address_id = input("ID do endereço: ")

        data = {
            "name": name,
            "phone": phone,
            "address_id": address_id,
        }

        Customer.create(data)

        more = input("Deseja adicionar outro cliente? (s/n) ")
        if more.lower() == "s":
            CustomerTerminal.add()

    @staticmethod
    def edit() -> None:
        """Edita um cliente"""
        print("------------------------------")
        print("       Editar cliente        ")
        print("------------------------------")
        CustomerTerminal.list()
        customer_id = int(input("ID do cliente: "))
        Customer.get(customer_id)
        name = input("Nome: ")
        phone = input("Telefone: ")
        address_id = input("ID do endereço: ")

        data = {
            "name": name,
            "phone": phone,
            "address_id": address_id,
        }

        Customer.edit(customer_id, data)

        more = input("Deseja editar outro cliente? (s/n) ")
        if more.lower() == "s":
            CustomerTerminal.edit()

    @staticmethod
    def remove() -> None:
        """Remove um cliente"""
        print("------------------------------")
        print("      Remover cliente        ")
        print("------------------------------")
        CustomerTerminal.list()
        customer_id = int(input("ID do cliente: "))

        confirm = input("Deseja remover o cliente? (s/n) ")
        if confirm.lower() == "s":
            Customer.delete(customer_id)

        more = input("Deseja remover outro cliente? (s/n) ")
        if more.lower() == "s":
            CustomerTerminal.remove()

    @staticmethod
    def list() -> None:
        """Lista todos os clientes"""
        print("------------------------------")
        print( "      Listar clientes        ")
        print("------------------------------")
        Customer.list()
        
        


class TesteCliente(unittest.TestCase):
    """Classe para testar a classe Cliente"""

    def test_positive(self) -> None:
        """Verifica que o cliente de teste 'Vitor' existe"""
        self.assertTrue(Customer.exists("Vitor"), "Cliente 'Vitor' não existe.")

    def test_negative(self) -> None:
        """Verifica que o cliente 'abcdef' não existe"""
        self.assertFalse(Customer.exists("abcdef"), "Cliente 'abcdef' existe.")


if __name__ == '__main__':
    unittest.main()
