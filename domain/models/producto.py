class Producto:
    def __init__(self, id: int, nombre: str, precio: float):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio})"
