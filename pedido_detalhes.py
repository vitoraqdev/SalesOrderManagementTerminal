import requests


class PedidoDetalhes:
    """Classe para chamar funções APIs no escopo dos detalhes dos pedidos"""
    @staticmethod
    def exists(id_pedido: int) -> bool:
        """
        Verifica se o detalhe do pedido existe.
        """
        url = f"http://localhost:8000/order_details/{id_pedido}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def add(data: dict) -> None:
        """
        Adiciona um detalhe do pedido.
        """
        url = f"http://localhost:8000/order_details/"
        requests.post(url, data=data)

    @staticmethod
    def list(order_id: int) -> None:
        """Lista todos os detalhes do pedido"""
        url = f"http://localhost:8000/order_details/{order_id}"
        response = requests.get(url)
        if response.ok:
            for order in response.json():
                print(order)

    @staticmethod
    def edit(order_id: int, data: dict) -> None:
        """
        Edita um detalhe do pedido.
        """
        url = f"http://localhost:8000/order_details/{order_id}"
        requests.put(url, data=data)

    @staticmethod
    def remove(id_pedido: int) -> None:
        """
        Remove um detalhe do pedido.
        """
        url = f"http://localhost:8000/order_details/{id_pedido}/delete"
        requests.delete(url)
