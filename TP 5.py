# Ejercicio 1: Leer números que representan edades de un grupo de personas, finalizando la
# lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18
# años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos.
# Descartar valores que no representan una edad válida. (Se considera válida una
# edad entre 0 y 100).

# cantMenoresDeEdad = 0
# cantMayoresDeEdad = 0
# sumaMenores = 0
# sumaMayores = 0
# edadesIngresadasTotales = 0
# 
# edad = int(input("Ingrese una edad (o -1 para terminar): "))
# 
# while edad != -1:
#     if edad < 1 or edad > 100:
#         print("Ingrese una edad válida entre 1 y 100")
#     else:
#         if edad < 18:
#             cantMenoresDeEdad += 1
#             sumaMenores += edad
#             edadesIngresadasTotales += 1
#         else:
#             cantMayoresDeEdad += 1
#             sumaMayores += edad
#             edadesIngresadasTotales += 1
# 
#     edad = int(input("Ingrese una edad: "))
# 
# if edadesIngresadasTotales > 0:
#     promedioEdadAmbosGrupos = (sumaMenores + sumaMayores) / edadesIngresadasTotales
#     print("Cantidad de personas menores de 18 años:", cantMenoresDeEdad)
#     print("Cantidad de personas mayores de 18 años:", cantMayoresDeEdad)
#     print("Promedio de edad de ambos grupos:", promedioEdadAmbosGrupos)
# else:
#     print("No se ingresaron edades válidas")

# Ejercicio 2: Escribir un programa que permita ingresar los números de legajo de los alumnos
# de un curso y su nota de examen final. El fin de la carga se determina ingresan-
# do un -1 en el legajo. Informar para cada alumno si aprobó o no el examen con-
# siderando que se aprueba con nota mayor o igual a 4. Se debe validar que la
# nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
# - Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
# - Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
# - Porcentaje de alumnos que están aplazados (tienen 1 en el examen).

# legajo = int(input("Ingrese su legajo: "))
# cantidadAplazados = 0
# cantidadAprobados = 0
# cantidadDesaprobados = 0
# 
# while legajo != -1:
#     notaExamenFinal = int(input("Ingrese la nota de su examen final: "))
#     
#     if notaExamenFinal < 1 or notaExamenFinal > 10:
#         print("Ingrese un número de nota válido entre 1 y 10")
#         notaExamenFinal = int(input("Ingrese la nota de su examen final: "))
#     
#     if notaExamenFinal == 1:
#         cantidadAplazados += 1
#         print("Desaprobó el examen")
#     elif notaExamenFinal >= 2 and notaExamenFinal < 4:
#         cantidadDesaprobados += 1
#         print("Desaprobó el examen")
#     elif notaExamenFinal >= 4 and notaExamenFinal <= 10:
#         cantidadAprobados += 1
#         print("Aprobó el examen")
#     
#     legajo = int(input("Ingrese su legajo: "))
# 
# totalAlumnos = cantidadAplazados + cantidadAprobados + cantidadDesaprobados
# if totalAlumnos > 0:
#     porcentajeAplazados = (cantidadAplazados / totalAlumnos) * 100
# else:
#     porcentajeAplazados = 0
# 
# print("Cantidad de alumnos que aprobaron:", cantidadAprobados)
# print("")
# print("Cantidad de alumnos que desaprobaron:", cantidadDesaprobados)
# print("")
# print("Porcentaje de alumnos aplazados (nota igual a 1):", porcentajeAplazados)

# Ejercicio 3:

# cantidadSolicitada = int(input("Ingrese la cantidad que solicita de un producto: "))
# 
# precioBase = 0
# cantidadVentasTotales = 0
# cantidadVentasPrecioBase = 0
# cantidadVentasDesc10 = 0
# cantidadVentasDesc25 = 0
# valorTotalVenta = 0
# unidadesTotales = 0
# 
# while cantidadSolicitada != -1:
#     precioBase = int(input("Ingrese el precio base del producto seleccionado: "))
#     
#     if cantidadSolicitada < 0:
#         print("Ingrese una cantidad válida mayor a 0")
#         cantidadSolicitada = int(input("Ingrese la cantidad que solicita de un producto: "))
#         precioBase = int(input("Ingrese el precio base del producto seleccionado: "))
#         
#     if cantidadSolicitada >= 1 and cantidadSolicitada <= 12:
#         cantidadVentasTotales += 1
#         cantidadVentasPrecioBase += 1
#         valorTotalVenta += (precioBase * cantidadSolicitada)
#         unidadesTotales += cantidadSolicitada
#     
#     elif cantidadSolicitada >= 13 and cantidadSolicitada <= 100:
#         cantidadVentasTotales += 1
#         cantidadVentasDesc10 += 1
#         valorTotalVenta += (precioBase - ((precioBase * 10) // 100)) * cantidadSolicitada
#         unidadesTotales += cantidadSolicitada
#     
#     elif cantidadSolicitada > 100:
#         cantidadVentasTotales += 1
#         cantidadVentasDesc25 += 1
#         valorTotalVenta += (precioBase - ((precioBase * 25) // 100)) * cantidadSolicitada
#         unidadesTotales += cantidadSolicitada
#     
#     cantidadSolicitada = int(input("Ingrese la cantidad que solicita de un producto: "))
# 
# precioPromedioPorUnidad = valorTotalVenta / unidadesTotales
# print("")
# print("Cantidad de ventas realizadas total:", cantidadVentasTotales)
# print("")
# print("Cantidad de ventas en las que se aplicó un 10% de descuento:", cantidadVentasDesc10)
# print("")
# print("Precio promedio por unidad:", precioPromedioPorUnidad)
# print("")
# print("Cantidad de ventas en las que SOLO se aplicó el precio base (no se realizaron descuentos):", cantidadVentasPrecioBase)
# print("")
# print("Valor total de la venta:", valorTotalVenta)

