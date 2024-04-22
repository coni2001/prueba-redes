import os
campus = ["Zona core", "Campus Uno", "Campus Matriz", "Sector Outsourcing"]
def mostrar_menu_principal():
    os.system("cls")
    print("¿Que es lo que desea hacer? \n1. Ver Campus. \n2. Ver dispositivos. \n3. Añadir Campus.  \n4. Añadir dispositivo. \n5. Borar Campus \n6. Borrar dispositivo" )
    print("Presione 'q' para salir del programa")
def menu_ver_disp():
    while True:
        os.system("cls")
        print("Seleccione el campus")
        cont = 1
        exit=0
        while len(campus) >= cont:
            for item in campus:
                print (str(cont)+".",item)
                cont += 1
                exit= cont 
            print (str(exit)+". Volver al Menú Principal")
        selector = int(input ("\nSelecciona una opción: "))
        x = int(selector)-1
        if x >= 0 and x < len(campus):
            file= open(campus[int(x)]+".txt", "r")
            for item in file:
                item=item.strip()
                print (item)
            file.close()
        elif selector == (len(campus)+1):
            print("Volviendo al Menú Principal...")
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def mostrar_submenu_2():
    while True:
        print("Submenú 2:")
        print("1. Opción A")
        print("2. Opción B")
        print("3. Volver al Menú Principal")
        opcion = input("Selecciona una opción (A, B o 3): ")

        if opcion == "A":
            print("Has seleccionado la opción A del Submenú 2")
        elif opcion == "B":
            print("Has seleccionado la opción B del Submenú 2")
        elif opcion == "3":
            print("Volviendo al Menú Principal...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Selecciona una opción: ")

        if opcion_principal == "1":
            menu_ver_disp()
        elif opcion_principal == "2":
            mostrar_submenu_2()
        elif opcion_principal == "q":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

