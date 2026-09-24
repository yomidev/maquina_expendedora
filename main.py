#from modelos.producto import Producto
#from modelos.maquina import MaquinaExpendedora
from modelos import Producto, MaquinaExpendedora

def buscar_producto(maquina, codigo):
    for p in maquina.productos:
        if p._codigo.upper() == codigo.upper():
            return p
    return None

def menu_usuario(maquina):
    maquina.mostrar_productos()
    print()
    codigo = input("Codigo del producto: ").strip()
    try:
        dinero = float(input("Cuanto dinero insertas?: "))
    except ValueError:
        print("Debes ingresar un numero")
        return
    print(maquina.comprar(codigo, dinero))
    
def menu_admin(maquina):
    pin = input("PIN del Admin: ").strip()
    print("1. Reabastecer producto")
    print("2. Ver Dinero")
    opcion = input("Opcion").strip()
    if opcion == "1":
        codigo = input("Codigo del producto: ").strip()
        try:
            cantidad = int(input("Cantidad a reabastecer: "))
        except ValueError:
            print("Debe de ingresar un numero entero")
            return
        print(maquina.reabastecer(codigo, cantidad, pin))
        
    elif opcion == "2":
        print(maquina.ver_dinero(pin))
    else: 
        print("Opcion no valida")
        
def menu(maquina):
    while True:
        print("\n" + "="*45)
        print("MAQUINA EXPENDEDORA 10")
        print("\n" + "="*45)
        print("1. Ver productos")
        print("2. Comprar productos")
        print("3. Modo Admin")
        print("4. Ver estadisticas")
        print("5. Salir")
        
        opcion = input("Ingresa una opcion: ")
        if opcion == "1":
            maquina.mostrar_productos()
        elif opcion == "2":
            menu_usuario(maquina)
        elif opcion == "3":
            menu_admin(maquina)
        elif opcion == "4":
            print(f"Maquinas creadas: {MaquinaExpendedora.total_maquinas}")
            print(f"Total de ventas: {MaquinaExpendedora.total_ventas}")
        elif opcion == "5":
            print("Saliendo")
            break
        else:
            print("Opcion no valida")
            
maquina = MaquinaExpendedora("MOD0001", "1234")
producto = Producto("A1", "Papas", 15, stock=3)
producto1 = Producto("A2", "Refresco", 20, stock=2)
producto2 = Producto("B1", "Chocolate", 12, stock=1)
producto3 = Producto("B2", "Galletas", 10, stock=0)
producto4 = Producto("C1", "Agua", 8, stock=5)


maquina.agregar_producto(producto)
maquina.agregar_producto(producto1)
maquina.agregar_producto(producto2)
maquina.agregar_producto(producto3)
maquina.agregar_producto(producto4)

menu(maquina)
