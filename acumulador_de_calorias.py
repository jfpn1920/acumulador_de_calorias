ids = []
alimentos = []
cantidades = []
calorias = []
totales = []
#-------------------------------------------#
#--|menu_principal_acumulador_de_calorias|--#
#-------------------------------------------#
while True:
    print("menu principal acumulador de calorias")
    print("1) crear registro")
    print("2) editar registro")
    print("3) eliminar registro")
    print("4) buscar registro")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_registro|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_registro = 1
        else:
            id_registro = ids[-1] + 1
        alimento = input("nombre del alimento: ")
        cantidad = int(input("cantidad consumida: "))
        calorias_porcion = int(input("calorías por porción: "))
        total = cantidad * calorias_porcion
        ids.append(id_registro)
        alimentos.append(alimento)
        cantidades.append(cantidad)
        calorias.append(calorias_porcion)
        totales.append(total)
        print("registro creado correctamente.")
        print("id:", id_registro)
    #---------------------#
    #--|editar_registro|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar registro")
            for i in range(len(ids)):
                print(f"{ids[i]:<4} {alimentos[i]:<20} {cantidades[i]:<10} {calorias[i]:<11} {totales[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("alimento:", alimentos[posicion])
                print("cantidad:", cantidades[posicion])
                print("calorías:", calorias[posicion])
                print("total:", totales[posicion])
                alimentos[posicion] = input("nuevo alimento: ")
                cantidades[posicion] = int(input("nueva cantidad: "))
                calorias[posicion] = int(input("nuevas calorías por porción: "))
                totales[posicion] = cantidades[posicion] * calorias[posicion]
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_registro|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar registro")
            for i in range(len(ids)):
                print(f"{ids[i]:<4} {alimentos[i]:<20} {cantidades[i]:<10} {calorias[i]:<11} {totales[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print("id:", ids[posicion])
                print("alimento:", alimentos[posicion])
                print("cantidad:", cantidades[posicion])
                print("calorías:", calorias[posicion])
                print("total:", totales[posicion])
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    alimentos.pop(posicion)
                    cantidades.pop(posicion)
                    calorias.pop(posicion)
                    totales.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_registro|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar registro")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print("id:", ids[posicion])
                print("alimento:", alimentos[posicion])
                print("cantidad:", cantidades[posicion])
                print("calorías por porción:", calorias[posicion])
                print("total de calorías:", totales[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = totales[0]
            menor = totales[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]:<4} {alimentos[i]:<20} {cantidades[i]:<10} {calorias[i]:<11} {totales[i]}")
                suma = suma + totales[i]
                if totales[i] > mayor:
                    mayor = totales[i]
                if totales[i] < menor:
                    menor = totales[i]
            promedio = suma / len(ids)
            print("estadísticas acumulador de calorías")
            print("cantidad de registros:", len(ids))
            print("calorías acumuladas:", suma)
            print("promedio de calorías:", round(promedio, 2))
            print("mayor consumo:", mayor)
            print("menor consumo:", menor)
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el programa.")
        break
    else:
        print("opción inválida.")