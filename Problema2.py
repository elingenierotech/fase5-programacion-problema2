# Problema 2: Gestión de precios de restaurante con promociones

def calcular_precio_final(precio_base, categoria, categoria_objetivo, umbral):
    """
    Calcula el precio final aplicando 15% de descuento si:
    - La categoría es igual a la categoría objetivo
    - El precio base es mayor al umbral definido
    """
    if categoria == categoria_objetivo and precio_base > umbral:
        precio_final = precio_base * 0.85  # Aplica 15% de descuento
        return precio_final
    else:
        return precio_base

# matriz con Nombre, Categoría, Precio Base
menu = [
    ["Bandeja Paisa", "Plato Fuerte", 35000],
    ["Hamburguesa", "Comida Rápida", 18000],
    ["Ensalada César", "Entrada", 12000],
    ["Pizza Pepperoni", "Plato Fuerte", 28000],
    ["Pasta Alfredo", "Plato Fuerte", 22000],
    ["Gaseosa", "Bebida", 5000]
]

# Parámetros de la promoción
categoria_objetivo = "Plato Fuerte"
umbral_precio = 20000

# Generar informe
print("Informe de precios con promoción\n")
print("Producto\t\tCategoría\t\tPrecio Base\tPrecio Final")
print("-" * 70)

for producto in menu:
    nombre, categoria, precio_base = producto
    precio_final = calcular_precio_final(precio_base, categoria, categoria_objetivo, umbral_precio)
    
    # Ajuste de formato para impresión
    print(f"{nombre:<20}\t{categoria:<15}\t${precio_base:>8,.0f}\t${precio_final:>8,.0f}")