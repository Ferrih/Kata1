precio = 3.49
descuento = 0.4
precio_con_descuento = precio*descuento

numero_de_barras = input("Introduce el número de barras vendidas: ")
int(numero_de_barras)

print("Precio habitual " + str(precio))
print("Descuento: "+ str(descuento))
print("Coste final: "+ str(precio_con_descuento*numero_de_barras))