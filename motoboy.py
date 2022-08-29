import requests
from requests import Response

"""
          Motoboys
-----------------------------
1. Adicionar motoboy
2. Editar motoboy
3. Remover motoboy
4. Listar motoboys
5. Voltar


      Adicionar motoboy
-----------------------------
Nome:
Telefone:
Salário diário:
Deseja adicionar outro motoboy? (s/n)


        Editar motoboy
-----------------------------
(listar motoboy)
ID do motoboy:
Nome:
Telefone:
Salário diário:
Deseja editar outro motoboy? (s/n)


        Remover motoboy
-----------------------------
(listar pedidos)
ID do motoboy:
Deseja remover o motoboy? (s/n)


        Listar motoboy
-----------------------------
[1] João - (11) 99999-9999 - R$ 100.00
[2] Maria - (11) 99999-9999 - R$ 200.00
"""


class Motoboy:
    """Classe para chamar funções APIs no escopo dos motoboys"""

    @staticmethod
    def existe_motoboy(id_motoboy: int) -> bool:
        """
        Verifica se o motoboy existe.
        """
        url = f"http://localhost:8000/motoboy/{id_motoboy}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def pegar_motoboy(id_motoboy: int) -> Response:
        """Retorna a resposta de um request para a API. Essa função assume que o motoboy existe."""
        url = f"http://localhost:8000/motoboy/{id_motoboy}"
        response = requests.get(url)
        return response

    @staticmethod
    def editar_motoboy(id_motoboy: int, novo_motoboy: dict) -> Response:
        """Editar motoboy."""
        url = f"http://localhost:8000/motoboy/{id_motoboy}"
        response = requests.put(url, data=novo_motoboy)
        return response

    @staticmethod
    def remover_motoboy(id_motoboy: int) -> Response:
        """Remover motoboy."""
        url = f"http://localhost:8000/motoboy/{id_motoboy}"
        response = requests.delete(url)
        return response

    @staticmethod
    def listar_motoboys() -> None:
        """Lista os motoboys."""
        url = "http://localhost:8000/motoboy/"
        response = requests.get(url)
        if response.status_code == 200:
            for motoboy in response.json():
                print(f"[{motoboy['id']}] {motoboy['name']} - R$ {motoboy['daily_salary']:.2f} - {motoboy['phone']} - [{motoboy['is_active']}]")
        else:
            print("Não foi possível listar os motoboys.")


class MotoboyTerminal:
    """Classe terminal para motoboys."""

    def __init__(self) -> None:
        """Imprime menu de motoboys e chama funções."""
        print("------------------------------")
        print("           Motoboys           ")
        print("------------------------------")
        print("1. Adicionar motoboy")
        print("2. Editar motoboy")
        print("3. Remover motoboy")
        print("4. Listar motoboys")
        print("5. Voltar")
        print("------------------------------")
        opcao = input("Opção: ")
        if opcao == "1":
            self.adicionar_motoboy()
        elif opcao == "2":
            self.editar_motoboy()
        elif opcao == "3":
            self.remover_motoboy()
        elif opcao == "4":
            self.listar_motoboys()
        elif opcao == "5":
            return

    def adicionar_motoboy(self) -> None:
        """Adicionar motoboy."""
        print("------------------------------")
        print("           Motoboys           ")
        print("------------------------------")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        salario_diario = input("Salário diário: ")

        resposta = requests.post("http://localhost:8000/motoboy",
                                 data={'name': nome, 'phone': telefone, 'daily_salary': salario_diario, 'is_active': True})
        if resposta.status_code == 200:
            print("Motoboy adicionado com sucesso.")
        else:
            print("Não foi possível adicionar o motoboy.")

        if input("Deseja adicionar outro motoboy? (s/n) ") == "s":
            self.adicionar_motoboy()

    def editar_motoboy(self) -> None:
        """Editar motoboy."""
        print("-----------------------------")
        print("        Editar motoboy       ")
        print("-----------------------------")

        self.listar_motoboys()

        id_motoboy = input("ID do motoboy: ")
        # verifica se id_motoboy é inteiro
        if not id_motoboy.isdigit():
            print("ID inválido.")
            return

        # verifica se motoboy existe
        if not Motoboy.existe_motoboy(int(id_motoboy)):
            print("Prato não existe.")
            return

        motoboy_antigo = Motoboy.pegar_motoboy(int(id_motoboy)).json()

        print("Digite os novos dados do motoboy. (Deixe em branco para não alterar)")
        print(motoboy_antigo["name"])
        nome = input("Novo nome: ")
        if nome == "":
            nome = motoboy_antigo["name"]

        print(motoboy_antigo["phone"])
        telefone = input("Novo telefone: ")
        if telefone == "":
            telefone = motoboy_antigo["phone"]

        print(motoboy_antigo["daily_salary"])
        salario_diario = input("Novo salário diário: ")
        if salario_diario == "":
            salario_diario = motoboy_antigo["daily_salary"]

        print(motoboy_antigo["is_active"])
        ativo = input("Novo status: ")
        if ativo == "":
            ativo = motoboy_antigo["is_active"]

        novo_motoboy = {'name': nome, 'phone': telefone, 'daily_salary': salario_diario, 'is_active': ativo}
        resposta = Motoboy.editar_motoboy(int(id_motoboy), novo_motoboy)

        if resposta.status_code == 200:
            print("Prato editado com sucesso.")
        else:
            print("Erro ao editar motoboy.")
            print(resposta)

        if input("Deseja editar outro motoboy? (s/n) ") == "s":
            self.editar_motoboy()

    def remover_motoboy(self) -> None:
        """Remover motoboy."""
        print("-----------------------------")
        print("        Remover motoboy        ")
        print("-----------------------------")

        self.listar_motoboys()

        id_motoboy = input("ID do motoboy: ")
        # verifica se id_motoboy é inteiro
        if not id_motoboy.isdigit():
            print("ID inválido.")
            return

        # verifica se motoboy existe
        if not Motoboy.existe_motoboy(int(id_motoboy)):
            print("Prato não existe.")
            return

        motoboy = Motoboy.pegar_motoboy(int(id_motoboy)).json()
        print(motoboy)

        # confirma remoção
        if input(f"Deseja remover o motoboy `{motoboy['name']}`? (s/n) ") != "s":
            return

        resposta = Motoboy.remover_motoboy(int(id_motoboy))

        if resposta.status_code == 200:
            print("Prato removido com sucesso.")
        else:
            print("Erro ao remover motoboy.")
            print(resposta)

        if input("Deseja remover outro motoboy? (s/n) ") == "s":
            self.remover_motoboy()

    def listar_motoboys(self) -> None:
        """Listar motoboys."""
        Motoboy.listar_motoboys()
