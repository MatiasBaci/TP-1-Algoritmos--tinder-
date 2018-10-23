def password():
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
        santo_y_sena = str(input("Ingrese contraseña de al menos 5 caracteres con numeros, minusculas y mayusculas\n"))
        if len(santo_y_sena) >= 5:
            valido = "No se"
            i = -1
            while valido == "No se":
                i += 1
                if santo_y_sena[i] not in tupla_mayusculas:
                    if santo_y_sena[i] not in tupla_minusculas:
                        if santo_y_sena[i] not in tupla_numeros:                      ###es como 3D OOoo..ooOOoo.. whoa
                            valido = "No"
                            numero = False
                            print("Caracter(es) invalido(s)")
                        else:
                            numero = True
                    else:
                        minuscula = True
                else:
                    mayuscula = True
                if valido == "No se" and len(santo_y_sena) == i:
                    valido = "Si"

def password2():
    tupla_mayusculas = (*"ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",)
    tupla_minusculas = (*"abcdefghijklmnñopqrstuvwxyz",)
    tupla_numeros = (*"0123456789",)
    lista_mayusculas = []
    lista_minusculas = []
    lista_numeros = []
    contrasena = input("Ingrese contrasena de 5+ caracteres con al menos un numero, una letra")
    valido = False
    while not valido:


password()