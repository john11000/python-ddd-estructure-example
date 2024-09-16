from domain.models.cliente import Cliente
from domain.models.pedido import Pedido
from domain.models.producto import Producto
from domain.repository.repositorio_pedidos import RepositorioPedidos

class ServicioPedido:
    def __init__(self):
        self.pedidos = {}  # id -> Pedido
        self.next_id = 1

    def crear_pedido(self, cliente: Cliente) -> Pedido:
        pedido = Pedido(id=self.next_id, cliente=cliente)
        self.pedidos[self.next_id] = pedido
        self.next_id += 1
        return pedido

    def obtener_pedido(self, id: int) -> Pedido:
        return self.pedidos.get(id)

    def agregar_producto_a_pedido(self, id_pedido: int, producto: Producto, cantidad: int):
        pedido = self.obtener_pedido(id_pedido)
        if pedido:
            pedido.agregar_producto(producto, cantidad)
