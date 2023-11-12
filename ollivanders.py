https://replit.com/join/qvqenrrbzu-fernandaportil3

registro_clientes = {}

def registrar_cliente():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    varitas_compradas = []

    while True:
        print("Opciones de varitas:")
        print("1. Varita de Saúco")
        print("2. Varita de Espino")
        print("3. Varita de Sauce")
        print("4. Varita de Acebo")
        print("0. Terminar de agregar varitas")

        opcion = input("Seleccione una opción (1-4) o 0 para terminar: ")

        if opcion == '0':
            break
        elif opcion in ('1', '2', '3', '4'):
            varitas_compradas.append(opcion)
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

    registro_clientes[nombre_cliente] = varitas_compradas
    print(f"Registro exitoso para {nombre_cliente}.")

def mostrar_registro():
    print("\nRegistro de clientes y sus compras de varitas:")
    for cliente, varitas_compradas in registro_clientes.items():
        print(f"{cliente}: {', '.join([varita_nombre(opcion) for opcion in varitas_compradas])}")

def varita_nombre(opcion):
    opciones_varitas = {
        '1': 'Varita de Saúco',
        '2': 'Varita de Espino',
        '3': 'Varita de Sauce',
        '4': 'Varita de Acebo'
    }
    return opciones_varitas[opcion]

while True:
    print("\nMenú principal:")
    print("1. Registrar cliente y sus compras de varitas")
    print("2. Mostrar registro de clientes")
    print("0. Salir")

    opcion_menu = input("Seleccione una opción (1-2) o 0 para salir: ")

    if opcion_menu == '1':
        registrar_cliente()
    elif opcion_menu == '2':
        mostrar_registro()
    elif opcion_menu == '0':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.")
