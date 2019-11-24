#Calcular el salario de una enfermera
#Donde su salario se calcula de la siguiente manera
#Nro Dias Trabajados x Costo por Dia
#Se le suma las horas extras, cada hora extra vale 10 soles
#Mostrar la boleta de pago

# Declaracion variables
empleado,nrodias,costo,horas_extra,monto="",0,0.0,0,0.0

# INPUT
empleado=input("Ingrese el nombre del empleado:")
nrodias=int(input("Ingrese nro de dias:"))
costo=float(input("Ingrese costo por dia:"))
horas_extra=int(input("Ingrese nro de horas extra:"))

# PROCESSING
monto=(nrodias*costo)+(horas_extra*10)

# OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Empleado: ",empleado,"   #")
print("# NroDias   : ",nrodias,"       #")
print("# CostoxDia : ",costo,"         #")
print("# HorasExtra: ",horas_extra,"   #")
print("###########################")
print("# Monto a Pagar: ",monto,"     #")
print("###########################")

#Calcular el descuento de un producto
#donde el descuento de un producto se calcula de la siguiente manera
#costo_del_producto por descuento
#mostrar el descuento

#Declaracion de variables
cliente,producto,costo_del_producto,descuento,total="","",0.0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese el producto:")
costo_del_producto=float(input("Ingrese costo del producto:"))
descuento=float(input("Ingrese descuento:"))

#PROCESSING
total=costo_del_producto-descuento

#OUTPUT
print("#################################")
print("#        Boleta de pago         #")
print("#################################")
print("# cliente: ",cliente,"   #")
print("# producto: ",producto,"          #")
print("# costo del producto: ",costo_del_producto,"     #")
print("# descuento: ",descuento,"           #")
print("###########################")
print("# total: S/. ",total,"     #")
print("################################")


#Calcular el precio al por mayor
#Donde el precio se calcula de la siguiente manera
#costo_del_producto por docena
#Mostrar la boleta de pago

#Declaracion variables
cliente,producto,costo_del_producto,docena,total="","",0.0,0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese el producto:")
costo_del_producto=float(input("Ingrese costo del producto:"))
docena=float(input("Ingrese la docena:"))

#PROCESSING
total=costo_del_producto*docena

#OUTPUT
print("#################################")
print("#        Boleta de pago         #")
print("#################################")
print("# cliente: ",cliente,"   #")
print("# producto: ",producto,"        #")
print("# costo del producto: ",costo_del_producto,"   #")
print("# docena: ",docena,"           #")
print("###########################")
print("# total: S/. ",total,"     #")
print("################################")


#Calcular el valor del euro a soles
#Donde el precio se calcula
#costo_del_euro en soles
# Mostrar el calculo

# Declaracion variables
cliente,cant,costo_euro,total="",0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
cant=int(input("Ingrese cantidad:"))
costo_euro=float(input("Ingrese costo del euro:"))

# PROCESSING
total=cant*costo_euro

# OUTPUT
print("###########################")
print("#    Total en soles     #")
print("###########################")
print("# cliente: ",cliente,"   #")
print("# cantidad: ",cant,"          #")
print("# costo del euro: ",costo_euro,"     #")
print("###########################")
print("# total: ",total,"     #")
print("###########################")


#Calcular el alquiler  por tiendas en el Boulevard
#Donde la ganancia se calcula de la siguiente forma
#costo_del_alquiler
#Mostrar el calculo

# Declaracion variables
cliente,cant,costo_de_alquiler,total="",0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
cant=int(input("Ingrese cantidad:"))
costo_de_alquiler=float(input("Ingrese costo de alquiler:"))


# PROCESSING
total=cant*costo_de_alquiler

# OUTPUT
print("#################################")
print("#   Total ganado por alquiler   #")
print("#################################")
print("# cliente: ",cliente,"       #")
print("# cantidad: ",cant,"         #")
print("# Costo de alquiler: ",costo_de_alquiler,"   #")
print("###########################")
print("# total: ",total,"     #")
print("###########################")



#Detector de calidad de telas
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario

#DETECTOR
# Sera comprador compulsivo cuando el total > 110
calidad_de_tela=(total > 110)

#OUTPUT
print("###########################")
print("#         Boleta          #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# producto: ",producto, "  #")
print("# cantidad: ",cant,"       #")
print("# costoUnitario: S/. ",costo_unitario," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# calidad de tela: ",calidad_de_tela,  "#")
print("############################")



#Detector de marcas originales
cliente,producto,cant,costo_unit,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese el producto:")
cant=int(input("Ingrese cantidad:"))
costo_unit=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unit

