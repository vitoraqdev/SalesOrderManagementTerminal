import requests
from requests import Response

"""
           Pratos
-----------------------------
1. Adicionar prato
2. Editar prato
3. Remover prato
4. Listar pratos
5. Voltar


      Adicionar prato
-----------------------------
Nome:
Preço:
Descrição:
Deseja adicionar outro prato? (s/n)


        Editar prato
-----------------------------
(listar prato)
ID do prato:
Nome:
Preço
Descrição:
Deseja editar outro prato? (s/n)


        Remover prato
-----------------------------
(listar pedidos)
ID do prato:
Deseja remover o prato? (s/n)


        Listar prato
-----------------------------
[1] Pizza - R$ 20.00 - Pizza de calabresa
[2] Refrigerante - R$ 10.00 - Guaraná 2L
"""


class Prato:
    """Classe para chamar funções APIs no escopo dos pratos"""

    @staticmethod
    def existe_prato(id_prato: int) -> bool:
        """
        Verifica se o prato existe.
        """
        url = f"http://localhost:8000/item/{id_prato}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def pegar_prato(id_prato: int) -> Response:
        """Retorna a resposta de um request para a API. Essa função assume que o prato existe."""
        url = f"http://localhost:8000/item/{id_prato}"
        response = requests.get(url)
        return response

    @staticmethod
    def editar_prato(id_prato: int, novo_prato: dict) -> Response:
        """Editar prato."""
        url = f"http://localhost:8000/item/{id_prato}"
        response = requests.put(url, data=novo_prato)
        return response

    @staticmethod
    def remover_prato(id_prato: int) -> Response:
        """Remover prato."""
        url = f"http://localhost:8000/item/{id_prato}"
        response = requests.delete(url)
        return response

    @staticmethod
    def listar_pratos() -> None:
        """Lista os pratos."""
        url = "http://localhost:8000/item/"
        response = requests.get(url)
        if response.status_code == 200:
            for prato in response.json():
                print(f"[{prato['id']}] {prato['name']} - R$ {prato['price']:.2f} - {prato['description']} - [{prato['is_active']}]")
        else:
            print("Não foi possível listar os pratos.")


class PratoTerminal:
    """Classe terminal para pratos."""

    def __init__(self) -> None:
        """Imprime menu de pratos e chama funções."""
        print("------------------------------")
        print("            Pratos            ")
        print("------------------------------")
        print("1. Adicionar prato")
        print("2. Editar prato")
        print("3. Remover prato")
        print("4. Listar pratos")
        print("5. Voltar")
        print("------------------------------")
        opcao = input("Opção: ")
        if opcao == "1":
            self.adicionar_prato()
        elif opcao == "2":
            self.editar_prato()
        elif opcao == "3":
            self.remover_prato()
        elif opcao == "4":
            self.listar_pratos()
        elif opcao == "5":
            return

    def adicionar_prato(self) -> None:
        """Adicionar prato."""
        print("------------------------------")
        print("            Pratos            ")
        print("------------------------------")
        nome = input("Nome: ")
        preco = input("Preço: ")
        descricao = input("Descrição: ")
        resposta = requests.post("http://localhost:8000/item",
                                 data={"name": nome, "price": preco, "description": descricao, "is_active": True})
        if resposta.status_code == 200:
            print("Prato adicionado com sucesso.")
        else:
            print("Não foi possível adicionar o prato.")

        if input("Deseja adicionar outro prato? (s/n) ") == "s":
            self.adicionar_prato()

    def editar_prato(self) -> None:
        """Editar prato."""
        print("-----------------------------")
        print("        Editar prato         ")
        print("-----------------------------")

        self.listar_pratos()

        id_prato = input("ID do prato: ")
        # verifica se id_prato é inteiro
        if not id_prato.isdigit():
            print("ID inválido.")
            return

        # verifica se prato existe
        if not Prato.existe_prato(int(id_prato)):
            print("Prato não existe.")
            return

        prato_antigo = Prato.pegar_prato(int(id_prato)).json()

        print("Digite os novos dados do prato. (Deixe em branco para não alterar)")
        print(prato_antigo["name"])
        nome = input("Novo nome: ")
        if nome == "":
            nome = prato_antigo["name"]

        print(prato_antigo["price"])
        preco = input("Novo preço: ")
        if preco == "":
            preco = prato_antigo["price"]

        print(prato_antigo["description"])
        descricao = input("Nova descrição: ")
        if descricao == "":
            descricao = prato_antigo["description"]

        print(prato_antigo["is_active"])
        ativo = input("Novo status: ")
        if ativo == "":
            ativo = prato_antigo["is_active"]

        novo_prato = {"name": nome, "price": preco, "description": descricao, "is_active": ativo}
        resposta = Prato.editar_prato(int(id_prato), novo_prato)

        if resposta.status_code == 200:
            print("Prato editado com sucesso.")
        else:
            print("Erro ao editar prato.")
            print(resposta)

        if input("Deseja editar outro prato? (s/n) ") == "s":
            self.editar_prato()

    def remover_prato(self) -> None:
        """Remover prato."""
        print("-----------------------------")
        print("        Remover prato        ")
        print("-----------------------------")

        self.listar_pratos()

        id_prato = input("ID do prato: ")
        # verifica se id_prato é inteiro
        if not id_prato.isdigit():
            print("ID inválido.")
            return

        # verifica se prato existe
        if not Prato.existe_prato(int(id_prato)):
            print("Prato não existe.")
            return

        prato = Prato.pegar_prato(int(id_prato)).json()
        print(prato)

        # confirma remoção
        if input(f"Deseja remover o prato `{prato['name']}`? (s/n) ") != "s":
            return

        resposta = Prato.remover_prato(int(id_prato))

        if resposta.status_code == 200:
            print("Prato removido com sucesso.")
        else:
            print("Erro ao remover prato.")
            print(resposta)

        if input("Deseja remover outro prato? (s/n) ") == "s":
            self.remover_prato()

    def listar_pratos(self) -> None:
        """Listar pratos."""
        Prato.listar_pratos()
