from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import qrcode
from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()
ruta = "C:/Users/yesen/OneDrive/Escritorio/ExamenParcial2/"
c = canvas.Canvas(ruta +'Examen.pdf', pagesize=A4)

informacion = "Luis Javier, Materias Primas"
img = qrcode.make(informacion)
nombreImagen = ruta + "MiQR.png"
f = open(nombreImagen, "wb")
img.save(f)
f.close()
nombre = input("Ingresa el nombre del cliente: ")
direccion = input("Ingresa el direccion: ")
correo= input("Ingresa el correo electronico: ")

despensa = ["Azucar", "Harina", "Manteca", "M/Vegetal", "Levadoras"]
costo = [26,20,46,56,35]
lista = ["1.-","2.-","3.-","4.-","5.-"]
cantidades = [0,0,0,0,0]
compras = [0,0,0,0,0]
preciouni = [26,20,46,56,35]
opcion=1
contadorElementos = 0
print(" ")
print("Bienvenido Materias Primas")
print("   |Costo|     |Nombre del producto|")
for i,i2,i3 in zip (despensa, costo, lista):
       print(i3,"$",i2,"       ",i)
       
while opcion == 1:
    opcion2 = int(input("Selecciona alguno de los siguientes productos: "))
    if (opcion2==1):
        piezas = int(input("¿Cuantos kilos de Azucar? "))
        cantidades[0] = cantidades[0]+piezas
        compras[0] = (cantidades[0]*costo[0])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1.Si 2.No "))
    elif(opcion2==2):
        piezas = int(input("¿Cuantos kilos de Harina? "))
        cantidades[1] = cantidades[1]+piezas
        compras[1] = (cantidades[1]*costo[1])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==3):
        piezas = int(input("¿Cuantos kilos de Manteca? "))
        cantidades[2] = cantidades[2]+piezas
        compras[2] = (cantidades[2]*costo[2])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==4):
        piezas = int(input("¿Cuantos kilos de M/Vegetal? "))
        cantidades[3] = cantidades[3]+piezas
        compras[3] = (cantidades[3]*costo[3])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==5):
        piezas = int(input("¿Cuantas paquetes de levadoras quieres? "))
        cantidades[4] = cantidades[4]+piezas
        compras[4] = (cantidades[4]*costo[4])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    else:
        print("Producto que no esta en el menu, no esta disponible ")

print("compras: ")
print(" ")
print("|Cantidad|   |Precio del producto|   |TotalProducto|   |Nombre del producto|")

for i,i2,i3,i4 in zip(cantidades, costo, compras, despensa):
    print(" ",i,"           ","$",i2,"                  ","$",i3,"               ","$",i4,"")

TotalPagar = sum(compras)

print("El total de pagar es: $",TotalPagar)
Pago = input("Recibo $")
UsuarioPago = float(Pago)
Cambio = UsuarioPago-TotalPagar
print("El usuario pago un total de: $",UsuarioPago)
if (UsuarioPago<TotalPagar):
   print("no puedes llevar los productos")
else:
    print("Tu cambio es: $"+"{:.2f}".format(Cambio))

print("Articulos vendidos: ",contadorElementos)

now = datetime.now().replace(microsecond=0)
imagen = ruta + "LOGO.png"
c.drawImage(imagen,220,770,150,80,mask="auto")
c.setFont('Helvetica', 15)
c.drawString(220,750,"Ticket de compra")
c.setFont('Helvetica', 12)
c.setFont('Helvetica', 12)
c.drawString(120,730,f"cliente:  {nombre}")
c.drawString(120,700,f"Dirección: {direccion}")
c.drawString(120,670,f"Correo electrónico: {correo}")
c.setFont('Helvetica-Bold',16)
c.setFont('Helvetica',12)
c.drawString(120,640,f"fecha: ")
c.drawString(240,640,now.strftime("%d-%m-%Y    %H:%M:%S"))

PosX = 130
PosY = 580
c.drawString(320,580, "$")
c.drawString(320,560, "$")
c.drawString(320,540, "$")
c.drawString(320,520, "$")
c.drawString(320,500, "$")
c.drawString(390,580, "$")
c.drawString(390,560, "$")
c.drawString(390,540, "$")
c.drawString(390,520, "$")
c.drawString(390,500, "$")
for a,a2,a3,a4 in zip(despensa,cantidades,preciouni,compras):
    c.drawString(120,623, "______________________________________________")
    c.drawString(120,610, "Nombre Producto")
    c.drawString(230,610, "Cantidad")
    c.drawString(310,610, "Precio/pieza")
    c.drawString(400,610, "Total")
    c.drawString(120,608, "______________________________________________")
    c.drawString(PosX,PosY,f"{a}                       {a2}                       {a3}               {a4}")
    #PosX = PosX-10
    PosY = PosY-20
c.drawString(280,470,"Total de pagar: "+str(TotalPagar))
c.drawString(280,450,"Recibo: "+str(UsuarioPago))
if(UsuarioPago<TotalPagar):
    c.drawString(280,450,"Lo siento, pero te falta dinero para pagar el total")
else:
    c.drawString(280,430,"Cambio: "+str("{:.2f}".format(Cambio)))
    
c.drawString(280,410,"Total de productos vendidos:  "+str(contadorElementos))
c.setFont('Helvetica-Bold',20)
c.drawImage(nombreImagen,220,120,150,150)
c.setFont('Helvetica',18)


c.save()

