import json

import requests
from customer import Customer
import datetime
from pedido_detalhes import PedidoDetalhes
from typing import Any

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



class Pedido:
    """Classe para chamar funções APIs no escopo dos pedidos"""
    @staticmethod
    def exists(id_pedido: int) -> bool:
        """
        Verifica se o pedido existe.
        """
        url = f"http://localhost:8000/order/{id_pedido}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def get(order_id: int) -> Any:
        """
        Retorna o pedido.
        """
        url = f"http://localhost:8000/order/{order_id}"
        response = requests.get(url)
        return response.json()

    @staticmethod
    def create(data: dict) -> Any:
        """
        Adiciona um pedido.
        """
        url = f"http://localhost:8000/order/"
        request = requests.post(url, data=data)
        return request.json()

    @staticmethod
    def edit(id_pedido: int, data: dict) -> None:
        """Edita um pedido."""
        url = f"http://localhost:8000/order/{id_pedido}"
        requests.put(url, data=data)

    @staticmethod
    def delete(order_id: int) -> bool:
        """Removes an order"""
        url = f"http://localhost:8000/order/{order_id}"
        request = requests.delete(url)
        return request.ok

    @staticmethod
    def list() -> None:
        """Lista todos os pedidos"""
        url = f"http://localhost:8000/order/"
        response = requests.get(url)
        if response.ok:
            for order in response.json():
                print(order) # better print format todo?
        else:
            print("Erro ao listar pedidos.")

class PedidoTerminal:
    """
    Classe que representa o terminal de pedidos.
    """

    def __init__(self) -> None:
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

        opcao = input("Opção: ")
        if opcao == "1":
            self.adicionar_pedido()
        elif opcao == "2":
            self.editar_pedido()
        elif opcao == "3":
            self.remover_pedido()
        elif opcao == "4":
            self.listar_pedidos()
        else:
            return

    @staticmethod
    def adicionar_pedido() -> None:
        """Adiciona um pedido."""
        print("-----------------------------")
        print("      Adicionar pedido       ")
        print("-----------------------------")

        # CUSTOMER_ORDER
        date = datetime.date.today().strftime("%Y-%m-%d")

        Customer.list()
        client_id = input("ID do cliente: ")

        # Motoboy.listar_motoboys()
        motoboy_id = input("ID do motoboy: ")

        # Endereço.listar_enderecos()
        address_id = input("ID do endereço: ")

        source = input("Plataforma (Whatsapp: 0, iFood: 1, Litoral na Mesa: 2): ")

        additional = input("Adicional: ")

        delivery_fee = input("Taxa de entrega: ")

        discount = input("Desconto: ")

        status = input("Status (Pendente: 0, Pago: 1, Cancelado: 2): ")

        # enviar pro backend
        pedido = {
            "date": date,
            "customer_id": client_id,
            "motoboy_id": motoboy_id,
            "address_id": address_id,
            "source": source,
            "additional": additional,
            "delivery_fee": delivery_fee,
            "discount": discount,
            "status": status
        }

        new_order = Pedido.create(pedido)


        # ORDER_DETAILS
        order_id = new_order["id"]

        # Prato.listar_pratos()
        while True:
            item_id = input("ID do prato: ")
            quantity = input("Quantidade: ")
            pedido_detalhes = {
                "order_id": order_id,
                "item_id": item_id,
                "quantity": quantity
            }
            PedidoDetalhes.add(pedido_detalhes)
            if input("Deseja adicionar outro prato? (s/n)") == "n":
                break

    @staticmethod
    def editar_pedido() -> None:
        """Edita um pedido."""
        print("-----------------------------")
        print("        Editar pedido        ")
        print("-----------------------------")
        PedidoTerminal.listar_pedidos()
        order_id = int(input("ID do pedido: "))
        order = Pedido.get(order_id)

        # CUSTOMER_ORDER
        print("------------------------------")
        print("1. Data: ", order["date"])
        new_date = input("Nova data: ")
        if new_date:
            order["date"] = new_date

        print("2. Cliente: ", order["customer_id"])
        new_client_id = input("Novo cliente: ")
        if new_client_id:
            order["customer_id"] = new_client_id

        print("3. Motoboy: ", order["motoboy_id"])
        new_motoboy_id = input("Novo motoboy: ")
        if new_motoboy_id:
            order["motoboy_id"] = new_motoboy_id

        print("4. Endereço: ", order["address_id"])
        new_address_id = input("Novo endereço: ")
        if new_address_id:
            order["address_id"] = new_address_id

        print("5. Plataforma: ", order["source"])
        new_source = input("Nova plataforma: ")
        if new_source:
            order["source"] = new_source

        print("6. Adicional: ", order["additional"])
        new_additional = input("Novo adicional: ")
        if new_additional:
            order["additional"] = new_additional

        print("7. Taxa de entrega: ", order["delivery_fee"])
        new_delivery_fee = input("Nova taxa de entrega: ")
        if new_delivery_fee:
            order["delivery_fee"] = new_delivery_fee

        print("8. Desconto: ", order["discount"])
        new_discount = input("Novo desconto: ")
        if new_discount:
            order["discount"] = new_discount

        print("9. Status: ", order["status"])
        new_status = input("Novo status: ")
        if new_status:
            order["status"] = new_status

        Pedido.edit(order_id, order)


        # ORDER_DETAILS
        print("------------------------------")
        while True:
            PedidoDetalhes.list(order_id)
            item_id = input("ID do prato: ")
            quantity = input("Quantidade: ")
            unit_price = input("Preço unitário: ")
            pedido_detalhes = {
                "order_id": order_id,
                "item_id": item_id,
                "quantity": quantity,
                "unit_price": unit_price
            }
            PedidoDetalhes.edit(order_id, pedido_detalhes)
            if input("Deseja editar outro prato? (s/n): ") == "n":
                break

    @staticmethod
    def remover_pedido() -> None:
        """Remove um pedido."""
        print("-----------------------------")
        print("        Remover pedido       ")
        print("-----------------------------")
        PedidoTerminal.listar_pedidos()
        id_pedido = int(input("ID do pedido: "))
        if not Pedido.exists(id_pedido):
            print("Pedido não existe.")
            return
        if input("Deseja remover o pedido? (s/n): ") == "s":
            if Pedido.delete(id_pedido):
                print("Pedido removido com sucesso.")
            else:
                print("Erro ao remover pedido.")

    @staticmethod
    def listar_pedidos() -> None:
        """Lista os pedidos."""
        Pedido.list()
