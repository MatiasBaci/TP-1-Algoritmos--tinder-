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
    user_input = input("Eleji una de las opciones para proseguir\n>")  #guarda la respuesta del usuario en esa variable y la usamos para decidir que hacer
    while user_input not in (*"12345",):     #tupla conteniendo las opciones empaquetadas. verifica que el usuario no ingrese entradas no permitidas
        #print("\033[1;31;40m FATAL ERROR!!1!\n")
        #time.sleep(1)
        #print("No, mentira.")
        #time.sleep(1)
        if user_input == "salir":
            user_input = "5"
        else:
            user_input = input("Entrada no válida. Eleji una de las opciones indicadas\n>")
    return user_input


def registro(diccionario_usuarios):
    nombre = input("Ingresa tu nombre\n>")
    apellido = input("Ingresa tu apellido\n>")
    pseudonimo = nuevo_pseudonimo(diccionario_usuarios)
    contraseña = password()
    sexo = sex()
    edad = age()
    ubicacion = location()
    intereses = interests()
    likes = []
    mensajes = {}
    diccionario_usuarios[pseudonimo] = {"contraseña": contraseña, "nombre": nombre, "apellido": apellido, "sexo": sexo, "edad": edad, "ubicacion": ubicacion, "intereses": intereses, "likes": likes, "mensajes": mensajes}
    return diccionario_usuarios


def nuevo_pseudonimo(dicc_usuarios):
    en_proceso = True
    while en_proceso:        ###para ver si el proceso de elegir pseudonimo esta terminado o en proceso
        pseudonimo = input("Ingresa tu pseudonimo, compuesto unicamente de minusculas, numeros y guiones bajos\n>")
        if pseudonimo in dicc_usuarios:
            print("El pseudónimo elegido ya esta en uso. Eleji otro")
            time.sleep(2)
        elif not es_valido_pseudonimo(pseudonimo):        #Entra a esta parte si el pseudonimo no es valido
            print("El pseudónimo solo puede contener minusculas, números y guiones bajos '_'")
            time.sleep(2)
        else:
            en_proceso = False
    return pseudonimo


def es_valido_pseudonimo(string_de_caracteres):           #Chequea que el pseudonimo no contenga caracteres no permitidos
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
        santo_y_seña = str(input("Ingresa contraseña de al menos 5 caracteres con numeros, minusculas y mayusculas, sin espacios\n>"))
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
        edad = input("Ingresa edad\n>")
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
            if 0 < edad < 18:
                print("La policia ha sido notificada. Un patrullero esta en camino.")
            else:
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
            if -90 <= latitud <= 90:
                lat_valido = True
            else:
                print("Te equivocaste, no pasa nada. Latitud debe estar entre -90 y 90")
    lon_valido = False
    while not lon_valido:
        try:
            longitud = float(input("Ingrese su longitud\n>"))
        except TypeError:
            print("Oopsie whoopsie no ingresaste un número. Por favor ingresa un número UwU")
            time.sleep(2)
        else:
            if -180 <= longitud <= 180:
                lon_valido = True
            else:
                print("Todos cometemos errores. Longitud debe estar entre -180 y 180")
    ubicacion = (latitud, longitud)
    return ubicacion


def interests():
    otro_mas = True
    intereses = []
    while otro_mas:
        interes = input("Ingresa un interes, '0' (cero) para salir (consideramos que 'salir' es un interes valido).\n>").lower().strip()
        interes = interes.replace(" ", "-")
        if interes != "0":
            if es_valido_interes(interes, intereses):
                intereses.append(interes)
                print("{} ha sido agregado a tus intereses".format(interes))
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
    usuario_valido = False
    salir = False
    respuesta = "1"
    while not usuario_valido and not salir:
        pseudonimo = input("Ingresa tu nombre de usuario (pseudonimo)\n>")
        usuario_valido = True
        if pseudonimo not in dicc:
            print("Usuario equivocado. Intentalo de nuevo")
            time.sleep(1)
            usuario_valido = False
            respuesta = input("Reintentar? s/n\n>")
        if respuesta == "n" or respuesta == "no":
            salir = True
    contraseña_valida = False
    while not contraseña_valida and not salir:
        contraseña = input("Ingrese su contraseña\n>")
        if contraseña == dicc[pseudonimo]["contraseña"]:
            contraseña_valida = True
        else:
            print("Contraseña inválida")
            time.sleep(1)
            respuesta = input("Reintentar? s/n\n>")
        if respuesta == "n" or respuesta == "no":
            salir = True
    if usuario_valido and contraseña_valida:
        return pseudonimo, True
    return None, False


