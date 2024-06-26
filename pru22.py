import os

def guardar_campus():
    with open("campus.txt", "w") as f:
        for c in campus:
            f.write(c + "\n")
def cargar_campus():
    if os.path.exists("campus.txt"):
        with open("campus.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    else:
        return []

campus = cargar_campus()

def menu_ver_disp():
    while True:
        os.system("clear")
        print("Seleccione el campus")
        for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
        print(f"{len(campus) + 1}. Volver al Menú Principal")
        
        try:
            selector = int(input("\nSelecciona una opción: "))
            
            if selector == len(campus) + 1:
                print("Volviendo al Menú Principal.")
                break
            elif 1 <= selector <= len(campus):
                archivo = campus[selector - 1] + ".txt"
                try:
                    os.system("clear")
                    with open(archivo, "r") as arch:
                        for line in arch:
                            print(line.strip())
                    input("\nPulsa Enter para continuar.")
                except IOError as e:
                    print("Error al abrir el archivo:", e)
            else:
                print("Esta opcion no se encuentra. Inténtalo de nuevo.")
                input("Presiona Enter para continuar")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
            input("Presiona Enter para continuar.")

def menu_add_disp():
    while True:
        os.system("clear")
        print("¿Dónde agregar nuevo dispositivo?\n")
        for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
        print(f"{len(campus) + 1}. Volver al Menú Principal")
        print()
        try:
            selector = int(input("Elija una opción: "))
            
            if selector == len(campus) + 1:
                print("Volviendo al Menú Principal.")
                break
            elif 1 <= selector <= len(campus):
                os.system("clear")
                file_path = campus[selector - 1] + ".txt"
                
                with open(file_path, "a") as file:
                    print("Ingrese los siguientes datos para el nuevo dispositivo:")
                    print("NOTA: Si el dispositivo tiene más de una IP, agregar de la siguiente forma (INTERFAZ: IP/MASK). \nEjemplo fe0/1:192.168.10.1/24")
                    tipo_dispositivo = input("a. Tipo de dispositivo:")
                    device_name = input("b. Nombre de dispositivo: ")
                    ip_address = input("c. Dirección IP: ")
                    vlans = input("c. VLAN(s) configuradas: ")
                    network_services = input("d. Servicios de red comprometidos: ")
                    
                    jerarquia_opciones = {
                        1: "Núcleo",
                        2: "Acceso",
                        3: "Distribución"
                    }
                    print("e. Capa a la que pertenece, modelo jerárquico:")
                    for key, value in jerarquia_opciones.items():
                        print(f"{key}. {value}")
                    jerarquia = int(input("Elija su opción: "))
                    
                    file.write(f"\n---------------------------------\n")
                    file.write(f"Tipo de dispositivo: {tipo_dispositivo}\n")
                    file.write(f"Nombre de dispositivo: {device_name}\n")
                    file.write(f"Direccionamiento IP: {ip_address}\n")
                    file.write(f"VLAN(s) configuradas: {vlans}\n")
                    file.write(f"Servicios de red: {network_services}\n")
                    if jerarquia in jerarquia_opciones:
                        file.write(f"Capa a la que pertenece, (modelo jerárquico): {jerarquia_opciones[jerarquia]}\n")
                    else:
                        file.write("Jerarquía: No especificada\n")
                    file.write("---------------------------------\n")
                    
                    print("Dispositivo agregado correctamente.")
                    input("Presiona Enter para continuar.")
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                input("Presiona Enter para continuar")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
            input("Presiona Enter para continuar.")
def menu_del_disp():
    while True:
        os.system("clear")
        print("Seleccione el campus para borrar dispositivo")
        for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
        print(f"{len(campus) + 1}. Volver al Menú Principal")

        try:
            selector = int(input("\nSelecciona una opción: "))
            
            if selector == len(campus) + 1:
                print("Volviendo al Menú Principal...")
                break
            elif 1 <= selector <= len(campus):
                archivo = campus[selector - 1] + ".txt"
                os.system("clear")
                with open(archivo, "r") as arch:
                    lineas = arch.readlines()

                # Mostrar dispositivos para borrar
                print("\nDispositivos del campus:")
                # Mostrar la primera línea sin número
                print(lineas[0].strip())
                for i, linea in enumerate(lineas[1:], 1):
                        print(f"{i}. {linea.strip()}")
                while True:
                    # pedir cantidad de lineas a borrar
                    while True:
                        try:
                            cant_borrar = input("\nIngrese la cantidad de líneas a borrar (o 'q' para salir): ")
                            if cant_borrar.lower() == "q":
                                print("Saliendo del proceso de borrado...")
                                return
                            elif cant_borrar.isdigit() and int(cant_borrar) > 0 and int(cant_borrar) <= len(lineas):
                                cant_borrar = int(cant_borrar)
                                break
                            else:
                                print("Cantidad inválida. Debe ser un número entre 1 y", len(lineas))
                        except ValueError:
                            print("Entrada no válida. Intentelo de nuevo")
                            input("Presiona Enter para continuar.")
                    lineas_borrar = []
                    for _ in range(cant_borrar):
                        while True:
                            linea_num = input(f"Seleccione el número de línea {_ + 1}: ")
                            # devolver un valor booleano True o False si coincide que la cadena contenga caracteres dígitos.
                            if linea_num.isdigit() and int(linea_num) > 0 and int(linea_num) <= len(lineas):
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
                        # Borrar las líneas seleccionadas
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
            else:
                print("Opción no válida. Debe ingresar una opcion del menu.")
                input("Presiona Enter para continuar.")
        except ValueError:
                print("Entrada no válida. Intentelo de nuevo")
                input("Presiona Enter para continuar.")

def menu_add_campus():
    os.system("clear")
    print("Campus existentes:")
    for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
    new_campus = input("Ingrese el nombre del nuevo campus (o 'q' para salir):")
    if new_campus.lower() == "q":
        print("Saliendo...")
        return
    if new_campus in campus:
        print("El campus ya existe.")
        input("Presiona Enter para continuar.")
        return
    campus.append(new_campus)
    guardar_campus() # Guardar la lista actualizada
    with open(f"{new_campus}.txt", "w") as new_file:
        new_file.write(f"DISPOSITIVOS DE {new_campus}")
        print(f"{new_campus}: Creado correctamente.")
        input("Presiona Enter para continuar.")
def menu_del_campus():
    while True:
        os.system("clear")
        print("Seleccione el campus para borrar")
        for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
        print(f"{len(campus) + 1}. Volver al Menú Principal")
        try:
            selector = int(input("\nSelecciona una opción: "))

            if selector == len(campus) + 1:
                print("Volviendo al Menú Principal...")
                return
            elif 1 <= selector <= len(campus):
                campus_borrar = campus[selector - 1]
                archivo_borrar = campus_borrar + ".txt"
                
                confirmar = input(f"¿Está seguro que desea borrar el campus '{campus_borrar}' y su archivo '{archivo_borrar}'? (s/n): ")
                if confirmar.lower() == "s":
                    
                    os.remove(archivo_borrar)
                    campus.remove(campus_borrar)
                    guardar_campus()
                    print(f"Campus '{campus_borrar}' y su archivo '{archivo_borrar}' eliminados correctamente.")
                    input("Presiona Enter para continuar...")
                    
                elif confirmar.lower() == "n":
                    print("Operación cancelada.")
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
                    input("Presione Enter para continuar")
            else:
                print("Opcion no valida. Vuelva a intentar.")
                input("Presione Enter para continuar")
        except ValueError:
                print("Entrada no válida. Debe ingresar un número.")
                input("Presiona Enter para continuar.")
def menu_prin():
    while True:
        os.system("clear")
        print("BIENVENIDO ADMINISTRADOR DE RED.\n¿Qué desea hacer?")
        print("1. Ver los dispositivos.")
        print("2. Ver los campus.")
        print("3. Añadir dispositivo.")
        print("4. Añadir campus.")
        print("5. Borrar dispositivo.")
        print("6. Borrar campus.")
        print("7. Salir")
        try:
            selector = int(input("Elija una opción: "))

            if selector == 1:
                menu_ver_disp()
            elif selector == 2:
                os.system("clear")
                print("Lista de campus:")
                for idx, item in enumerate(campus, 1):
                    print(f"{idx}. {item}")
                input("\nPulsa Enter para continuar...")
            elif selector == 3:
                menu_add_disp()
            elif selector == 4:
                menu_add_campus()
            elif selector == 5:
                menu_del_disp()  # Llamando a la función para borrar dispositivo
            elif selector == 6:
                menu_del_campus()
            elif selector == 7:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                input("Presiona Enter para continuar.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
            input("Presiona Enter para continuar.")
if __name__ == "__main__":
    menu_prin()