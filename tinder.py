###uso 3 numeral (###) para cuando el mensaje es para nosotros
###uso 1 numeral (#) para cuando el mensaje es para los profes

###lo mejor seria priorizar las funciones importantes como registro, ingresar, editar, etc. y dejar para lo ultimo las petes como sex, age, etc.


from datos_prueba import cargar_datos_prueba
from geopy.distance import geodesic


def menu_principal():
    print("MENU PRINCIPAL\n")
    print("1: Cargar conjunto prueba")
    print("2: Registrarse en el sistema")
    print("3: Ingresar al sistema")
    print("4: Editar usuario existente")
    print("5: Salir")
    user_input = input("Por favor elija una de las opciones para proseguir:\n")  #guarda la respuesta del usuario en esa variable y la usamos para decidir que hacer
    while user_input not in (*"12345",):     #tupla conteniendo las opciones empaquetadas. verifica que el usuario no ingrese entradas no permitidas
        user_input = input("Entrada no válida. Por favor, elija una de las opciones indicadas:\n")
    return user_input

        
def registro():
    nombre = input("Ingrese su nombre\n")
    apellido = input("Ingrese su apellido\n")
    pseudonimo = nuevo_pseudonimo()
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
        pseudonimo = input("Ingrese su pseudonimo, compuesto unicamente de minusculas, numeros y guiones bajos\nPseudonimo: ")
        if pseudonimo in dicc_usuarios:
            print("El pseudónimo elegido ya esta en uso. Por favor eliga otro")
        elif not esValidoPseudonimo(pseudonimo):        #Entra a esta parte si el pseudonimo no es valido
            print("El pseudónimo solo puede contener minusculas, números y guiones bajos '_'")
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
        santo_y_seña = input("Ingrese contraseña de al menos 5 caracteres con numeros, minusculas y mayusculas\n Contraseña: ")
        if len(santo_y_seña) >= 5:
            valido = "No se"
            i = -1
            while valido == "No se":
                i += 1
                if santo_y_seña[i] not in tupla_mayusculas:
                    if santo_y_seña[i] not in tupla_minusculas:
                        if santo_y_seña[i] not in tupla_numeros:                      ###es como 3D OOoo..ooOOoo..
                            valido = "No"
                            numero = False
                            print("Caracter(es) invalido(s)")
                        else:
                            numero = True
                    else:
                        minuscula = True
                else:
                    mayuscula = True
                if valido == "No se" and len(santo_y_seña) == i:
                    valido = "Si"
    return santo_y_seña



def sex():
    sexo_valido = False
    ##salir = False
    caracteres_permitidos = ("h", "m", "i", "hombre", "mujer", "indefinido")
    while not sexo_valido: ##or not salir:
        sexo = input("Ingrese sexo\n'h' hombre\n'm' mujer\n'i' indefinido\nSexo:").lower()      #'s' salir
        if sexo in caracteres_permitidos:
            sexo_valido = True
        else:
            print("Invalido")
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
        edad = input("Ingrese su edad")
        if len(edad) > 2:       ###es para que la funcion no compare caracter por caracter si es que son muchos, porque ya es invalido
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
    return int(edad)





def location():





def interests():
    otro_mas = True
    intereses = []
    while otro_mas:
        interes = input("Ingrese un interes, o 'exit'\n").lower().strip()
        interes = interes.replace(" ", "-")
        if interes != "exit":
            if es_valido_interes(interes, intereses):
                intereses.append(interes)
                print("{} ha sido agregado a sus intereses".format(interes))
            else:
                print("Caracteres invalidos, o el interes ya se encuentra en su lista de intereses")
        else: otro_mas = False
    return intereses

