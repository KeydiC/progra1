class Producto():
    def __init__(self,nombre,precio_base,stock):
        self.nombre=nombre
        self.precio_base=precio_base
        self.stock=stock
    
    def aplicar_descuento(self,porcentaje):
        self.precio_base*=(1-porcentaje)
        print (f"el nuevo precio del producto {self.nombre} es: {self.precio_base}")
    
    
    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0:
            print("no hay suficiente stock")
        else:
           self.stock+=cantidad
           print(f"el nuuevo stock de {self.nombre} es {self.stock}")

class Categoria(): 
    def __init__(self,nombre_categoria):
        self.nombre_categoria= nombre_categoria
        self.lista=[]

    def agregar_producto(self,producto):
        self.lista.append(producto)
        print(f"El producto {producto.nombre} se agrego a la lista")

    def valor_total_categoria(self):
        suma=0
        for m in self.lista:
            suma+=m.precio_base*m.stock
        print(f"El precio total {self.nombre_categoria} es {suma} pesos")


class Pedido():
    def __init__(self,cliente):
        self.cliente=cliente
        self.lista_comprados=[]
        self.estado="Pendiente"
    
    def agregar_producto(self,product):
        self.lista_comprados.append(product)
        print (f"Agregaste el producto {product.nombre} al carrito")

    def calcular_total(self):
        total=0
        for x in self.lista_comprados:
            total+=x.precio_base
        print(f"El total de productos comprados es ${total}, el iva es ${0.16*total} y dando sumado {1.16*total:0.2f}")

    def finalizar_pedido(self,listab):
        self.estado="Completado"
        for x in self.lista_comprados:
            for y in listab:
                if x.nombre==y.nombre:
                    y.stock-=1
                    print(f"Al producto {y.nombre} se le quito un elemento")