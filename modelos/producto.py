class Producto:
    def __init__(self, codigo, nombre, precio, stock=0):
        self._codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.__stock = stock
        
    def __validar_cantidad(self, cantidad):
        return isinstance(cantidad, int) and cantidad > 0 #True o False
    
    def hay_stock(self):
        return self.__stock > 0
    
    def reducir_stock(self):
        if not self.hay_stock():
            return False
        self.__stock -= 1
        return True
    
    def reabastecer(self, cantidad):
        if not self.__validar_cantidad(cantidad):
            return "La cantidad ingresada no es correcta"
        self.__stock += cantidad
        return f"{self.nombre} reabastecido. Nuevo stock: {self.__stock}"
    
    def info(self):
        estado = "Disponible" if self.hay_stock() else "AGOTADO"
        return f"[{self._codigo} {self.nombre:<12} ${self.precio:<5} -> {estado}]"
    