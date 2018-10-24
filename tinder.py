###uso 3 numeral (###) para cuando el mensaje es para nosotros
###uso 1 numeral (#) para cuando el mensaje es para los profes

import time
from geopy.distance import geodesic
from datos_prueba import cargar_datos_prueba


def menu_principal():
    print("\n\nMENU PRINCIPAL\n")
    print("1: Cargar conjunto prueba")
    print("2: Registrarse en el sistema")
    print("3: Ingresar al sistema")
    print("4: Editar usuario existente")
    print("5: Salir")
    user_input = input("Por favor elija una de las opciones para proseguir\n>")  #guarda la respuesta del usuario en esa variable y la usamos para decidir que hacer
    while user_input not in (*"12345",):     #tupla conteniendo las opciones empaquetadas. verifica que el usuario no ingrese entradas no permitidas
        user_input = input("Entrada no válida. Por favor, elija una de las opciones indicadas\n>")
    return user_input


def registro(diccionario_usuarios):
    nombre = input("Ingrese su nombre\n>")
    apellido = input("Ingrese su apellido\n>")
    pseudonimo = nuevo_pseudonimo(diccionario_usuarios)
    contraseña = password()
    sexo = sex()
    edad = age()
    ubicacion = location()
    intereses = interests()
    diccionario_usuarios[pseudonimo] = [contraseña, nombre, apellido, sexo, edad, ubicacion, intereses]
    return diccionario_usuarios


def nuevo_pseudonimo(dicc_usuarios):
    enProceso = True
    while enProceso:        ###para ver si el proceso de elegir pseudonimo esta terminado o en proceso
        pseudonimo = input("Ingrese su pseudonimo, compuesto unicamente de minusculas, numeros y guiones bajos\n>")
        if pseudonimo in dicc_usuarios:
            print("El pseudónimo elegido ya esta en uso. Por favor eliga otro")
            time.sleep(2)
        elif not esValidoPseudonimo(pseudonimo):        #Entra a esta parte si el pseudonimo no es valido
            print("El pseudónimo solo puede contener minusculas, números y guiones bajos '_'")
            time.sleep(2)
        else:
            enProceso = False
    return pseudonimo


def esValidoPseudonimo(string_de_caracteres):           #Chequea que el pseudonimo no contenga caracteres no permitidos
    caracteres_permitidos = (*"abcdefghijklmnopqrstuvwxyz1234567890_",)         #Tupla conteniendo los carateres permitidos en forma empaquetada
    for caracter in string_de_caracteres:
        if caracter not in caracteres_permitidos:
            return False
    return True


def password():                     ###perdon si es confuso, ni yo la entiendo
    mayuscula = False
    tupla_mayusculas = (*"ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",)
    minuscula = False
    tupla_minusculas = (*"abcdefghijklmnñopqrstuvwxyz",)
    numero = False
    tupla_numeros = (*"0123456789",)
    while not mayuscula or not minuscula or not numero:
        mayuscula = False
        minuscula = False
        numero = False
        santo_y_seña = str(input("Ingrese contraseña de al menos 5 caracteres con numeros, minusculas y mayusculas, sin espacios\n>"))
        if len(santo_y_seña) >= 5:
            valido = "No se"
            i = -1
            while valido == "No se":
                i += 1
                if santo_y_seña[i] not in tupla_mayusculas:
                    if santo_y_seña[i] not in tupla_minusculas:
                        if santo_y_seña[i] not in tupla_numeros:                      ###es como 3D OOoo..ooOOoo.. whoa
                            valido = "No"
                            numero = False
                            print("Caracter(es) invalido(s)")
                            time.sleep(2)
                        else:
                            numero = True
                    else:
                        minuscula = True
                else:
                    mayuscula = True
                if valido == "No se" and len(santo_y_seña) == i + 1:
                    valido = "Si"
    return santo_y_seña


def sex():      ###permitir que busque varios sexos
    sexo_valido = False
    ##salir = False
    caracteres_permitidos = ("h", "m", "i", "hombre", "mujer", "indefinido")
    while not sexo_valido: ##or not salir:
        sexo = input("Ingrese sexo\n'h' hombre\n'm' mujer\n'i' indefinido\n>").lower()      #'s' salir
        if sexo in caracteres_permitidos:
            sexo_valido = True
        else:
            print("Invalido")
            time.sleep(1)
    if sexo not in ("hombre", "mujer", "indefinido"):
        if sexo == "h":
            sexo = "hombre"
        elif sexo == "m":
            sexo = "mujer"
        elif sexo == "i":
            sexo = "indefinido"
    return sexo


