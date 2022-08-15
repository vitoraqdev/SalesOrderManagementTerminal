import requests
from cliente import Cliente

"""
           Pedidos
-----------------------------
1. Adicionar pedido
2. Editar pedido
3. Remover pedido
4. Listar pedidos
5. Voltar


      Adicionar pedido
-----------------------------
Nome:
Prato:
Quantidade:
Deseja adicionar outro prato? (s/n)


        Editar pedido
-----------------------------
(listar pedidos)
ID do pedido:
Nome:
Prato:
Quantidade:
Deseja editar outro prato? (s/n)


        Remover pedido
-----------------------------
(listar pedidos)
ID do pedido:
Deseja remover o pedido? (s/n)


        Listar pedidos
-----------------------------
[1] 01/01/2022 - João - [[Pizza, 3], [Refrigerante, 2]] - R$ 80.00
[2] 02/01/2022 - Maria - [[Pizza, 2], [Refrigerante, 1], [Adicional tomate, 2] - R$ 70.00
"""

class Pedidos:
    """Classe para chamar funções APIs no escopo dos pedidos"""
    

class PedidosTerminal:
    """
    Classe que representa o terminal de pedidos.
    """
    @staticmethod
    def menu_pedidos() -> None:
        """
        Menu de pedidos.
        """
        print("------------------------------")
        print("           Pedidos            ")
        print("------------------------------")
        print("1. Adicionar pedido")
        print("2. Editar pedido")
        print("3. Remover pedido")
        print("4. Listar pedidos")
        print("5. Voltar")
        print("------------------------------")

    @staticmethod
    def adicionar_pedido() -> None:
        """Adiciona um pedido."""
        pass

    @staticmethod
    def editar_pedido() -> None:
        """Edita um pedido."""
        pass

    @staticmethod
    def remover_pedido() -> None:
        """Remove um pedido."""
        pass

    @staticmethod
    def listar_pedidos() -> None:
        """Lista os pedidos."""
        pass

    @staticmethod
    def voltar() -> None:
        """Volta para o menu principal."""
        pass

