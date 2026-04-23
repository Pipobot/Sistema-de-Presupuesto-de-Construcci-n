import os
os.system ("cls")

#Actividad

IVA = 0.19 
PRESUPUESTO_MAXIMO = 50000000 

print("==Sistema de Presupuesto de Construcción==")
nombre_proyecto = input("Ingrese el nombre del proyecto: ")

while True:
    try:
        metros = float(input("Ingrese la cantidad de metros cuadrados a construir: "))
        costo_metros = float(input("Ingrese el costo por metro cuadrado: "))
        costo_trabajadores = float(input("Ingrese el pago por trabajador: "))
        trabajadores = int(input("Ingrese la cantidad de trabajadores: "))
        if metros > 0 and costo_metros > 0 and costo_trabajadores > 0 and trabajadores > 0:
            break
        else:
            print("Error! Todos los valores deben ser mayor a 0.")
    except:
        print("Error! Los datos no son validos :(")
        
costo_materiales = metros * costo_metros
costo_mano_de_obra = trabajadores * costo_trabajadores
costo_neto = costo_materiales + costo_mano_de_obra
iva_aplicado = costo_neto * IVA
costo_total = costo_neto + iva_aplicado
costo_redondeado = round(costo_total, 2)

limite = PRESUPUESTO_MAXIMO * 0.10

if costo_total <= PRESUPUESTO_MAXIMO:
    estado = "Dentro del presupuesto."
elif costo_total <= limite:
    estado = "Presuepuesto ajustado."
else:
    estado = "Fuera del presupuesto."
    
print("==RESUMEN DEL PROYECTO==")
print(f"Nombre del proyecto: {nombre_proyecto}")
print(f"Costo total: ${costo_redondeado}")
print(f"Estado del proyecto: {estado}")