def age():
    invalido = True
    while invalido:
        invalido = False
        edad = input("Ingrese edad\n>")
        if len(edad) > 2 or edad == '':       ###es para que la funcion no compare caracter por caracter si es que son muchos, porque ya es invalido
            invalido = True
        else:
            for caracter in edad:
                if caracter not in (*"0123456789",):
                    invalido = True
        if not invalido:
            if int(edad) > 99 or int(edad) < 18:
                invalido = True
        if invalido:
            print("Edad invalida. Debe ser un numero entre 18 y 99.")
            time.sleep(2)
    return int(edad)


def location():
    lat_valido = False
    while not lat_valido:
        try:
            latitud = float(input("Ingrese su latitud\n>").replace(",", "."))
        except TypeError:
            print("Oopsie whoopsie no ingresaste un número. Por favor ingresa un número UwU")
            time.sleep(2)
        else:
            lat_valido = True
    lon_valido = False
    while not lon_valido:
        try:
            longitud = float(input("Ingrese su longitud\n>"))
        except TypeError:
            print("Oopsie whoopsie no ingresaste un número. Por favor ingresa un número UwU")
            time.sleep(2)
        else:
            lon_valido = True
    ubicacion = (latitud, longitud)
    return ubicacion


def interests():
    otro_mas = True
    intereses = []
    while otro_mas:
        interes = input("Ingrese un interes, o 'salir'\n>").lower().strip()
        interes = interes.replace(" ", "-")
        if interes != "salir":
            if es_valido_interes(interes, intereses):
                intereses.append(interes)
                print("{} ha sido agregado a sus intereses".format(interes))
                time.sleep(1)
            else:
                print("Caracteres invalidos, o el interes ya se encuentra en su lista de intereses")
                time.sleep(2)
        else:
            otro_mas = False
    return intereses


def es_valido_interes(interes, intereses):
    caracteres_validos = (*"abcdefghijklmnopqrstuvwxyz1234567890-",)
    if interes == '':
        return False
    for caracter in interes:
        if caracter not in caracteres_validos:  #se fija que sea valido
            return False
    if interes in intereses:    #se fija que no este repetido
        return False
    return True


def ingresar(dicc):
    usuarioValido = False
    salir = False
    respuesta = "1"
    while not usuarioValido and not salir:
        pseudonimo = input("Ingrese su nombre de usuario (pseudonimo)\n>")
        usuarioValido = True
        if pseudonimo not in dicc:
            print("Usuario equivocado. Inténtelo de nuevo")
            time.sleep(1)
            usuarioValido = False
            respuesta = input("Desea continuar? (0 para salir, cualquier cosa para continuar\n>")
        if respuesta == "0":
            salir = True
    contraseñaValida = False
    while not contraseñaValida and not salir:
        contraseña = input("Ingrese su contraseña\n>")
        if contraseña == dicc[pseudonimo][0]:
            contraseñaValida = True
        else:
            print("Contraseña inválida")
            time.sleep(1)
            respuesta = input("Desea continuar? (0 para salir, cualquier cosa para continuar)\n>")
        if respuesta == "0":
            salir = True
    if usuarioValido and contraseñaValida:
        return pseudonimo, True
    return None, False


def busqueda(pseudonimo):       ### devuelve los datos para hacer la busqueda en un diccionario
    print("Sexo en el que esta interesade\n")
    time.sleep(1)
    sexo_buscar = sex()
    time.sleep(1)
    #rango_edad = age()
    print("Edad minima de busqueda\n")
    time.sleep(0.5)
    edad_min = age()
    print("Edad maxima de busqueda\n")
    time.sleep(0.5)
    edad_max = age()
    rango_distancia = float(input("Rango de busqueda\nIngrese el rango máximo de busqueda en kilómetros, puede ser decimal\n>"))
    lista = [pseudonimo, [sexo_buscar, (edad_min, edad_max), rango_distancia]]
    return lista


