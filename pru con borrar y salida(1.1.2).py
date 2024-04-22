import os

campus = ["zona core", "campus uno", "campus matriz", "sector outsourcing"]

def menu_ver_disp():
    while True:
        os.system("cls")
        print("Seleccione el campus")
        for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
        print(f"{len(campus) + 1}. Volver al Menú Principal")
        
        selector = int(input("\nSelecciona una opción: "))
        
        if selector == len(campus) + 1:
            print("Volviendo al Menú Principal...")
            break
        elif 1 <= selector <= len(campus):
            archivo = campus[selector - 1] + ".txt"
            
            try:
                with open(archivo, "r") as arch:
                    for line in arch:
                        print(line.strip())
                input("\nPulsa Enter para continuar...")
            except IOError as e:
                print("Error al abrir el archivo:", e)
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_add_disp():
    os.system("cls")
    print("¿Dónde agregar nuevo dispositivo?\n")
    for idx, item in enumerate(campus, 1):
        print(f"{idx}. {item}")
    print()
    selector = int(input("Elija una opción: "))
    if 1 <= selector <= len(campus):
        os.system("cls")
        file_path = campus[selector - 1] + ".txt"
        with open(file_path, "a") as file:
            print("Ingrese los siguientes datos para el nuevo dispositivo:")
            print("NOTA: Si el dispositivo tiene más de una IP, agregar de la siguiente forma (INTERFAZ: IP/MASK). \nEjemplo fe0/1:192.168.10.1/24")
            ip_address = input("a. Dirección IP: ")
            device_name = input("b. Nombre de dispositivo: ")
            vlans = input("c. VLAN(s) configuradas: ")
            network_services = input("d. Servicios de red comprometidos: ")
            hierarchy_options = {
                1: "Núcleo",
                2: "Acceso",
                3: "Distribución"
            }
            print("e. Capa a la que pertenece, modelo jerárquico:")
            for key, value in hierarchy_options.items():
                print(f"{key}. {value}")
            jerarquia = int(input("Elija su opción: "))
            
            file.write(f"\n---------------------------------\n")
            file.write(f"Dispositivo: {device_name}\n")
            file.write(f"Direccionamiento IP: {ip_address}\n")
            file.write(f"VLAN(s) configuradas: {vlans}\n")
            file.write(f"Servicios de red: {network_services}\n")
            if jerarquia in hierarchy_options:
                file.write(f"Capa a la que pertenece, (modelo jerárquico): {hierarchy_options[jerarquia]}\n")
            else:
                file.write("Jerarquía: No especificada\n")
            file.write("---------------------------------\n")
            
            print("Dispositivo agregado correctamente.")
            input("Presiona Enter para continuar...")
    else:
        print("Opción no válida. Inténtalo de nuevo.")

def menu_del_disp():
    os.system("cls")
    print("Seleccione el campus para borrar dispositivo")
    for idx, item in enumerate(campus, 1):
        print(f"{idx}. {item}")
    print(f"{len(campus) + 1}. Volver al Menú Principal")

    selector = int(input("\nSelecciona una opción: "))

    if selector == len(campus) + 1:
        print("Volviendo al Menú Principal...")
        return
    elif 1 <= selector <= len(campus):
        archivo = campus[selector - 1] + ".txt"

        try:
            with open(archivo, "r") as arch:
                lineas = arch.readlines()

            # Mostrar dispositivos para borrar
            print("\nDispositivos del campus:")
            for i, linea in enumerate(lineas, 1):
                    print(f"{i}. {linea.strip()}")
            while True:
                #pedir cantidad de lineas a borrar
                while True:
                    cant_borrar = (input("\nIngrese la cantidad de líneas a borrar (o 'q' para salir): "))
                    if cant_borrar.lower() == "q":
                            print("Saliendo del proceso de borrado...")
                            return
                    elif cant_borrar.isdigit() and int(cant_borrar) > 0 and int(cant_borrar) <= len(lineas):
                        cant_borrar = int(cant_borrar)
                        break
                    else:
                        print("Cantidad inválida. Debe ser un número entre 1 y", len(lineas))
                lineas_borrar = []
                for _ in range(cant_borrar):
                    while True:
                        linea_num = int(input(f"Seleccione el número de línea {_ + 1}: "))
                        #convertir caracter en minuscula si es mayuscula
                        if linea_num and int(linea_num) > 0 and int(linea_num) <= len(lineas):
                            lineas_borrar.append(int(linea_num) - 1)
                            break
                        else:
                            print("Número de línea inválido. Intente de nuevo.")
                
                # Mostrar las líneas seleccionadas para borrar
                print("\nLíneas seleccionadas para borrar:")
                for num_linea in lineas_borrar:
                    print(f"{num_linea + 1}. {lineas[num_linea].strip()}")

                # Confirmar si el usuario desea borrar estas líneas
                confirmacion = input("\n¿Desea borrar estas línea? (s/n): ")
                if confirmacion.lower() == "s":
                    #Borrar las líneas seleccionadas
                    for num_linea in sorted(lineas_borrar, reverse=True):
                        del lineas[num_linea]

                    # Borrar dispositivo seleccionado
                    with open(archivo, "w") as arch:
                        for linea in lineas:
                            arch.write(linea)
            
                    print("Dispositivo borrado correctamente.")
                    break
                elif confirmacion.lower() == "n":
                    print("Operación cancelada. Vuelve a intentarlo.")
                else:
                    print("Operación cancelada. No se han borrado líneas.")

            input("Presiona Enter para continuar...")
        except (IOError, IndexError) as e:
            print("Error al abrir o manipular el archivo:", e)
    else:
        print("Opción no válida. Inténtalo de nuevo.")

while True:
    os.system("cls")
    print("BIENVENIDO ADMINISTRADOR DE RED.\n¿Qué desea hacer?")
    print("1. Ver los dispositivos.")
    print("2. Ver los campus.")
    print("3. Añadir dispositivo.")
    print("4. Añadir campus.")
    print("5. Borrar dispositivo.")
    print("6. Borrar campus.")
    print("7. Salir")

    selector = int(input("Elija una opción: "))

    if selector == 1:
        menu_ver_disp()
    elif selector == 2:
        os.system("cls")
        print("Lista de campus:")
        for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
        input("\nPulsa Enter para continuar...")
    elif selector == 3:
        menu_add_disp()
    elif selector == 4:
        os.system("cls")
        print("Función para añadir campus.")
        input("\nPulsa Enter para continuar...")
    elif selector == 5:
        menu_del_disp()  # Llamando a la función para borrar dispositivo
    elif selector == 6:
        os.system("cls")
        print("Función para borrar campus.")
        input("\nPulsa Enter para continuar...")
    elif selector == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")