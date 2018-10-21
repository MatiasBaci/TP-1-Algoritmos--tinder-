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

def nuevo_pseudonimo(dicc_usuarios):        ###se tiene que fijar que no este el pseudonimo ya en el diccionario mayor
    pseudonimo = input("Ingrese su pseudonimo, compuesto unicamente de minusculas, numeros y guiones bajos\n")
    while

def password():

def sex():                      ###dejar estas funciones menores para el final

def age():

def location():

def interests():






def ingresar():




def editar():




def salir():






#Bloque principal


print("Bienvenido a la version python de tinder! OwO")
opcion_usuario = 0
while opcion_usuario == 0:       #ciclo que ejecuta la funcion adecuada segun la opcion elegida
    opcion_usuario = menu_principal()
    if opcion_usuario == "1":
        diccionario_usuarios = cargar_datos_prueba()        ###hay que hacer un append para un diccionario mayor, y no permitir que se cargue varias veces
        print("Los datos han sido cargados")
        opcion_usuario = 0
    elif opcion_usuario == "2":
        registro()
    elif opcion_usuario == "3":
        ingresar()
    elif opcion_usuario == "4":
        editar()
    elif opcion_usuario == "5":     ###pongo elif por las dudas, cambiar luego de testear mucho
        salir()