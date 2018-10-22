###uso 3 numeral (###) para cuando el mensaje es para nosotros
###uso 1 numeral (#) para cuando el mensaje es para los profes

###lo mejor seria priorizar las funciones importantes como registro, ingresar, editar, etc. y dejar para lo ultimo las petes como sex, age, etc.


from datos_prueba import cargar_datos_prueba


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
            print("el pseudónimo elegido ya esta en uso. Por favor eliga otro")
        elif not esValidoPseudonimo(pseudonimo):        #Entra a esta parte si el pseudonimo no es valido
            print("El pseudónimo solo puede contener minusculas, números y guiones bajo '_'")
        else:
            enProceso = False
    return pseudonimo


def esValidoPseudonimo(string_de_caracteres):           #Chequea que el pseudonimo no contenga caracteres no permitidos
    caracteres_permitidos = (*"abcdefghijklmnñopqrstuvwxyz1234567890_",)         #Tupla conteniendo los carateres permitidos en forma empaquetada
    tupla_del_string = (*string_de_caracteres,)         #Lo mismo que con la tupla 'caracteres_permitidos' pero con el pseudonimo
    for caracter in tupla_del_string:
        if caracter not in caracteres_permitidos:
            return False
    return True

def password():

def sex():                      ###dejar estas funciones menores para el final

def age():

def location():

def interests():






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

    




def editar():




def busqueda(pseudonimo):       ### devuelve los datos para hacer la busqueda en un diccionario
    print("sexo en el que esta interesade")
    sexo_buscar = sex()
    print("rango de edades en las que esta interesade")
    rango_edad = age()
    rango_distancia = float(input("rango de busqueda\nIngrese el rango máximo de busqueda en kilómetros. el número puede ser decimal:\n"))
    dicc = {pseudonimo:[sexo_buscar,rango_edad,rango_distancia]}
    return dicc

def findMatch(dicc_busqueda):       ###le das el diccionario con el usuario que esta buscando un match y sus preferencias (rango edades, sexo y rango distancia)
    






#Bloque principal


print("Bienvenide a la version python de tinder! >w< <3")
diccionario_usuarios = {}           ###aca van a ir todos los usuarios. los cargados y los nuevos      
diccionario_usuarios_nuevos = {}    ###aca solo van a estar los usuarios nuevos
opcion_usuario = 0
while opcion_usuario == 0:       #ciclo que ejecuta la funcion adecuada segun la opcion elegida
    opcion_usuario = menu_principal()
    if opcion_usuario == "1":
        diccionario_usuarios_prueba = cargar_datos_prueba()        ###hay que hacer un append para un diccionario mayor, y no permitir que se cargue varias veces
        print("Los datos han sido cargados")
        opcion_usuario = 0
    elif opcion_usuario == "2":
        usuario_nuevo = registro()
        diccionario_usuarios_nuevos.update(usuario_nuevo)
    elif opcion_usuario == "3":
        pseudonimoIngresado,valido = ingresar(diccionario_usuarios)
        if not valido:
            opcion_usuario = menu_principal()
        else:
            diccionario_busqueda = busqueda(pseudonimoIngresado)


    elif opcion_usuario == "4":
        editar()
    elif opcion_usuario == "5":     ###pongo elif por las dudas, cambiar luego de testear mucho
        exit()