def findMatch(dicc_usuarios, lista_busqueda):       ###le das el diccionario con el usuario que esta buscando un match y sus preferencias (rango edades, sexo y rango distancia)
    info_usuario = dicc_usuarios.pop(lista_busqueda[0])     #quita al usuario en sesion del diccionario y devuelve su informacion (value correspondiente a esa key) a info_usuaario.
    lista_busqueda.append(info_usuario)
    dicc_matches = {}
    for usuario in dicc_usuarios:           #por cada usuario en el diccionario se fija si hacen match. si hay, mete a ese usuario y sus datos (values) en otro diccionario 'dicc_matches'
        edad_min = lista_busqueda[1][1][0]
        edad_max = lista_busqueda[1][1][1]
        sexo_interesado = lista_busqueda[1][0]
        distancia_al_usuario = geodesic(dicc_usuarios[usuario][5], info_usuario[5]).kilometers    #VOLVER A PONER CUANDO SE SOLUCIONE GEOPY
        #distancia_al_usuario = lista_busqueda[1][2] ###PROVISORIO, REMOVER AL SOLUCIONAR GEOPY
        if (edad_min <= dicc_usuarios[usuario][4] <= edad_max) and (dicc_usuarios[usuario][3] == sexo_interesado) and (distancia_al_usuario <= lista_busqueda[1][2]):
            datos = dicc_usuarios[usuario]
            dicc_matches.update({usuario:datos})
    if dicc_matches == {}:
        print("No hubo ningun match. Estas destinadx a morir solx :(")
        time.sleep(2)
    return dicc_matches, lista_busqueda          ###lista_busqueda ahora tambien tiene los datos de su usuario. no se si vale la pena hacer esto. quizas lo cambie. esta asi porque va a usar info agregada en la funcion de abajo


def porcentaje_match(dicc_matches, lista_busqueda):      ### debe mostrar los usarios matcehados y el porcentaje de match de cada uno.
    for match in dicc_matches:
        intereses_match = dicc_matches[match][-1]
        intereses_usuario = lista_busqueda[-1]
        total = len(intereses_match) + len(intereses_usuario)
        comun = 0
        for interest in intereses_usuario:      ###se fija si cada interes del usuario esta en los intereses del match
            if interest in intereses_match:
                comun += 1
        porcentaje = 100 * 2 / total
        porcentaje = round(porcentaje)
        #porcentaje = str(porcentaje)
        #porcentaje2 = ""
        #for digito in porcentaje:
        #    while digito != '.':
        #        porcentaje2 = porcentaje2 + digito
        #porcentaje = int(porcentaje2)
        nombre = dicc_matches[match][1]
        apellido = dicc_matches[match][2]
        print("Match!!! OwO <3 {} {} y vos tienen un {}% de intereses en comun.".format(nombre, apellido, porcentaje))    ###aca deberiamos hacer que pregunte si quiere mandar un mensaje si fueron matcheados ambos
        time.sleep(1)
    print("Este porcentaje es completamente eficaz y para nada arbitrario a la hora de juzgar cuanto se parecen dos personas.")
    time.sleep(5)
    print("No, cuantificar la personalidad de alguien y reducirlo a un porcentaje no es absurdo.")
    time.sleep(5)


#Bloque principal

print("Bienvenide a la version python de tinder! >w< <3")
diccionario_usuarios = {}           ###aca van a ir todos los usuarios. los cargados y los nuevos      
diccionario_usuarios_nuevos = {}    ###aca solo van a estar los usuarios nuevos
opcion_usuario = "0"
datos_ya_cargados = False
while opcion_usuario == "0":       #ciclo que ejecuta la funcion adecuada segun la opcion elegida
    opcion_usuario = menu_principal()
    if opcion_usuario == "1":       #carga los datos del otro archivo si es que no se hizo antes
        if not datos_ya_cargados:
            diccionario_usuarios_prueba = cargar_datos_prueba()
            diccionario_usuarios.update(diccionario_usuarios_prueba)
            datos_ya_cargados = True
            print("Los datos han sido cargados")
            time.sleep(1)
        else:
            print("No se cargaron datos porque ya habian sido cargados.")
            time.sleep(2)
        opcion_usuario = "0"
    elif opcion_usuario == "2":
        diccionario_usuarios.update(registro(diccionario_usuarios))
        opcion_usuario = "0"
    elif opcion_usuario == "3":
        pseudonimoIngresado, valido = ingresar(diccionario_usuarios)
        if valido:
            #lista_busqueda = busqueda(diccionario_usuarios)
            lista_busqueda = busqueda(pseudonimoIngresado)
            dicc_matches, lista_busqueda = findMatch(diccionario_usuarios, lista_busqueda)
            porcentaje_match(dicc_matches, lista_busqueda)
        opcion_usuario = "0"
    elif opcion_usuario == "4":
        print("Editar? No hay presupuesto para tantas funcionalidades.")
        time.sleep(3)
        opcion_usuario = "0"
    elif opcion_usuario == "5":     ###pongo elif por las dudas, cambiar luego de testear mucho
        print("Chau hermose <3")
        time.sleep(3)
        exit()
