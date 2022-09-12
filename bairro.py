import requests
from requests import Response

from customer import Client

"""
           Bairros
-----------------------------
1. Adicionar bairro
2. Editar bairro
3. Remover bairro
4. Listar bairros
5. Voltar


      Adicionar bairro
-----------------------------
Nome:
Taxa de entrega: R$ 
Deseja adicionar outro bairro? (s/n)


        Editar bairro
-----------------------------
(listar bairros)
ID do bairro:
Nome:
Taxa de entrega: R$ 
Deseja editar outro bairro? (s/n)


        Remover bairro
-----------------------------
(listar bairros)
ID do bairro:
Deseja remover o bairro? (s/n)


        Listar bairros
-----------------------------
[1] Ipiranga - R$ 3.00
[2] Liberdade - R$ 6.00
"""


class Bairro:
    """Classe para chamar funções APIs no escopo dos bairros"""

    @staticmethod
    def existe_bairro(id_bairro: int) -> bool:
        """
        Verifica se o bairro existe.
        """
        url = f"http://localhost:8000/address/neighborhood/{id_bairro}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def pegar_bairro(id_bairro: int) -> Response:
        """Retorna a resposta de um request para a API. Essa função assume que o bairro existe."""
        url = f"http://localhost:8000/address/neighborhood/{id_bairro}"
        response = requests.get(url)
        return response

    @staticmethod
    def editar_bairro(id_bairro: int, novo_bairro: dict) -> Response:
        """Editar bairro."""
        url = f"http://localhost:8000/address/neighborhood/{id_bairro}"
        response = requests.put(url, data=novo_bairro)
        return response

    @staticmethod
    def remover_bairro(id_bairro: int) -> Response:
        """Remover bairro."""
        url = f"http://localhost:8000/address/neighborhood/{id_bairro}"
        response = requests.delete(url)
        return response

    @staticmethod
    def listar_bairros() -> None:
        """Lista os bairros."""
        url = "http://localhost:8000/address/neighborhood/"
        response = requests.get(url)
        if response.status_code == 200:
            for bairro in response.json():
                print(f"[{bairro['id']}] {bairro['name']} - R$ {bairro['delivery_fee']}")
        else:
            print("Não foi possível listar os bairros.")


class BairroTerminal:
    """Classe terminal para bairros."""

    def __init__(self) -> None:
        """Imprime menu de bairros e chama funções."""
        print("------------------------------")
        print("           Bairros            ")
        print("------------------------------")
        print("1. Adicionar bairro")
        print("2. Editar bairro")
        print("3. Remover bairro")
        print("4. Listar bairros")
        print("5. Voltar")
        print("------------------------------")
        opcao = input("Opção: ")
        if opcao == "1":
            self.adicionar_bairro()
        elif opcao == "2":
            self.editar_bairro()
        elif opcao == "3":
            self.remover_bairro()
        elif opcao == "4":
            self.listar_bairros()
        elif opcao == "5":
            return

    def adicionar_bairro(self) -> None:
        """Adicionar bairro."""
        print("------------------------------")
        print("           Bairros            ")
        print("------------------------------")
        nome = input("Nome: ")
        taxa_de_entrega = input("Taxa de entrega: R$ ")

        resposta = requests.post("http://localhost:8000/address/neighborhood",
                                 data={"name": nome, "delivery_fee": taxa_de_entrega})
        if resposta.status_code == 200:
            print("Bairro adicionado com sucesso.")
        else:
            print("Não foi possível adicionar o bairro.")

        if input("Deseja adicionar outro bairro? (s/n) ") == "s":
            self.adicionar_bairro()

    def editar_bairro(self) -> None:
        """Editar bairro."""
        print("-----------------------------")
        print("        Editar bairro        ")
        print("-----------------------------")

        self.listar_bairros()

        id_bairro = input("ID do bairro: ")
        # verifica se id_bairro é inteiro
        if not id_bairro.isdigit():
            print("ID inválido.")
            return

        # verifica se bairro existe
        if not Bairro.existe_bairro(int(id_bairro)):
            print("Bairro não existe.")
            return

        bairro_antigo = Bairro.pegar_bairro(int(id_bairro)).json()

        print("Digite os novos dados do bairro. (Deixe em branco para não alterar)")
        print(bairro_antigo["name"])
        nome = input("Novo nome: ")
        if nome == "":
            nome = bairro_antigo["name"]

        print(bairro_antigo["delivery_fee"])
        taxa_de_entrega = input("Nova taxa de entrega: R$ ")
        if taxa_de_entrega == "":
            taxa_de_entrega = bairro_antigo["delivery_fee"]

        novo_bairro = {"name": nome, "delivery_fee": taxa_de_entrega}

        resposta = Bairro.editar_bairro(int(id_bairro), novo_bairro)

        if resposta.status_code == 200:
            print("Bairro editado com sucesso.")
        else:
            print("Erro ao editar bairro.")
            print(resposta)

        if input("Deseja editar outro bairro? (s/n) ") == "s":
            self.editar_bairro()

    def remover_bairro(self) -> None:
        """Remover bairro."""
        print("-----------------------------")
        print("        Remover bairro       ")
        print("-----------------------------")

        self.listar_bairros()

        id_bairro = input("ID do bairro: ")
        # verifica se id_bairro é inteiro
        if not id_bairro.isdigit():
            print("ID inválido.")
            return

        # verifica se bairro existe
        if not Bairro.existe_bairro(int(id_bairro)):
            print("Bairro não existe.")
            return

        bairro = Bairro.pegar_bairro(int(id_bairro)).json()
        print(bairro)

        # confirma remoção
        if input(f"Deseja remover o bairro `{bairro['name']}`? (s/n) ") != "s":
            return

        resposta = Bairro.remover_bairro(int(id_bairro))

        if resposta.status_code == 200:
            print("Bairro removido com sucesso.")
        else:
            print("Erro ao remover bairro.")
            print(resposta)

        if input("Deseja remover outro bairro? (s/n) ") == "s":
            self.remover_bairro()

    def listar_bairros(self) -> None:
        """Listar bairros."""
        Bairro.listar_bairros()
