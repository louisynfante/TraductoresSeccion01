""" Realice un programa que permita cargar una lista con articulos y sus precios, 
el usuario debe comprar dichos articulos,
y debes imprimir el total de ventas con su iva"""

def lista():
    acum=0
    opc=""
    print "Bienvenido al mini MercadoVideosGame online"
    lista={"Televisor":350000,"Celular":46000,"Tablet":220000,"Computadora":650000}
    for x,y in lista.iteritems():
        print x,"=",y
    print "Ingrese el Nombre del cliente:"
    cliente=raw_input()
    for x,y in lista.iteritems():
        print cliente," Deseas comprar",x,"a",y,"bs"
        print "Presione s/n"
        opc=raw_input()
        opc=opc.lower()
        if (opc=="s"):
            acum=acum+y
        
    iva=(acum*12)/100
    total=acum+iva
    print "El costo de tu compra es:",acum,"bs"
    print "el iva es:",iva,"bs"
    print "total facturacion es:",total,"bs"
     
lista()