def es_valido_interes(interes, intereses):
    caracteres_validos = (*"abcdefghijklmnopqrstuvwxyz1234567890-",)
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
    while not usuarioValido or not salir:
        pseudonimo = input("ingrese su nombre de usuario (pseudonimo)\nusuario: ")
        usuarioValido = True
        if pseudonimo not in dicc:
            print("usuario equivocado. Inténtelo de nuevo")
            usuarioValido = False
            respuesta = input("desea continuar? (0 para salir, cualquier cosa para continuar\n")
        if respuesta == "0":
            salir = True

    contraseñaValida = False
    while not contraseñaValida or not salir:
        contraseña = input("ingrese su contraseña\ncontraseña: ")
        if contraseña == dicc[pseudonimo][0]:
            contraseñaValida = True
        else:
            print("contraseña inválida")
            respuesta = input("desea continuar? (0 para salir, cualquier cosa para continuar\n")
        if respuesta == "0":
            salir = True
    if usuarioValido and contraseñaValida:
        return pseudonimo,True
    return None,False

    
def editar():        ###OPCIONAL, NO HACER BAJO NINGUNA CIRCUNSTANCIA   -/- suena como un reto ¬.o





def busqueda(pseudonimo):       ### devuelve los datos para hacer la busqueda en un diccionario
    print("Sexo en el que esta interesade")
    sexo_buscar = sex()
    print("Rango de edades en las que esta interesade")
    rango_edad = age()
    rango_distancia = float(input("rango de busqueda\nIngrese el rango máximo de busqueda en kilómetros. el número puede ser decimal:\n"))
    lista = [pseudonimo,[sexo_buscar,rango_edad,rango_distancia]]
    return lista

def findMatch(dicc_usuarios,lista_busqueda):       ###le das el diccionario con el usuario que esta buscando un match y sus preferencias (rango edades, sexo y rango distancia)
    info_usuario = dicc_usuarios.pop(lista_busqueda[0])     #quita al usuario en sesion del diccionario y devuelve su informacion (value correspondiente a esa key) a info_usuaario.
    lista_busqueda.append(info_usuario)
    dicc_matches = {}
    for usuario in dicc_usuarios:           #por cada usuario en el diccionario se fija si hacen match. si hay, mete a ese usuario y sus datos (values) en otro diccionario 'dicc_matches'
        edad_min = lista_busqueda[1][1][0]
        edad_max = lista_busqueda[1][1][1]
        sexo_interesado = lista_busqueda[1][0]
        distancia_al_usuario = geodesic(dicc_usuarios[usuario][5],info_usuario[5])
        if (edad_min < dicc_usuarios[usuario][4] < edad_max) and (dicc_usuarios[usuario][3] == sexo_interesado) and (distancia_al_usuario <= lista_busqueda[0][2]):
            datos = dicc_usuarios.pop(usuario)
            dicc_matches.update({usuario:datos})
    return dicc_matches,lista_busqueda          ###lista_busqueda ahora tambien tiene los datos de su usuario. no se si vale la pena hacer esto. quizas lo cambie. esta asi porque va a usar info agregada en la funcion de abajo

def porcentaje_match(dicc_matches,lista_busqueda):      ### debe mostrar los usarios matcehados y el porcentaje de match de cada uno.






#Bloque principal


print("Bienvenide a la version python de tinder! >w< <3")
diccionario_usuarios = {}           ###aca van a ir todos los usuarios. los cargados y los nuevos      
diccionario_usuarios_nuevos = {}    ###aca solo van a estar los usuarios nuevos
opcion_usuario = 0
while opcion_usuario == 0:       #ciclo que ejecuta la funcion adecuada segun la opcion elegida
    opcion_usuario = menu_principal()
    if opcion_usuario == "1":
        diccionario_usuarios_prueba = cargar_datos_prueba()        ###hay que hacer un append para un diccionario mayor, y no permitir que se cargue varias veces
        diccionario_usuarios.update(diccionario_usuarios_prueba)
        print("Los datos han sido cargados")
        opcion_usuario = "0"
    elif opcion_usuario == "2":
        usuario_nuevo = registro()
        diccionario_usuarios_nuevos.update(usuario_nuevo)
    elif opcion_usuario == "3":
        pseudonimoIngresado,valido = ingresar(diccionario_usuarios)
        if not valido:
            opcion_usuario = menu_principal()
        else:
            lista_busqueda = busqueda(diccionario_usuarios,pseudonimoIngresado)
    elif opcion_usuario == "4":
        editar()
    elif opcion_usuario == "5":     ###pongo elif por las dudas, cambiar luego de testear mucho
        exit()