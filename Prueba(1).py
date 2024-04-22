import os
campus = ["zona Core", "campus uno", "campus matriz", "sector outsourcing"]
def menu_ver_disp():
    while True:
        os.system("cls")
        print("Seleccione el campus")
        cont = 1
        exit_option = len(campus) + 1
        for item in campus:
            print(str(cont) + ".", item)
            cont += 1
        print(str(exit_option) + ". Volver al Menú Principal")
        
        selector = int(input("\nSelecciona una opción: "))
        
        if selector == exit_option:
            print("Volviendo al Menú Principal...")
            break
        elif selector >= 1 and selector <= len(campus):
            # Construir la ruta al archivo de texto
            archivo = campus[selector - 1] + ".txt"
            
            # Intentar abrir el archivo
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
    print("¿Donde agregar nuevo dispositivo?\n")
    for i, item in enumerate(campus, 1):
        print(f"{i}. {item}")
    print()
    selector = int(input("Elija una opción: "))
    
    if selector >= 1 and selector <= len(campus):
        os.system("cls")
        file_path = campus[selector - 1] + ".txt"
        
        with open(file_path, "a") as file:
            print("Elija un dispositivo:")
            print("1. Router")
            print("2. Switch")
            print("3. Switch multicapa")
            dispositivo = int(input("Elija su opción: "))
            
            print("Agregue el nombre de su dispositivo:")
            nombre = input("Agregue su nombre: ")
            
            print(f"Jerarquía para {nombre}:")
            print("1. Núcleo")
            print("2. Acceso")
            print("3. Distribución")
            jerarquia = int(input("Elija su opción: "))
            
            servicios = []
            while True:
                print("Elija un servicio:")
                print("1. Datos")
                print("2. VLAN")
                print("3. Trunking")
                print("4. Salir")
                servicio = int(input("Elija su opción: "))
                
                if servicio == 4:
                    break
                elif servicio >= 1 and servicio <= 3:
                    servicios.append(servicio)
                else:
                    print("Opción no válida. Intente de nuevo.")
            
            file.write(f"\n---------------------------------\n")
            file.write(f"Dispositivo: {nombre}\n")
            if jerarquia == 1:
                file.write("Jerarquía: Núcleo\n")
            elif jerarquia == 2:
                file.write("Jerarquía: Acceso\n")
            elif jerarquia == 3:
                file.write("Jerarquía: Distribución\n")
            file.write("Servicios: ")
            if servicios:
                for servicio in servicios:
                    if servicio == 1:
                        file.write("Datos, ")
                    elif servicio == 2:
                        file.write("VLAN, ")
                    elif servicio == 3:
                        file.write("Trunking, ")
                file.write("\n")
            else:
                file.write("Ninguno\n")
            file.write("---------------------------------\n")
            
            print("Dispositivo agregado correctamente.")
            input("Presiona Enter para continuar...")
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
        for i, item in enumerate(campus, 1):
            print(f"{i}. {item}")
        input("\nPulsa Enter para continuar...")
    elif selector == 3:
        menu_add_disp()
    elif selector == 4:
        os.system("cls")
        print("Función para añadir campus.")
        input("\nPulsa Enter para continuar...")
    elif selector == 5:
        os.system("cls")
        print("Función para borrar dispositivo.")
        input("\nPulsa Enter para continuar...")
    elif selector == 6:
        os.system("cls")
        print("Función para borrar campus.")
        input("\nPulsa Enter para continuar...")
    elif selector == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
