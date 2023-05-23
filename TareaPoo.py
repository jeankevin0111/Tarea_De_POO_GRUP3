import math
import time
class Producto:
    def __init__(self, nombre, tipo, cantidad, minimo, precio_base):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.cantMinima = minimo
        self.precio_base = precio_base

    def calcular_precio_final(self):
        impuestos = {
            "papeleria": 0.16,
            "supermercado": 0.04,
            "drogueria": 0.12
        }
        impuesto = impuestos.get(self.tipo.lower(), 0)
        return self.precio_base * (1 + impuesto)


    def vender(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            if self.cantidad > self.cantMinima:
                return True
        else:
            return False

    def abastecer(self, cantidad):
        self.cantidad += cantidad

    def __str__(self):
        return f"Nombre: {self.nombre}\nTipo: {self.tipo}\nCantidad: {self.cantidad}\nMínimo: {self.cantMinima}\nPrecio Base: {self.precio_base}"
################################################################################################################
class Tienda:
    def __init__(self):
        self.productos = [ Producto("Marcadores", "papeleria", 50, 10, 10),Producto("Atún", "supermercado", 100, 20, 5),Producto("Paracetamol", "drogueria", 80, 15, 3),Producto("Graduador", "papeleria", 30, 5, 20)]
        self.procesos= []
        self.dinero=0
        self.usuario=None
    def menuPrincipal(self,usuario):
        menuPrincipal= True
        print("\033[30;43;1m"+usuario.__str__()+"\033[0;m")
        while menuPrincipal:
            self.verProductos()
            print("\033[30;41;1m"+"Menú del sistema"+"\033[0;m")
            print("1:Vender un producto\n"
                  "2:Abastecer la tienda con un producto.\n"
                  "3:Calcular estadísticas de ventas")
            seleccion = input("Ingrese un opcion:   ")
            if seleccion == "1":
                self.vender_producto()
            elif seleccion == "2":
                self.abastecer_producto()
            elif seleccion == "3":
                self.calcular_estadisticas_ventas()
            else:
                print("\033[30;41;1m"+"El dato ingresado es incorrecto, intente de nuevo"+"\033[0;m")


    def agregar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                return False
        self.productos.append(producto)
        return True

    def verProductos(self):
        print("Selecciona uno de los productos")
        print("------------------------")
        contador=0
        for producto in self.productos:
            contador+=1
            print("\033[30;43;1m"+f"Producto #{contador}"+"\033[0;m")
            print("---------")
            print(producto)
            time.sleep(0.5)
            print("------------------------")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def vender_producto(self):
        print("------------------------")
        producto0=input("ingrese Nombre del producto:  ")
        cantidad=int(input("Ingrese la cantidad deseada:  "))
        producto = self.buscar_producto(producto0)
        if producto:
            if producto.vender(cantidad):
                vender=producto.calcular_precio_final() * cantidad
                self.dinero+=vender
                print(f"Venta exitosa. Total a pagar: ${round(vender, 2) }")
                self.procesos.append(producto0)
                time.sleep(3)
            else:
                print("No hay suficiente cantidad disponible para la venta.")
                time.sleep(3)
        else:
            print("El producto no se encuentra en la tienda.")
            time.sleep(3)


    def abastecer_producto(self):
        print("------------------------")
        producto0 = input("ingrese Nombre del producto:  ")
        cantidad = int(input("Ingrese la cantidad deseada abastecer:  "))
        producto = self.buscar_producto(producto0)
        if producto:
            producto.abastecer(cantidad)
            print("\033[30;41;1m"+f"Se han abastecido {cantidad} unidades del producto {producto.nombre}."+"\033[0;m")
            print("------------------------------------------")
            time.sleep(3)
        else:
            print("El producto no se encuentra en la tienda.")
            time.sleep(3)

    def calcular_estadisticas_ventas(self):
        mas_vendido = None
        menos_vendido = None
        total_ventas = 0
        numero_producto_vendido = 0

        if len(self.procesos) == 0:
            print("\033[30;43;1m"+"No se han realizado ventas."+"\033[0;m")
            input()
            print("--------------------------------------")
            return
        Ventas_individuales = {}
        for nombreProducto in self.procesos:
            if nombreProducto not in Ventas_individuales:
                Ventas_individuales[nombreProducto] = 1
            else:
                Ventas_individuales[nombreProducto] += 1

        for producto in self.productos:
            CantidadVentas = Ventas_individuales.get(producto.nombre, 0)
            total_ventas += CantidadVentas * producto.calcular_precio_final()
            numero_producto_vendido += CantidadVentas

            if mas_vendido is None or CantidadVentas > Ventas_individuales.get(mas_vendido.nombre,0):
                mas_vendido = producto

            if menos_vendido is None or CantidadVentas < Ventas_individuales.get(menos_vendido.nombre, 0):
                menos_vendido = producto
        if numero_producto_vendido > 0:
            proVenta = total_ventas / numero_producto_vendido
        else:
            proVenta = 0

        print("Estadísticas de Ventas:")
        print(f"Producto más vendido: {mas_vendido.nombre}")
        print(f"Producto menos vendido: {menos_vendido.nombre}")
        print(f"Cantidad total de dinero obtenido por las ventas de la tienda: ${round(self.dinero, 2)}")
        print(f"Cantidad de dinero promedio obtenido por unidad de producto vendida: ${round(proVenta, 2)}")
        input()
class Usuario:
    def __init__(self,nombre,apellido,correo):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
    def __str__(self):
        return f"Bienvenido {self.nombre} {self.apellido}   correo:{self.correo}"

usuario=Usuario("Admin","Admin","admin@gmail.com")
tienda = Tienda()




tienda.menuPrincipal(usuario)




