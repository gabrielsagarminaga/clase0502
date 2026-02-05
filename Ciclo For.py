gastos=[500,500,500,500,500]
total=0
for gasto in gastos:
    total = total + gasto #suma cada elemento
    print(f"Total: Q {total}") 

#Ejercicio 1 Modificado (Bonus)
gastos = [1200, 350, 450, 875, 600]
total = 0

for gasto in gastos:
    print(f"Gasto actual: Q {gasto}")
    total = total + gasto  # suma cada elemento
    print(f"Total: Q {total}")

# Ejercicio 2---Range---
for numero in range (5):#range(5) genera: 0,1,2,3,4
    print(numero)

for numero in range(1,6):
    print(numero)

for numero in range(0,10,2):
    print(numero)
#Ejercicio 2- Parte B
precio_por_pagina = 2.50
for paginas in range(1,6):
    total = paginas* precio_por_pagina
    print(f"{paginas} pagina(s) : Q{total:.2f}")

#Ejercicio 2- Parte C
tipo_cambio = 7.80
total=0
for usd in range(10,101,10):
    print(usd,usd * tipo_cambio, total)
    total+= (usd*tipo_cambio)
    #Agregar una linea que muestre el ahorro en quetzales comparando con la entrada anterior

#Ejercicio 3 Parte A
ventas=[15000,22000,18000,25000]
for posicion, venta in enumerate(ventas):
    print(f"{posicion+1} lugar: Q {venta}")

#Ejercicio 3- Parte B
productos = ["Laptop","Mouse","Teclado"]
for n,p in enumerate(productos, start=1):
    print(f"#{n}: {p}")

#Ejercicio 3-- Parte C ---
prod= ["Papel","Lapiceros","Cuadernos"]
stock= [45,120,85]

for n,p in enumerate(prod, start=1):
    cant = stock[n-1]
    if cant < 50:
        print(f"[{n}] {p}: {cant}  [!] Bajo Stock")
    else:
        print(f"[{n}] {p}: {cant} ///Alto Stock")    