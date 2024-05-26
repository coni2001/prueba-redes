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
                    nom_dispositivo = input("b. Nombre de dispositivo: ")

                    ip_addresses = []
                    while True:
                        ip_address = input("c. Dirección IP (o 'q' para terminar): ")
                        if ip_address.lower() == 'q':
                            if not ip_addresses:
                                print("Debe ingresar al menos una dirección IP.")
                            else:
                                break
                        elif validar_ip_multiface(ip_address):
                            ip_addresses.append(ip_address)
                        else:
                            print("Formato de dirección IP no válido. Inténtelo de nuevo.")
                    vlans = input("d. VLAN(s) configuradas: ")
                    servicios_red = input("e. Servicios de red comprometidos: ")
                    jerarquia_opciones = {
                        1: "Núcleo",
                        2: "Acceso",
                        3: "Distribución"
                    }
                    print("f. Capa a la que pertenece, modelo jerárquico:")
                    for key, value in jerarquia_opciones.items():
                        print(f"{key}. {value}")
                    while True:
                        try:
                            jerarquia = int(input("Elija su opción: "))
                            if jerarquia in jerarquia_opciones:
                                jerarquia_str = jerarquia_opciones[jerarquia]
                                break
                            else:
                                print("Opción no válida. Inténtalo de nuevo.")
                        except ValueError:
                            print("Entrada inválida. Debe ingresar un número.")
                    
                    file.write(f"\n---------------------------------\n")
                    file.write(f"Tipo de dispositivo: {tipo_dispositivo}\n")
                    file.write(f"Nombre de dispositivo: {nom_dispositivo}\n")
                    file.write("Direccionamiento IP:\n")
                    for ip in ip_addresses:
                        file.write(f"  - {ip}\n")
                    file.write(f"VLAN(s) configuradas: {vlans}\n")
                    file.write(f"Servicios de red: {servicios_red}\n")
                    file.write(f"Capa a la que pertenece, (modelo jerárquico): {jerarquia_str}\n")
                    file.write("---------------------------------\n")
                    
                    print("Dispositivo agregado correctamente.")
                    input("Presiona Enter para continuar.")
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                input("Presiona Enter para continuar")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
            input("Presiona Enter para continuar.")