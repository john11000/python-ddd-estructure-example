from abc import ABC, abstractmethod
from domain.models.pedido import Pedido

class RepositorioPedidos(ABC):
    @abstractmethod
    def guardar(self, pedido: Pedido):
        """Guardar un pedido en el repositorio."""
        pass

    @abstractmethod
    def obtener(self, id: int) -> Pedido:
        """Obtener un pedido por su id."""
        pass