# Ejercicio 4: Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga
# su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento
# de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente.
# Si paga en los siguientes 10 días del mes deberá pagar el importe original de la
# factura, mientras que si paga después del día 20 deberá abonar una multa de
# $350 o del 10% de su factura, lo que resulte mayor. Escribir un programa que
# lea el número del cliente y el total de la factura, y emita un informe donde conste el número del cliente y los tres importes que podría abonar según la fecha de
# pago.

# numeroDeCliente = int(input("Ingrese su numero de cliente: "))
# totalDeLaFactura = float(input("Ingrese el total de la factura: "))
# 
# while totalDeLaFactura <= 0:
#     print("Por favor, ingrese un precio de factura valido.")
#     totalDeLaFactura = float(input("Ingrese el total de la factura: "))
# 
# dosPorciento = (totalDeLaFactura * 2) / 100
# precioDosPorciento = totalDeLaFactura - dosPorciento
# diezPorciento = (totalDeLaFactura * 10) / 100
# precioDiezPorciento = totalDeLaFactura + diezPorciento
# precioDescuento200 = totalDeLaFactura - 200
# multa350 = totalDeLaFactura + 350
# 
# print("")
# print("Numero de cliente:", numeroDeCliente)
# 
# if precioDosPorciento > precioDescuento200:
#     print("")
#     print("Si paga del 1 al 10:", precioDescuento200)
# else:
#     print("")
#     print("Si paga del 1 al 10:", precioDosPorciento)
# 
# 
# print("")
# print("Si paga del 11 al 20:", totalDeLaFactura)
# 
# if multa350 > precioDiezPorciento:
#     print("")
#     print("Si paga del 21 en adelante:", multa350)
# else:
#     print("")
#     print("Si paga del 21 en adelante:", precioDiezPorciento)

# Ejercicio 5: Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y
# un número entero N que representa una cantidad de días. Realizar un programa
# que imprima la nueva fecha que resulta de sumar N días a la fecha dada. Tener
# en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica 3.

D = int(input("Ingrese un numero de dia: "))
M = int(input("Ingrese un numero de mes: "))
A = int(input("Ingrese un año: "))
N = int(input("Ingrese la cantidad de dias que le quiere agregar a la fecha ingresada: "))

resultadoD = D + N
resultadoM = M
resultadoA = A
maximoDiasMesActual = 0

# asignar el maximo de dias del mes actual

if (resultadoM == 1) or (resultadoM == 3) or (resultadoM == 5) or (resultadoM == 7) or (resultadoM == 8) or (resultadoM == 10) or (resultadoM == 12):
    maximoDiasMesActual = 31
elif resultadoM == 2:
    if (A % 400 == 0) or (A % 100 != 0 and A % 4 == 0):
        maximoDiasMesActual = 29
    else:
        maximoDiasMesActual = 28
else:
    maximoDiasMesActual = 30
        
# mientras resultadoD sea mayor al maximo de dias del mes actual, se va a ejecutar el loop mientras se verdadera dicha condicion      
while (resultadoD > maximoDiasMesActual):
    # restarle a la nueva cantidad de dias el tope de dias del mes, y agregar 1 mes al resultado final.
    resultadoD -= maximoDiasMesActual
    resultadoM += 1
    
    # ver si el mes que tengo es mayor a 12, para saber si resetea los meses y no pasarse. Y por ultimo suma 1 anio.
    if resultadoM > 12:
        resultadoM -= 12
        resultadoA += 1
    
    # asignar el maximo de dias del mes actual
    if (resultadoM == 1) or (resultadoM == 3) or (resultadoM == 5) or (resultadoM == 7) or (resultadoM == 8) or (resultadoM == 10) or (resultadoM == 12):
        maximoDiasMesActual = 31
    elif resultadoM == 2:
        if (A % 400 == 0) or (A % 100 != 0 and A % 4 == 0):
            maximoDiasMesActual = 29
        else:
            maximoDiasMesActual = 28
    else:
        maximoDiasMesActual = 30
    
print("Nueva fecha:", resultadoD, "/", resultadoM, "/", resultadoA)

# Ejercicio 6: Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene. Tener en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa
# 12345 se debe imprimir 5.

