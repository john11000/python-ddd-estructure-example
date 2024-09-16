from domain.models.pedido import Pedido
from domain.repository.repositorio_pedidos import RepositorioPedidos

class RepositorioPedidosEnMemoria(RepositorioPedidos):
    def __init__(self):
        self.pedidos = {}  # Almacena pedidos en memoria usando un diccionario

    def guardar(self, pedido: Pedido):
        """Guarda el pedido en el repositorio."""
        self.pedidos[pedido.id] = pedido

    def obtener(self, id: int) -> Pedido:
        """Obtiene un pedido por su id."""
        return self.pedidos.get(id)
