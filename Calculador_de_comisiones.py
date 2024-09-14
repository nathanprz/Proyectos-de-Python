#Pide nombre del usuario y lo almacena en una variable
nombre = input("¿Cúal es tu nombre?: ")

#Pide cuanto gana por venta y lo guarda en una variable
comision = float(input("¿Cuanto ganas en comisiones?, Por ejemplo: 13% (solo el numero sin signos extra)\nPorcentaje: "))

#Pide las ventas y lo almacena en una variable
ventas = float(input("¿Cúanto vendiste?: "))
ventas = round(ventas,2)

#Operacion y redondeo
ganancias = round(ventas * comision / 100,2)
#Muestra las ganancias del usuario y su nombre
print(f"Hola {nombre}\nComo has vendido {ventas} y tus comiciones son del {comision}\n\tTUS GANANCIAS SON:{ganancias} pesos")