#DETECTOR
# Sera marcas originiales cuando el total > 300
marcas_originales=(total > 300)

#OUTPUT
print("###########################")
print("#         Boleta          #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# producto: ",producto, "  #")
print("# cantidad: ",cant,"       #")
print("# costoUnitario: S/. ",costo_unit," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# marcas originales: ",marcas_originales,  "#")
print("############################")



#Detector de consumo de gasolina en un vehiculo
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario

#DETECTOR
# Sera comprador compulsivo cuando el total > 150
consumo_de_gasolina=(total > 150)

#OUTPUT
print("###########################")
print("#         Boleta          #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# producto: ",producto, "  #")
print("# cantidad: ",cant,"       #")
print("# costoUnitario: S/. ",costo_unitario," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# consumo de gasolina de un vehiculo: ",consumo_de_gasolina," #")
print("############################")




#Detector de comprador compulsivo
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario

#DETECTOR
# Sera comprador compulsivo cuando el total > 160
comprador_compulsivo=(total > 160)

#OUTPUT
print("###########################")
print("#         Factura         #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# producto: ",producto, "  #")
print("# cantidad: ",cant,"       #")
print("# costoUnitario: S/. ",costo_unitario," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# comprador compulsivo: ",comprador_compulsivo,  "#")
print("############################")



#Detector de calidad de electrodomesticos
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario

#DETECTOR
# Sera comprador compulsivo cuando el total > 200
calidad_de_electrodomesticos=(total > 200)

#OUTPUT
print("###########################")
print("#         Factura         #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# producto: ",producto, "  #")
print("# cantidad: ",cant,"       #")
print("# costoUnitario: S/. ",costo_unitario," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# calidad de electrodomesticos: ",calidad_de_electrodomesticos,  "#")
print("############################")



#Detector de calidad de tortas
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario

#DETECTOR
# Sera comprador compulsivo cuando el total > 70
calidad_de_tortas=(total > 70)

#OUTPUT
print("###########################")
print("#         Boleta          #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# producto: ",producto, "  #")
print("# cantidad: ",cant,"       #")
print("# costoUnitario: S/. ",costo_unitario," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# calidad de tortas: ",calidad_de_tortas,  "#")
print("############################")




#Detector de calidad de alimentos
cliente,productos,cant,precios,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
productos=input("Ingrese productos:")
cant=int(input("Ingrese cantidades:"))
precios=float(input("Ingrese precios:"))

#PROCESSING
total=cant*precios

#DETECTOR
# Sera alimentos de calidad cuando el total > 300
calidad_de_alimentos=(total > 300)

#OUTPUT
print("###########################")
print("#         Boleta          #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# productos: ",productos, "  #")
print("# cantidad: ",cant,"       #")
print("# precios: S/. ",precios," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# calidad de alimentos: ",calidad_de_alimentos,  "#")
print("############################")



#Detector de consumo de bebidas alto en azucar
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario

#DETECTOR
# Sera consumidor compulsivo cuando el total > 15 a diario
consumo_de_gaseosas=(total > 15)

#OUTPUT
print("###########################")
print("#         Boleta          #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# producto: ",producto, "  #")
print("# cantidad: ",cant,"       #")
print("# costoUnitario: S/. ",costo_unitario," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# consumo de gaseosas: ",consumo_de_gaseosas," #")
print("############################")



#Detector de consumo de comida chatarra
cliente,producto,cant,costo_unitario,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_unitario=float(input("Ingrese costo unitario:"))

#PROCESSING
total=cant*costo_unitario

#DETECTOR
# Sera consumidor compulsivo cuando el total > 30 a diario
consumo_de_comida_chatarra=(total > 30)

#OUTPUT
print("###########################")
print("#         Boleta          #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# producto: ",producto, "  #")
print("# cantidad: ",cant,"       #")
print("# costoUnitario: S/. ",costo_unitario," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# consumo de comida chatarra: ",consumo_de_comida_chatarra," #")
print("############################")



#Detector de consumo de energia
cliente,producto,cant,costo,total="","",0,0.0,0.0

#INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo=float(input("Ingrese costo:"))

#PROCESSING
total=cant*costo

#DETECTOR
# Sera consumidor compulsivo cuando el total > 100
consumo_de_energia=(total > 100)

#OUTPUT
print("###########################")
print("#         Recibo de Luz   #")
print("###########################")
print("# cliente: ",cliente,"    #")
print("# producto: ",producto, "  #")
print("# cantidad: ",cant,"       #")
print("# costo: S/. ",costo," #")
print("############################")
print("#   Total: S/. ",total,"      #")
print("# consumo de energia: ",consumo_de_energia," #")
print("############################")

