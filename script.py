# soy santiago soto estudiate de ingenieria en sistemas del CEAD valledupar de la unad y este es el problema # 3
#Grupo: 213022A_2201
#codigo: Autoria Propia
print("Mi nombre es Santiago Soto y este es el problema # 3")
inventario=[["A001","Arroz", 10, 20],
            ["A002","Frijoles",5,10],
            ["A003","Azucar", 10, 30],
            ["A004","Sal", 8, 20],
            ["A005","Aceite", 15, 25]]
def cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0
print(f"{'Código':<6} {'Nombre':<10} {'Stock Actual':<13} {'Stock Mínimo':<10}")
print("-" * 50)
for articulo in inventario:
    print(f"{articulo[0]:<6} {articulo[1]:<10} {articulo[2]:<13} {articulo[3]:<10}")
#ahora generaremos la lista de pedidos para complertar el stock mínimo
print("\nLista de pedidos para completar el stock mínimo:")
for articulo in inventario:
    cantidad= cantidad_a_pedir(articulo[2], articulo[3])
    if cantidad > 0:
        print(f"{articulo[0]:<6} {articulo[1]:<10} {cantidad:<13}")