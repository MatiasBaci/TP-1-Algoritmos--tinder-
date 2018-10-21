#Menu principal
from datos_prueba import cargar_datos_prueba




menuPrincipal():
    print("MENU PRINCIPAL\n")
    print("1: Cargar conjunto prueba")
    print("2: Registrarse en el sistema")
    print("3: Ingresar al sistema")
    print("4: editar usuario existente")
    print("5: salir")
    user_input = input("Por favor elija una de las opciones para proseguir:\n")  #guarda la respuesta del usuario en esa variable y la usamos para decidir que hacer
    while user_input not in (*"12345",):     #tupla conteniendo las opciones empaquetadas. verifica que el usuario no ingrese entradas no permitidas
        user_input = input("entrada no válida. Por favor, elija una de las opciones indicadas:\n")
    return user_input

        





print("bienvenido a la version python de tinder! OwO")

opcion_usuario = menuPrincipal()
if opcion_usuario == "1":
    diccionario_usuarios = cargar_datos_prueba()
elif opcion_usuario == "2":
    