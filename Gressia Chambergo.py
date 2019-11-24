#Ejercicio_01
#Detector de adiccion a las redes sociales
usuario,red_social_1,red_social_2,cant_de_hora_diarias_1,cant_de_hora_diaria_2,total_de_horas_por_dia="","","",0,0,0

# INPUT
usuario=input("Ingrese nombre del usuario:")
red_social_1=input("Ingrese red social 1:")
red_social_2=input("Ingrese red social 2: ")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2

# DETECTOR
# Sera adiccion de las redes sociales si el total de horas por dia > 12
adiccion_de_las_redes_sociales=(total_de_horas_por_dia > 12)

# OUTPUT
print("###########################")
print("#       RED SOCIAL        #")
print("###########################")
print("# Usuario: ",usuario,"  #")
print("# red social 1: ",red_social_1,"        #")
print("# red social 2: ",red_social_2,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("###########################")
print("total de horas por dia:",total_de_horas_por_dia,"      #")
print("adiccion de las redes sociales:",adiccion_de_las_redes_sociales,"   #")
print("###########################")


#Ejercicio_02
#Detector de bajo rendimiento academico
alumno,horas_dedicadas_al_estudio_por_dia,total_de_horas_por_semana="",0,0

# INPUT
alumno=input("Ingrese alumno:")
horas_dedicadas_al_estudio_por_dia=int(input("Ingrese horas dedicadas al estudio por dia:"))

# PROCESSING
total_de_horas_por_semana=horas_dedicadas_al_estudio_por_dia*7

# DETECTOR
# Sera bajo rendimiento academico si el total de horas por semana < 31
bajo_rendimiento_academico=(total_de_horas_por_semana < 31)

# OUTPUT
print("###########################")
print("#  RENDIMIENTO ACADEMICO  #")
print("###########################")
print("# alumno: ",alumno,"  #")
print("# horas dedicadas al aestudio por dia: ",horas_dedicadas_al_estudio_por_dia,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# bajo rendimiento academico : ",bajo_rendimiento_academico,  "#")
print("###########################")


#Ejercicio_03
#Detector de comprador compulsivo
cliente,producto1,producto2,cant_de_producto1,cant_de_producto2,cost_uni1,cost_uni2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto1=input("Ingrese producto 1:")
producto2=input("Ingrese producto 2:")
cant_de_producto1=int(input("Ingrese cantidad de producto 1:"))
cant_de_producto2=int(input("Ingrese cantidad de producto 2:"))
costo_uni1=float(input("Ingrese costo unitario 1:"))
costo_uni2=float(input("Ingrese costo unitario 2:"))

# PROCESSING
total=cant_de_producto1*cost_uni1+cant_de_producto2*costo_uni2

# DETECTOR
# Sera comprador compulsivo si el total > 180
comprador_compulsivo=(total < 180)

# OUTPUT
print("###########################")
print("#   COSMETICOS   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto1,"        #")
print("# Producto 2: ",producto2,"        #")
print("# Cantidad de producto 1: ",cant_de_producto1,"           #")
print("# Cantidad de producto 2: ",cant_de_producto2," #")
print("# Costo Unitario 1: S/. ",costo_uni1," #")
print("# Costo Unitario 2: S/. ",costo_uni2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador compulsivo: ",comprador_compulsivo,  "#")
print("###########################")


#Ejercicio_04
#Detector de automedicacion
paciente,medicamento_1,medicamento_2,cant_de_medicamento1_por_dia,cant_de_medicamento2_por_dia,total_de_medicamentos_por_semana="","","",0,0,0

# INPUT
paciente=input("Ingrese paciente:")
medicamento_1=input("Ingrese medicamento 1: ")
medicamento_2=input("Ingrese medicamento 2: ")
cant_de_medicamento1_por_dia=int(input("Ingrese cantidad de medicamento 1 por dia:"))
cant_de_medicamento2_por_dia=int(input("Ingrese cantidad de medicamento 2 por dia:"))

# PROCESSING
total_de_medicamentos_por_semana=cant_de_medicamento1_por_dia*7+cant_de_medicamento2_por_dia*7

# DETECTOR
# Sera automedicacion si el total de medicamento por semana > 15
automedicacion=(total_de_medicamentos_por_semana > 15 )

# OUTPUT
print("###########################")
print("#       MEDICAMENTOS       #")
print("###########################")
print("# Paciente: ",paciente,"  #")
print("# medicamento 1: ",medicamento_1,"        #")
print("# medicamento 2: ",medicamento_2,"        #")
print("# cantidad de medicamento 1 por dia : ",cant_de_medicamento1_por_dia,"        #")
print("# cantidad de medicamento 2 por dia : ",cant_de_medicamento2_por_dia,"        #")
print("###########################")
print("total de medicamento por semana:",total_de_medicamentos_por_semana,"      #")
print("# automedicacion : ",automedicacion,  "#")
print("###########################")


#Ejercicio_05
#Detector de inclinacion al deporte
nombre,deporte1,deporte2,cant_de_hora_diarias_1,cant_de_hora_diarias_2,total_de_horas_por_semana="","","",0,0,0

# INPUT
nombre=input("Ingrese nombre:")
deporte1=input("Ingrese deporte 1: ")
deporte2=input("Ingrese deporte 2: ")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2

# DETECTOR
# Sera inclinacion al deporte si el total de horas por semana > 8
inclinacion_al_deporte=(total_de_horas_por_semana > 8)

# OUTPUT
print("###########################")
print("#       DEPORTE        #")
print("###########################")
print("# Nombre: ",nombre,"  #")
print("# deporte 1: ",deporte1,"        #")
print("# deporte 2: ",deporte2,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# inclinacion al deporte :",inclinacion_al_deporte,  "#")
print("###########################")


#Ejercicio_06
#Detector de comprador pasivo
cliente,producto_1,cantidad_producto_1,cost_uni_1,total="","",0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
cant_de_producto_1=int(input("Ingrese cantidad de producto 1:"))
costo_uni_1=float(input("Ingrese costo unitario 1:"))

# PROCESSING
total=cant_de_producto_1*cost_uni_1

# DETECTOR
# Sera comprador_pasivo si el total > 50
comprador_pasivo=(total > 50)

# OUTPUT
print("###########################")
print("#   ARTEFACTOS   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Cantidad de producto 1: ",cant_de_producto_1,"           #")
print("# Costo Unitario 1: S/. ",costo_uni_1," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador pasivo: ",comprador_pasivo,  "#")
print("###########################")


#Ejercicio_07
#Detector nota aprobatoria
nombre_alumno,nota_1,nota_2,nota_3,promedio="",0,0,0,0

# INPUT
nombre_alumno=input("Ingrese el nombre del alumno:")
nota_1=int(input("Ingrese nota 1:"))
nota_2=int(input("Ingrese nota 2:"))
nota_3=int(input("Ingrese nota 3:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3)/3

# DETECTOR
# Sera nota aprobatoria si el promedio > 14
nota_aprobatoria=(promedio > 14)

# OUTPUT
print("###########################")
print("#     BOLETA DE NOTA      #")
print("###########################")
print("# nombre alumno : ",nombre_alumno,"  #")
print("# nota 1: ",nota_1,"        #")
print("# nota 2: ",nota_2,"        #")
print("# nota 3: ",nota_3,"        #")
print("###########################")
print("promedio:",promedio,"      #")
print("# nota aprobatoria: ",nota_aprobatoria,  "#")
print("###########################")


#Ejercicio_08
#Detector de cumplimiento de horas de trabajo
trabajador,horas_de_jornada_laboral_por_dia,dias_de_jornada_laboral,total="",0,0,0

# INPUT
trabajador=input("Ingrese trabajador:")
horas_de_jornada_laboral_por_dia=int(input("Ingrese horas de jornada laboral por dia:"))
dias_de_jornada_laboral=int(input("Ingrese dias de jornada laboral:"))

# PROCESSING
total=horas_de_jornada_laboral_por_dia*dias_de_jornada_laboral

# DETECTOR
# Sera cumplimiento de horas de trabajo si el total de horas por semana > 42
cumplimiento_de_horas_de_trabajo=(total_de_horas_por_semana > 42 )

# OUTPUT
print("###########################")
print("#       HORAS DE TRABAJO        #")
print("###########################")
print("# trabajador: ",trabajador,"  #")
print("# horas de jornada laboral por dia: ",horas_de_jornada_laboral_por_dia,"        #")
print("# dias de jornada laboral: ",dias_de_jornada_laboral,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# cumplimiento de horas de trabajo : ",cumplimiento_de_horas_de_trabajo,  "#")
print("###########################")


#Ejercicio_09
#Detector de adiccion a la television
nombre,horas_dedicadas_a_la_television_por_dia,horas_dedicadas_a_la_television_por_semana,total="",0,0,0

# INPUT
nombre=input("Ingrese nombre:")
horas_dedicadas_a_la_television_por_dia=int(input("Ingrese horas dedicadas a la television por dia:"))
horas_dedicadas_a_la_television_por_semana=int(input("Ingrese horas dedicadas a la television por semana:"))

# PROCESSING
total=horas_dedicadas_a_la_television_por_dia*horas_dedicadas_a_la_television_por_semana

# DETECTOR
# Sera adiccion a la television si el total de horas por semana > 60
adiccion_a_la_television=(total_de_horas_por_semana > 60 )

# OUTPUT
print("###########################")
print("#       HORAS DEDICADAS A LA TELEVISION     #")
print("###########################")
print("# nombre: ",nombre,"  #")
print("# horas dedicadas a la television por dia: ",horas_dedicadas_a_la_television_por_dia,"        #")
print("# dias dedicadas a la television por semana: ",horas_dedicadas_a_la_television_por_semana,"        #")
print("###########################")
print("total :",total,"      #")
print("# adiccion a la television : ",adiccion_a_la_television,  "#")
print("###########################")


#Ejercicio_10
#Detector de adiccion al gimnasio
cliente,horas_dedicadas_al_gimnasio_por_dia,horas_dedicadas_al_gimnasio_por_semana,total="",0,0,0

# INPUT
cliente=input("Ingrese cliente:")
horas_dedicadas_al_gimnasio_por_dia=int(input("Ingrese horas dedicadas al gimnasio por dia:"))
horas_dedicadas_al_gimnasio_por_semana=int(input("Ingrese horas dedicadas al gimnasio por semana:"))

# PROCESSING
total=horas_dedicadas_al_gimnasio_por_dia*horas_dedicadas_al_gimnasio_por_semana

# DETECTOR
# Sera adiccion al gimnasio si el total de horas por semana > 50
adiccion_a_la_television=(total_de_horas_por_semana > 50 )

# OUTPUT
print("###########################")
print("#       HORAS DEDICADAS AL GIMNASIO     #")
print("###########################")
print("# cliente: ",cliente,"  #")
print("# horas dedicadas al gimnasio por dia: ",horas_dedicadas_al_gimnasio_por_dia,"        #")
print("# dias dedicadas al gimnasio por semana: ",horas_dedicadas_al_gimnasio_por_semana,"        #")
print("###########################")
print("total :",total,"      #")
print("# adiccion al gimasio : ",adiccion_al_gimnasio,"   #")
print("###########################")


#CONVERSORES
# Ejercicio_1
# Declaracion variables
trabajador,nro_dias,costo_por_dia,monto_a_pagar="",0,0.0,0.0

# INPUT
trabajador="CESAR PEREZ"
nro_dias=5
costo_por_dia=50

# PROCESSING
monto=(nro_dias*costo_por_dia)

# OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Trabajador: ",trabajador,"   #")
print("# Nro Dias   : ",nro_dias,"          #")
print("# Costo por Dia : ",costo_por_dia,"         #")
print("###########################")
print("# Monto a Pagar: ",monto_a_pagar,"     #")
print("###########################")

# Ejercicio_2
# Declaracion variables
cliente,producto_1,producto_2,costo_uni_1,costo_uni_2,cant_de_producto_1,cant_de_producto_2,total="","","",0.0,0.0,0,0,0.0

# INPUT
cliente="Karina Sanchez"
producto_1="Atun"
producto_2="Leche"
costo_uni_1=2.50
costo_uni_2=1.80
cant_de_producto_1=2
cant_de_producto_2=5

# PROCESSING
total=(costo_uni_1*cant_de_producto_1)+(costo_uni_2*cant_de_producto_2)

# OUTPUT
print("###########################")
print("#     BOLETA DE VENTA      #")
print("###########################")
print("# Cliente: ",cliente,"   #")
print("# Producto 1   : ",producto_1,"          #")
print("# Producto 2   : ",producto_2,"          #")
print("# Costo Unitario 1: ",costo_uni_1,"         #")
print("# Costo Unitario 2: ",costo_uni_2,"         #")
print("# Cantidad de Producto 1: ",cant_de_producto_1,"           #")
print("# Cantidad de Producto 2: ",cant_de_producto_2,"           #")
print("###########################")
print("# Total: ",total,"     #")
print("###########################")


# Ejercicio_3
# Declaracion variables
alumno,nota_1,nota_2,nota_3,promedio="",0,0,0,0

# INPUT
alumno="Franco Reyes"
nota_1=15
nota_2=13
nota_3=17

# PROCESSING
promedio=(nota_1+nota_2+nota_3)/3

# OUTPUT
print("###########################")
print("#     BOLETA DE NOTA      #")
print("###########################")
print("# Alumno: ",alumno,"   #")
print("# Nota 1   : ",nota_1,"          #")
print("# Nota 2   : ",nota_2,"          #")
print("# Nota 3   : ",nota_3,"          #")
print("###########################")
print("# Promedio: ",promedio,"     #")
print("###########################")

# Ejercicio_4
# Declaracion variables
paciente,medicamento_1,medicamento_2,costo_uni_1,costo_uni_2,cant_medicamento_1,cant_medicamento_2,total="","","",0.0,0.0,0,0,0.0

# INPUT
paciente="Susana Ballesteros"
medicamento_1="ibuprofeno"
medicamento_2="naproxeno"
costo_uni_1=1.20
costo_uni_2=1.00
cant_medicamento_1=7
cant_medicamento_2=4

# PROCESSING
total=(costo_uni_1*cant_medicamento_1)+(costo_uni_2*cant_medicamento_2)

# OUTPUT
print("###########################")
print("#     FACTURA     #")
print("###########################")
print("# Paciente: ",paciente,"   #")
print("# Medicamento 1   : ",medicamento_1,"          #")
print("# Medicamento 2   : ",medicamento_2,"          #")
print("# Costo Unitario 1: ",costo_uni_1,"         #")
print("# Costo Unitario 2: ",costo_uni_2,"         #")
print("# Cantidad medicamento 1: ",cant_medicamento_1,"           #")
print("# Cantidad medicamento 2: ",cant_medicamento_2,"           #")
print("###########################")
print("# Total: ",total,"     #")
print("###########################")

# Ejercicio_5
# Declaracion variables
cliente,golosina_1,golosina_2,costo_uni_1,costo_uni_2,cant_de_producto_1,cant_de_producto_2,total="","","",0.0,0.0,0,0,0.0

# INPUT
cliente="Mateo Puescas"
golosina_1="Galletas"
golosina_2="Chocolates"
costo_uni_1=0.80
costo_uni_2=1.20
cant_de_producto_1=3
cant_de_producto_2=6

# PROCESSING
total=(costo_uni_1*cant_de_producto_1)+(costo_uni_2*cant_de_producto_2)

# OUTPUT
print("###########################")
print("#     BOLETA DE VENTA      #")
print("###########################")
print("# Cliente: ",cliente,"   #")
print("# Golosina 1   : ",golosina_1,"          #")
print("# Golosina 2  : ",golosina_2,"          #")
print("# Costo Unitario 1: ",costo_uni_1,"         #")
print("# Costo Unitario 2: ",costo_uni_2,"         #")
print("# Cantidad de Producto 1: ",cant_de_producto_1,"           #")
print("# Cantidad de Producto 2: ",cant_de_producto_2,"           #")
print("###########################")
print("# Total: ",total,"     #")
print("###########################")



#IMPRESION_ASCII
#Ejercicio_01
#Declaracion de variables de adiccion a las redes sociales
usuario,red_social_1,red_social_2,cant_de_hora_diarias_1,cant_de_hora_diaria_2,total_de_horas_por_dia="","","",0,0,0

# INPUT
usuario=input("Ingrese nombre del usuario:")
red_social_1=input("Ingrese red social 1:")
red_social_2=input("Ingrese red social 2: ")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2

# OUTPUT
print("###########################")
print("#       RED SOCIAL        #")
print("###########################")
print("# Usuario: ",usuario,"  #")
print("# red social 1: ",red_social_1,"        #")
print("# red social 2: ",red_social_2,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("###########################")
print("total de horas por dia:",total_de_horas_por_dia,"      #")
print("adiccion de las redes sociales:",adiccion_de_las_redes_sociales,"   #")
print("###########################")


#Ejercicio_02
#Declaracion de variable de bajo rendimiento academico
alumno,horas_dedicadas_al_estudio_por_dia,total_de_horas_por_semana="",0,0

# INPUT
alumno=input("Ingrese alumno:")
horas_dedicadas_al_estudio_por_dia=int(input("Ingrese horas dedicadas al estudio por dia:"))

# PROCESSING
total_de_horas_por_semana=horas_dedicadas_al_estudio_por_dia*7

# OUTPUT
print("###########################")
print("#  RENDIMIENTO ACADEMICO  #")
print("###########################")
print("# alumno: ",alumno,"  #")
print("# horas dedicadas al aestudio por dia: ",horas_dedicadas_al_estudio_por_dia,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# bajo rendimiento academico : ",bajo_rendimiento_academico,  "#")
print("###########################")


#Ejercicio_03
#Declaracion de variable de comprador compulsivo
cliente,producto1,producto2,cant_de_producto1,cant_de_producto2,cost_uni1,cost_uni2,total="","","",0,0,0.0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto1=input("Ingrese producto 1:")
producto2=input("Ingrese producto 2:")
cant_de_producto1=int(input("Ingrese cantidad de producto 1:"))
cant_de_producto2=int(input("Ingrese cantidad de producto 2:"))
costo_uni1=float(input("Ingrese costo unitario 1:"))
costo_uni2=float(input("Ingrese costo unitario 2:"))

# PROCESSING
total=cant_de_producto1*cost_uni1+cant_de_producto2*costo_uni2

# OUTPUT
print("###########################")
print("#   COSMETICOS   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto1,"        #")
print("# Producto 2: ",producto2,"        #")
print("# Cantidad de producto 1: ",cant_de_producto1,"           #")
print("# Cantidad de producto 2: ",cant_de_producto2," #")
print("# Costo Unitario 1: S/. ",costo_uni1," #")
print("# Costo Unitario 2: S/. ",costo_uni2," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador compulsivo: ",comprador_compulsivo,  "#")
print("###########################")


#Ejercicio_04
#Declaracion de variable de automedicacion
paciente,medicamento_1,medicamento_2,cant_de_medicamento1_por_dia,cant_de_medicamento2_por_dia,total_de_medicamentos_por_semana="","","",0,0,0

# INPUT
paciente=input("Ingrese paciente:")
medicamento_1=input("Ingrese medicamento 1: ")
medicamento_2=input("Ingrese medicamento 2: ")
cant_de_medicamento1_por_dia=int(input("Ingrese cantidad de medicamento 1 por dia:"))
cant_de_medicamento2_por_dia=int(input("Ingrese cantidad de medicamento 2 por dia:"))

# PROCESSING
total_de_medicamentos_por_semana=cant_de_medicamento1_por_dia*7+cant_de_medicamento2_por_dia*7

# OUTPUT
print("###########################")
print("#       MEDICAMENTOS       #")
print("###########################")
print("# Paciente: ",paciente,"  #")
print("# medicamento 1: ",medicamento_1,"        #")
print("# medicamento 2: ",medicamento_2,"        #")
print("# cantidad de medicamento 1 por dia : ",cant_de_medicamento1_por_dia,"        #")
print("# cantidad de medicamento 2 por dia : ",cant_de_medicamento2_por_dia,"        #")
print("###########################")
print("total de medicamento por semana:",total_de_medicamentos_por_semana,"      #")
print("# automedicacion : ",automedicacion,  "#")
print("###########################")


#Ejercicio_05
#Declaracion de variable de inclinacion al deporte
nombre,deporte1,deporte2,cant_de_hora_diarias_1,cant_de_hora_diarias_2,total_de_horas_por_semana="","","",0,0,0

# INPUT
nombre=input("Ingrese nombre:")
deporte1=input("Ingrese deporte 1: ")
deporte2=input("Ingrese deporte 2: ")
cant_de_hora_diarias_1=int(input("Ingrese cantidad de horas diarias 1:"))
cant_de_hora_diarias_2=int(input("Ingrese cantidad de horas diarias 2:"))

# PROCESSING
total_de_horas_por_dia=cant_de_hora_diarias_1+cant_de_hora_diarias_2

# OUTPUT
print("###########################")
print("#       DEPORTE        #")
print("###########################")
print("# Nombre: ",nombre,"  #")
print("# deporte 1: ",deporte1,"        #")
print("# deporte 2: ",deporte2,"        #")
print("# cantidad de horas diarias 1: ",cant_de_hora_diarias_1,"        #")
print("# cantidad de horas diarias 2: ",cant_de_hora_diarias_2,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# inclinacion al deporte :",inclinacion_al_deporte,  "#")
print("###########################")


#Ejercicio_06
#Declaracion de variable de comprador pasivo
cliente,producto_1,cantidad_producto_1,cost_uni_1,total="","",0,0.0,0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto_1=input("Ingrese producto 1:")
cant_de_producto_1=int(input("Ingrese cantidad de producto 1:"))
costo_uni_1=float(input("Ingrese costo unitario 1:"))

# PROCESSING
total=cant_de_producto_1*cost_uni_1

# OUTPUT
print("###########################")
print("#   ARTEFACTOS   #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto 1: ",producto_1,"        #")
print("# Cantidad de producto 1: ",cant_de_producto_1,"           #")
print("# Costo Unitario 1: S/. ",costo_uni_1," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# comprador pasivo: ",comprador_pasivo,  "#")
print("###########################")


#Ejercicio_07
#Declaracion de variable  nota aprobatoria
nombre_alumno,nota_1,nota_2,nota_3,promedio="",0,0,0,0

# INPUT
nombre_alumno=input("Ingrese el nombre del alumno:")
nota_1=int(input("Ingrese nota 1:"))
nota_2=int(input("Ingrese nota 2:"))
nota_3=int(input("Ingrese nota 3:"))

# PROCESSING
promedio=(nota_1+nota_2+nota_3)/3

# OUTPUT
print("###########################")
print("#     BOLETA DE NOTA      #")
print("###########################")
print("# nombre alumno : ",nombre_alumno,"  #")
print("# nota 1: ",nota_1,"        #")
print("# nota 2: ",nota_2,"        #")
print("# nota 3: ",nota_3,"        #")
print("###########################")
print("promedio:",promedio,"      #")
print("# nota aprobatoria: ",nota_aprobatoria,  "#")
print("###########################")


#Ejercicio_08
#Declaracion de variable de cumplimiento de horas de trabajo
trabajador,horas_de_jornada_laboral_por_dia,dias_de_jornada_laboral,total="",0,0,0

# INPUT
trabajador=input("Ingrese trabajador:")
horas_de_jornada_laboral_por_dia=int(input("Ingrese horas de jornada laboral por dia:"))
dias_de_jornada_laboral=int(input("Ingrese dias de jornada laboral:"))

# PROCESSING
total=horas_de_jornada_laboral_por_dia*dias_de_jornada_laboral

# OUTPUT
print("###########################")
print("#       HORAS DE TRABAJO        #")
print("###########################")
print("# trabajador: ",trabajador,"  #")
print("# horas de jornada laboral por dia: ",horas_de_jornada_laboral_por_dia,"        #")
print("# dias de jornada laboral: ",dias_de_jornada_laboral,"        #")
print("###########################")
print("total de horas por semana:",total_de_horas_por_semana,"      #")
print("# cumplimiento de horas de trabajo : ",cumplimiento_de_horas_de_trabajo,  "#")
print("###########################")


#Ejercicio_09
#Declaracion de variable de adiccion a la television
nombre,horas_dedicadas_a_la_television_por_dia,horas_dedicadas_a_la_television_por_semana,total="",0,0,0

# INPUT
nombre=input("Ingrese nombre:")
horas_dedicadas_a_la_television_por_dia=int(input("Ingrese horas dedicadas a la television por dia:"))
horas_dedicadas_a_la_television_por_semana=int(input("Ingrese horas dedicadas a la television por semana:"))

# PROCESSING
total=horas_dedicadas_a_la_television_por_dia*horas_dedicadas_a_la_television_por_semana

# OUTPUT
print("###########################")
print("#       HORAS DEDICADAS A LA TELEVISION     #")
print("###########################")
print("# nombre: ",nombre,"  #")
print("# horas dedicadas a la television por dia: ",horas_dedicadas_a_la_television_por_dia,"        #")
print("# dias dedicadas a la television por semana: ",horas_dedicadas_a_la_television_por_semana,"        #")
print("###########################")
print("total :",total,"      #")
print("# adiccion a la television : ",adiccion_a_la_television,  "#")
print("###########################")


#Ejercicio_10
#Declaracion de variable de adiccion al gimnasio
cliente,horas_dedicadas_al_gimnasio_por_dia,horas_dedicadas_al_gimnasio_por_semana,total="",0,0,0

# INPUT
cliente=input("Ingrese cliente:")
horas_dedicadas_al_gimnasio_por_dia=int(input("Ingrese horas dedicadas al gimnasio por dia:"))
horas_dedicadas_al_gimnasio_por_semana=int(input("Ingrese horas dedicadas al gimnasio por semana:"))

# PROCESSING
total=horas_dedicadas_al_gimnasio_por_dia*horas_dedicadas_al_gimnasio_por_semana

# OUTPUT
print("###########################")
print("#       HORAS DEDICADAS AL GIMNASIO     #")
print("###########################")
print("# cliente: ",cliente,"  #")
print("# horas dedicadas al gimnasio por dia: ",horas_dedicadas_al_gimnasio_por_dia,"        #")
print("# dias dedicadas al gimnasio por semana: ",horas_dedicadas_al_gimnasio_por_semana,"        #")
print("###########################")
print("total :",total,"      #")
print("# adiccion al gimasio : ",adiccion_al_gimnasio,"   #")
print("###########################")