def busqueda(pseudonimo):       ### devuelve los datos para hacer la busqueda en un diccionario
    print("Sexo en el que esta interesade\n")
    time.sleep(1)
    sexo_buscar = sex()
    time.sleep(1)
    #rango_edad = age()
    print("Edad minima de busqueda")
    time.sleep(0.5)
    edad_min = age()
    print("Edad maxima de busqueda")
    time.sleep(0.5)
    edad_max = age()
    rango_distancia = float(input("Rango de busqueda\nIngrese el rango máximo de busqueda en kilómetros, puede ser decimal\n>"))
    dicc_busqueda = {"pseudonimo": pseudonimo, "sexo_buscar": sexo_buscar, "rango_edad": (edad_min, edad_max), "rango_distancia": rango_distancia}
    return dicc_busqueda


def find_match(dicc_usuarios, dicc_busqueda):       ###le das el diccionario con el usuario que esta buscando un match y sus preferencias (rango edades, sexo y rango distancia)
        #dicc_usuarios es el diccionario con todos los usuarios
        #dicc_busqueda tiene el pseudonimo del usuario actual y sus parametros de busqueda
    dicc_matches = {}
    for usuario in dicc_usuarios:           #por cada usuario en el diccionario se fija si hacen match. si hay, mete a ese usuario y sus datos (values) en otro diccionario 'dicc_matches'
        edad_min = dicc_busqueda["rango_edad"][0]
        edad_max = dicc_busqueda["rango_edad"][1]
        sexo_interesado = dicc_busqueda["sexo_buscar"]
        distancia_al_usuario = geodesic(dicc_usuarios[usuario]["ubicacion"], dicc_usuarios[dicc_busqueda["pseudonimo"]]["ubicacion"]).kilometers
        if (edad_min <= dicc_usuarios[usuario]["edad"] <= edad_max) and (dicc_usuarios[usuario]["sexo"] == sexo_interesado) and (distancia_al_usuario <= dicc_busqueda["rango_distancia"]):
            datos = dicc_usuarios[usuario]
            dicc_matches.update({usuario: datos})
    if dicc_busqueda["pseudonimo"] in dicc_matches: #si el usuario que esta buscando ahora se encuentra en sus propios matches lo quita
        del dicc_matches[dicc_busqueda["pseudonimo"]]
    if dicc_matches == {}:
        print("No hubo ningun match. Estas destinadx a morir solx :(")
        time.sleep(2)
    return dicc_matches, dicc_busqueda


def porcentaje_match(dicc_matches, dicc_busqueda, dicc_usuarios):      #muestra los usarios matcehados y el porcentaje de match de cada uno.
    pseudonimo = dicc_busqueda["pseudonimo"]
    print("En base a tus gustos, te mostraremos tu porcentaje de exito en una relacion con cada persona que encontramos.")
    time.sleep(3)
    print("Este porcentaje es completamente eficaz y para nada arbitrario a la hora de juzgar cuanto se parecen dos personas.")
    time.sleep(3)
    print("No, cuantificar la personalidad de alguien y reducirlo a un porcentaje no es absurdo.")
    time.sleep(3)
    input("Presiona Enter para continuar")
    for match in dicc_matches:
        lista_intereses_match = dicc_matches[match]["intereses"]
        lista_intereses_usuario = dicc_usuarios[pseudonimo]["intereses"]
        comun = 0
        for interest in lista_intereses_usuario:      #se fija cuantos intereses del usuario estan en los intereses del match
            if interest in lista_intereses_match:
                comun += 1
        #total = len(lista_intereses_match) + len(lista_intereses_usuario)
        #porcentaje = 100 * 2 * comun / total       mas parecida a la consigna pero que funciona + o -
        porcentaje = 100 * comun / len(lista_intereses_usuario)
        porcentaje = round(porcentaje)
        nombre = dicc_matches[match]["nombre"]
        apellido = dicc_matches[match]["apellido"]
        print("Match!!! OwO <3 {} {} y vos tienen un {}% de intereses en comun.".format(nombre, apellido, porcentaje))
        time.sleep(1)
        respuesta = input("like/hate ?\n>").lower   #si el usuario quiere dejar like, y mensaje
        ###por alguna razon la primera vez siempre entra al while, sin importar lo que pongas
        time.sleep(1)
        while respuesta != "like" and respuesta != "hate":
            respuesta = input("Respuesta no valida. Like/hate ?\n>").lower()
            time.sleep(1)
        if respuesta == "like":
            dicc_usuarios[match]["likes"].append("{}".format(pseudonimo))
            print("Le dejaste un like a {}".format(nombre))
            time.sleep(1)
            if dicc_usuarios[pseudonimo] in dicc_usuarios[match]["likes"]:
                respuesta = input("{} ya te habia dejado un like a vos. ¿Queres dejar un mensaje? s/n\n>".format(nombre)).lower
                if respuesta == "s" or respuesta == "si":
                    print("Solo podes dejar un mensaje. Usalo bien.")
                    time.sleep(1)
                    mensaje = input("Escribi tu mensaje.\n>")
                    #dicc_usuarios[match]["mensajes"]{pseudonimo} = mensaje
                    #print("Mensaje enviado.")
                    print("El mensaje no se pudo enviar porque no hay internet.")
                    time.sleep(1)