# numeroOriginal = int(input("Ingrese un numero entero: "))
# contadorCifras = 0
# cifraSuelta = 0
# 
# while numeroOriginal == 0:
#     if numeroOriginal == 0:
#         print("Por favor, ingrese otro numero que no sea 0")
#         numeroOriginal = int(input("Ingrese un numero entero: "))
# 
# if numeroOriginal < 0:
#     numeroOriginal = -numeroOriginal
# 
# while numeroOriginal != 0:
#     cifraSuelta += numeroOriginal % 10
#     contadorCifras += 1
#     numeroOriginal = numeroOriginal // 10
#     cifraSuelta -= cifraSuelta
# 
# print(contadorCifras)

# Ejercicio 7: Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el
# número invertido. Tener en cuenta que el número puede ser negativo. Por ejemplo, si se ingresa 1234 debe mostrar 4321.

# numeroOriginal = int(input("Ingrese un numero entero: "))
# numeroAlReves = 0
# cifraSuelta = 0
# 
# while numeroOriginal == 0:
#     if numeroOriginal == 0:
#         print("Por favor, ingrese otro numero que no sea 0")
#         numeroOriginal = int(input("Ingrese un numero entero: "))
# 
# if numeroOriginal < 0:
#     numeroOriginal = -numeroOriginal
# 
# while numeroOriginal != 0:
#     cifraSuelta += numeroOriginal % 10
#     numeroAlReves *= 10
#     numeroAlReves += cifraSuelta
#     numeroOriginal -= cifraSuelta
#     numeroOriginal = numeroOriginal // 10
#     cifraSuelta -= cifraSuelta
#     
# print(numeroAlReves)

# Ejercicio 8:

legajoEmpleado = int(input("Ingrese su legajo: "))

salarioEmpleadoMasGana = 0
totalSalariosPagados = 0
cantEmpleadosMasDe200 = 0
cantEmpleadosMenosDe50 = 0
legajoEmpleadoMasGana = 0
sueldoMasBajo = 0
totalSueldosCat1 = 0
totalSueldosCat2 = 0
totalSueldosCat3 = 0
totalSueldos = 0

while legajoEmpleado != -1:
    categoriaEmpleado = int(input("Ingrese su categoria correspondiente: "))
    salarioEmpleado = int(input("Ingrese su salario: "))
    
    if legajoEmpleado <= 0 or categoriaEmpleado <= 0 or salarioEmpleado <= 0:
        print("Por favor ingresar valores positivos")
        legajoEmpleado = int(input("Ingrese su legajo: "))
        categoriaEmpleado = int(input("Ingrese su categoria correspondiente: "))
        salarioEmpleado = int(input("Ingrese su salario: "))
    
    if salarioEmpleado >= 200000:
        cantEmpleadosMasDe200 += 1
#         totalSalariosPagados += salarioEmpleado
#         totalSueldos += 1
    
    if salarioEmpleado <= 50000 and categoriaEmpleado == 3:
        cantEmpleadosMenosDe50 += 1
        totalSalariosPagados += salarioEmpleado
        totalSueldosCat3 += salarioEmpleado
        totalSueldos += 1
    
    if salarioEmpleado > salarioEmpleadoMasGana:
        salarioEmpleadoMasGana = salarioEmpleado
        legajoEmpleadoMasGana = legajoEmpleado
    
    if sueldoMasBajo == 0:
        sueldoMasBajo = salarioEmpleado
    elif salarioEmpleado < sueldoMasBajo:
        sueldoMasBajo = salarioEmpleado
    
    if categoriaEmpleado == 1:
        totalSueldosCat1 += salarioEmpleado
        totalSueldos += 1
    elif categoriaEmpleado == 2:
        totalSueldosCat2 += salarioEmpleado
        totalSueldos += 1
    else:
#         totalSueldosCat3 += salarioEmpleado
        totalSalariosPagados += salarioEmpleado
    
    legajoEmpleado = int(input("Ingrese su legajo: "))
        
totalSalariosPagados = (totalSueldosCat1 + totalSueldosCat2 + totalSueldosCat3)
salarioPromedio = totalSalariosPagados / totalSueldos

print("")
print("Importe total de salarios pagados por la empresa:", totalSalariosPagados)
print("Cantidad de empleados que ganan mas de $200.000:", cantEmpleadosMasDe200)
print("Cantidad de empleados que ganan menos de $50.000 y son de categoria 3:", cantEmpleadosMenosDe50)
print("Legajo del empleado que mas gana:", legajoEmpleadoMasGana)
print("Sueldo mas bajo:", sueldoMasBajo)
print("Importe total de sueldos por categoria:")
print("Categoria 1:", totalSueldosCat1)
print("Categoria 2:", totalSueldosCat2)
print("Categoria 3:", totalSueldosCat3)
print("Salario promedio:", salarioPromedio)

# Ejercicio 9:

# numero = int(input("Ingrese un numero: "))
# inicio = 1
# suma = 0
# 
# while numero <= 0:
#     print("Por favor, ingresar un numero positivo o que no sea 0")
#     numero = int(input("Ingrese un numero: "))
# 
# while inicio <= numero:
#     if inicio % 2 != 0:
#         print(inicio)
#         suma += inicio
#         inicio += 1
#     else:
#         inicio += 1
# print(suma)