def confirm_data(datosUsuario):
    file = open("datos.txt", "r")
    lineas = file.readlines()
    print(lineas)
    flag = True

    for linea in lineas:
        print(linea)
        datos = linea.split()
        flag = True
        for i in range(len(datos)):
            if datos[i] != datosUsuario[i]:
                flag = False
        if flag:
            return True

    file.close()
    return False

print(confirm_data('Laura Rojas Osorio 1794623489236531 536'.split()))