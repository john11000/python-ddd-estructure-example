from typing import Dict
from domain.models.cliente import Cliente
from domain.models.producto import Producto


class Pedido:
    def __init__(self, id: int, cliente: Cliente):
        self.id = id
        self.cliente = cliente
        self.items: Dict[Producto, int] = {}  # Producto -> cantidad

    def agregar_producto(self, producto: Producto, cantidad: int):
        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad

    def calcular_total(self) -> float:
        return sum(producto.precio * cantidad for producto, cantidad in self.items.items())

    def __repr__(self):
        return f"Pedido(id={self.id}, cliente={self.cliente}, items={self.items})"