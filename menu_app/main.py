def agregar_compra(Lista_compras):
    monto_compra = float(input("Ingrese el monto de la compra:$"))
    Lista_compras.append(monto_compra)
    print("Compra agregada correctamente")

def mostrar_compras(Lista_compras):
    print("Compras:")
    for indice, compras in enumerate(Lista_compras, start=1):
        print(f"{indice}. ${compras}")

def total(Lista_compras):
    suma_compras = sum(Lista_compras)
    print("Total gastado: $", suma_compras)


def main():
    Lista_compras = []
    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_compra(Lista_compras)
        elif opcion == "2":
            mostrar_compras(Lista_compras)
        elif opcion == "3":
            total(Lista_compras)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()