def ver_mensajes(pseudonimo, dicc_usuarios):
    if dicc_usuarios[pseudonimo]["mensajes"]:
        for persona_que_mando_msg in dicc_usuarios[pseudonimo]["mensajes"]:
            mensaje = dicc_usuarios[pseudonimo]["mensajes"][persona_que_mando_msg]
            print("{} dice: {}".format(persona_que_mando_msg, mensaje))
            time.sleep(3)
    else:
        print("Tenias tantos mensajes que no habia mas memoria en nuestros servidores asi que los borramos todos.")
        time.sleep(3)
        print("Ok, miento. Nadie te dejo nada.")
        time.sleep(2)

#Bloque principal

print("Bienvenide a la version python de tinder! >w< <3")
dicc_usuarios = {}           #aca van a ir todos los usuarios. los cargados y los nuevos
#diccionario_usuarios_nuevos = {}    #aca solo van a estar los usuarios nuevos
opcion_usuario = "0"
datos_ya_cargados = False
while opcion_usuario == "0":       #ciclo que ejecuta la funcion adecuada segun la opcion elegida
    opcion_usuario = menu_principal()
    if opcion_usuario == "1":       #carga los datos del otro archivo si es que no se hizo antes
        if not datos_ya_cargados:
            dicc_usuarios_prueba = cargar_datos_prueba()
            dicc_usuarios.update(dicc_usuarios_prueba)
            datos_ya_cargados = True
            print("Los datos han sido cargados")
            time.sleep(1)
        else:
            print("No se cargaron datos porque ya habian sido cargados.")
            time.sleep(2)
        opcion_usuario = "0"
    elif opcion_usuario == "2":
        dicc_usuarios.update(registro(dicc_usuarios))
        print("Usuario registrado con exito.")
        time.sleep(1)
        opcion_usuario = "0"
    elif opcion_usuario == "3":
        pseudonimo_ingresado, valido = ingresar(dicc_usuarios)
        if valido:
            respuesta = ""
            while respuesta != "salir":
                respuesta = input("Queres ver tus mensajes? s/n/salir\n>").lower()
                if respuesta == "s":
                    ver_mensajes(pseudonimo_ingresado, dicc_usuarios)
                    respuesta = "n"
                elif respuesta != "n" and respuesta != "salir":
                    print("Tomo eso como un 'no'.")
                    time.sleep(1)
                    respuesta = "salir"
                if respuesta != "salir":
                    respuesta = input("Queres buscar tu alma gemela? s/n/salir\n>").lower()
                    if respuesta == "s":
                        dicc_busqueda = busqueda(pseudonimo_ingresado)
                        dicc_matches, dicc_busqueda = find_match(dicc_usuarios, dicc_busqueda)
                        if dicc_matches:
                            porcentaje_match(dicc_matches, dicc_busqueda, dicc_usuarios)
                    elif respuesta == "n":
                        respuesta = "salir"
                    elif respuesta != "salir":
                        print("Tomo eso como un 'no'.")
                        time.sleep(1)
                        respuesta = "salir"
        opcion_usuario = "0"
    elif opcion_usuario == "4":
        print("Editar? No hay presupuesto para tantas funcionalidades.")
        time.sleep(3)
        opcion_usuario = "0"
    elif opcion_usuario == "5":     ###pongo elif por las dudas, cambiar luego de testear mucho
        print("Chau hermosx <3")
        time.sleep(3)
        exit()
