from domain.models.producto import Producto
from domain.models.cliente import Cliente
from domain.services.servicio_pedido import ServicioPedido

class UserController():
    def __init__(self):
        self.servicio_pedido = {}
        self.clientes = {}  # id -> Cliente
    
    def hello(self):
        return 'Hello, World! from controller'
    
    def main(self):
        # Crear repositorio y servicio
        servicio_pedido = ServicioPedido()
        # Crear productos y cliente
        producto1 = Producto(id=1, nombre='Camiseta', precio=19.99)
        producto2 = Producto(id=2, nombre='Pantalón', precio=39.99)
        cliente = Cliente(id=1, nombre='Juan Pérez')

        # Crear un pedido y agregar productos
        pedido = servicio_pedido.crear_pedido(cliente)
        servicio_pedido.agregar_producto_a_pedido(pedido.id, producto1, 2)
        servicio_pedido.agregar_producto_a_pedido(pedido.id, producto2, 1)
        return pedido.__repr__()
    