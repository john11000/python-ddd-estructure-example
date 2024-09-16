class Cliente:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

    def __repr__(self):
        return f"Cliente(id={self.id}, nombre='{self.nombre}')"
