#Menu principal
#import datos_prueba




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

opciones(opcion): #toma la opcion del usuario en forma de string
    if opcion == "1":
        





print("bienvenido a la version python de tinder! OwO")

opcion_usuario = menuPrincipal()
opciones(opcion_usuario) #funcion que toma la opcion del usuario y llama a la funcion correspondiente a esa opcion