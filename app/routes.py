from domain.models.producto import Producto
from domain.models.cliente import Cliente
from domain.services.servicio_pedido import ServicioPedido
from infraestructure.database.repository.repositorio_pedidos import RepositorioPedidosEnMemoria

# Crear repositorio y servicio
# repositorio = RepositorioPedidosEnMemoria()
servicio_pedido = ServicioPedido()

# Crear productos y cliente
producto1 = Producto(id=1, nombre='Camiseta', precio=19.99)
producto2 = Producto(id=2, nombre='Pantalón', precio=39.99)
cliente = Cliente(id=1, nombre='Juan Pérez')

# Crear un pedido y agregar productos
pedido = servicio_pedido.crear_pedido(cliente)
servicio_pedido.agregar_producto_a_pedido(pedido.id, producto1, 2)
servicio_pedido.agregar_producto_a_pedido(pedido.id, producto2, 1)
print(pedido.__repr__())
# Mostrar el pedido
# pedido_guardado = repositorio.obtener(pedido.id)
# print(pedido_guardado)
# print(f"Total del pedido: {pedido_guardado.calcular_total()}")
