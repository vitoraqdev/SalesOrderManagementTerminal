"""
Python terminal to be used with github.com/vitoraqdev/SalesOrderManagement
"""

"""
Menu Principal
------------------------------
Pedidos: #
------------------------------
1. Pedidos
2. Clientes
3. Endereços
4. Bairros
5. Pratos
6. Motoboys
7. Dados
8. Sair
"""

from pedido import PedidoTerminal


class MenuTerminal:
    """
    Classe que representa o menu principal.
    """
    @staticmethod
    def menu_principal() -> None:
        """
        Menu principal.
        """
        print("------------------------------")
        print("        Menu Principal        ")
        print("------------------------------")
        print("1. Pedidos")
        print("2. Clientes")
        print("3. Endereços")
        print("4. Bairros")
        print("5. Pratos")
        print("6. Motoboys")
        print("7. Dados")
        print("8. Sair")
        print("------------------------------")



if __name__ == "__main__":
    MenuTerminal.menu_principal()
    opcao = int(input("Opção: "))
    if opcao == 1:
        PedidoTerminal()
