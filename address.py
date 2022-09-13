"""
          Endereços
-----------------------------
1. Adicionar endereço
2. Editar endereço
3. Remover endereço
4. Listar endereços
5. Voltar


      Adicionar endereço
-----------------------------
Rua:
Número:
ID do bairro:
Complemento (Ex.: Casa 1):
Observação (Ex.: Portão verde):
Taxa de entrega:
Deseja adicionar outro endereço? (s/n)


        Editar endereço
-----------------------------
(listar endereços)
ID do endereço:
Rua:
Número:
ID do bairro:
Complemento (Ex.: Casa 1):
Observação (Ex.: Portão verde):
Taxa de entrega:
Deseja editar outro endereço? (s/n)


        Remover endereço
-----------------------------
(listar endereços)
ID do endereço:
Deseja remover o endereço? (s/n)


        Listar endereços
-----------------------------
[1] Rua 1, 100 - 1 - Casa 1 - Portão verde. Taxa de entrega: R$ 5.00
[2] Rua 2, 200 - 2 - Casa 2 - Portão azul. Taxa de entrega: R$ 10.00
"""
from typing import Any

import requests

import bairro


class Address:
    """Classe para chamar funções APIs no escopo dos endereços"""

    @staticmethod
    def exists(id_address: int) -> bool:
        """
        Verifica se o endereço existe.
        """
        url = f"http://localhost:8000/address/{id_address}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def get(id_address: int) -> Any:
        """
        Retorna o endereço.
        """
        url = f"http://localhost:8000/address/{id_address}"
        response = requests.get(url)
        if response.ok:
            return response.json()
        else:
            return None

    @staticmethod
    def create(data: dict) -> Any:
        """
        Cria um endereço.
        """
        url = "http://localhost:8000/address"
        response = requests.post(url, data=data)
        return response

    @staticmethod
    def update(id_address: int, data: dict) -> Any:
        """
        Atualiza um endereço.
        """
        url = f"http://localhost:8000/address/{id_address}"
        response = requests.put(url, data=data)
        return response

    @staticmethod
    def delete(id_address: int) -> bool:
        """
        Deleta um endereço.
        """
        url = f"http://localhost:8000/address/{id_address}"
        response = requests.delete(url)
        return response.ok

    @staticmethod
    def list() -> Any:
        """
        Lista todos os endereços.
        """
        url = "http://localhost:8000/address"
        response = requests.get(url)
        for address in response.json():
            print(f"[{address['id']}] {address['street']}, {address['number']} - {address['neighborhood_id']} - {address['complement']} - {address['observation']}. Taxa de entrega: R$ {address['delivery_fee']:0.2f}")



class AddressTerminal:
    """Classe para chamar funções APIs no escopo dos endereços"""
    def __init__(self):
        """Inicializa a classe"""
        print("------------------------------")
        print("          Endereços           ")
        print("------------------------------")
        print("1. Adicionar endereço")
        print("2. Editar endereço")
        print("3. Remover endereço")
        print("4. Listar endereços")
        print("5. Voltar")
        print("------------------------------")

        opcao = input("Opção: ")
        if opcao == "1":
            self.add()
        elif opcao == "2":
            self.edit()
        elif opcao == "3":
            self.remove()
        elif opcao == "4":
            self.list()
        else:
            return

    @staticmethod
    def add() -> None:
        """Adiciona um endereço"""
        while True:
            print("------------------------------")
            print("      Adicionar endereço      ")
            print("------------------------------")
            street = input("Rua: ")
            number = input("Número: ")
            bairro.Bairro.listar_bairros()
            neighborhood_id = input("ID do bairro: ")
            complement = input("Complemento (Ex.: Casa 1): ")
            observation = input("Observação (Ex.: Portão verde): ")
            delivery_fee = input("Taxa de entrega: ")

            data = {
                "street": street,
                "number": number,
                "neighborhood_id": neighborhood_id,
                "complement": complement,
                "observation": observation,
                "delivery_fee": delivery_fee,
            }

            response = Address.create(data)
            print(response.text)

            if input("Deseja adicionar outro endereço? (s/n): ") == "n":
                return

    @staticmethod
    def edit() -> None:
        """Edita um endereço"""
        while True:
            print("------------------------------")
            print("        Editar endereço       ")
            print("------------------------------")
            Address.list()
            id_address = int(input("ID do endereço: "))
            address = Address.get(id_address)

            street = input("Rua: ")
            if street:
                address["street"] = street

            number = input("Número: ")
            if number:
                address["number"] = number

            bairro.Bairro.listar_bairros()
            neighborhood_id = input("ID do bairro: ")
            if neighborhood_id:
                address["neighborhood_id"] = neighborhood_id

            complement = input("Complemento (Ex.: Casa 1): ")
            if complement:
                address["complement"] = complement

            observation = input("Observação (Ex.: Portão verde): ")
            if observation:
                address["observation"] = observation

            delivery_fee = input("Taxa de entrega: ")
            if delivery_fee:
                address["delivery_fee"] = delivery_fee

            response = Address.update(id_address, address)
            print(response.text)

            if input("Deseja editar outro endereço? (s/n): ") == "n":
                return

    @staticmethod
    def remove() -> None:
        """Remove um endereço"""
        while True:
            print("------------------------------")
            print("       Remover endereço       ")
            print("------------------------------")
            Address.list()
            id_address = int(input("ID do endereço: "))

            if input("Deseja remover o endereço? (s/n): ") == "n":
                return

            if Address.delete(id_address):
                print("Endereço removido com sucesso.")
            else:
                print("Erro ao remover endereço.")

    @staticmethod
    def list() -> None:
        """Lista os endereços"""
        print("------------------------------")
        print("       Listar endereços       ")
        print("------------------------------")
        Address.list()