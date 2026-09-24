import datetime
from .producto import Producto
class MaquinaExpendedora:
    total_maquinas = 0
    total_ventas = 0
    
    def __init__(self, modelo,pin_admin):
        self._modelo = modelo
        self.__dinero = 0
        self.__pin_admin = str(pin_admin)
        self.productos = []
        
        MaquinaExpendedora.total_maquinas += 1
        
    def __validar_pin(self, pin):
        return str(pin) == self.__pin_admin

    def __buscar_producto(self, codigo):
        for p in self.productos:
            if p._codigo.upper() == codigo.upper():
                return p
        return None
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos")
            return
        for p in self.productos:
            print(p.info())
            
    def comprar(self, codigo, dinero):
        producto = self.__buscar_producto(codigo)
        if producto is None:
            return "Codigo no encontrado"
        if not producto.hay_stock():
            return f"{producto.nombre} esta agotado"
        if dinero < producto.precio:
            return f"Dinero insuficiente. Necesitas {producto.precio}"
        
        producto.reducir_stock()
        self.__dinero += producto.precio
        MaquinaExpendedora.total_ventas += 1
        
        cambio = dinero - producto.precio
        fecha = datetime.date.today()
        return f"Compraste: {producto.nombre}, Tu cambio es {cambio}. Venta efectuada: {fecha}"
    
    def reabastecer(self, codigo, cantidad, pin):
        if not self.__validar_pin(pin):
            return "Pin incorrecto"
        producto = self.__buscar_producto(codigo)
        if producto is None:
            return "Codigo no encontrado"
        return producto.reabastecer(cantidad)
    
    def ver_dinero(self, pin):
        if not self.__validar_pin(pin):
            return "Pin Incorrecto"
        return f"Dinero acumulado: {self.__dinero:.2f}"
