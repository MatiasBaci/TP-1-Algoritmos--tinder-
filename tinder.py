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
    diccionario_usuarios2[pseudonimo] = [contraseña, nombre, apellido, sexo, edad, ubicacion, intereses]
    return diccionario_usuarios2

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
    ##tupla_del_string = (*string_de_caracteres,)         #Lo mismo que con la tupla 'caracteres_permitidos' pero con el pseudonimo
    ##for caracter in tupla_del_string:
    for caracter in string_de_caracteres:
        if caracter not in caracteres_permitidos:
            return False
    return True



def password():



def sex():                      ###dejar estas funciones menores para el final
    sexo_valido = False
    ##salir = False
    caracteres_permitidos = ("h", "m", "i", "hombre", "mujer", "indefinido")
    while not sexo_valido: ##or not salir:
        sexo = input("Ingrese sexo\n'h' hombre\n'm' mujer\n'i' indefinido\n's' salir\nSexo:").lower()
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



def ingresar():                         ###no me parece bueno hacer esto con funciones. son muchas cosas que tiene que hacer que no tiene mucho sentido que 
                                        ###este en una funcion en vez de el cuerpo del programa. sino es como que el programa entero es una funcion
                                        




def editar():        ###OPCIONAL




def salir():






#Bloque principal


print("Bienvenide a la version python de tinder! >w< <3")
opcion_usuario = "0"
while opcion_usuario == "0":       #ciclo que ejecuta la funcion adecuada segun la opcion elegida
    opcion_usuario = menu_principal()
    if opcion_usuario == "1":
        diccionario_usuarios = cargar_datos_prueba()        ###hay que hacer un append para un diccionario mayor, y no permitir que se cargue varias veces
        print("Los datos han sido cargados")
        opcion_usuario = "0"
    elif opcion_usuario == "2":
        registro()
    elif opcion_usuario == "3":
        ingresar()
    elif opcion_usuario == "4":
        editar()
    elif opcion_usuario == "5":     ###pongo elif por las dudas, cambiar luego de testear mucho
        opcion_usuario = "6"