#Diccionario con los usuarios de testeo


#- Pseudónimo (único en el sistema, solo minúsculas, números y guión bajo)
#- Contraseña (requiere al menos una mayúscula, una minúscula, un dígito decimal, y un
#largo mínimo de 5 caracteres)
#- Nombre
#- Apellido
#- Sexo
#   - Indefinido
#   - Mujer
#   - Hombre
#- Edad (de 18 a 99)
#- Ubicación actual: Latitud y longitud en grados decimales (ejemplo: 41.40338, 2.17403)
#- Intereses
#   - Los intereses son una lista de etiquetas (palabras sin espacios ni acentos, unidas
#   con guiones medios) a ser ingresadas por los usuarios. Por ejemplo: basquet,
#   green-day, star-wars, nueva-york, fotografia, francia, asado, bicicleta, taekwondo,
#   buenos-aires.

def cargar_datos_prueba():
    juan_perez = {"contraseña": "contraseña", "nombre": "Juan", "apellido": "Perez", "sexo": "hombre", "edad": 34, "ubicacion": (1, 2), "intereses": ["hax", "sushi", "roirros", "troirros"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    giorno_giovanna = {"contraseña": "contraseña", "nombre": "Giorno", "apellido": "Giovanna", "sexo": "hombre", "edad": 18, "ubicacion": (0, 0), "intereses": ["hax", "helado", "italia", "taxis", "robar", "oro", "animales", "plantas"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    jotaro_kujo = {"contraseña": "contraseña", "nombre": "Jotaro", "apellido": "Kujo", "sexo": "hombre", "edad": 28, "ubicacion": (0, 0), "intereses": ["hax", "delfines", "fumar", "poker"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    lisa_lisa = {"contraseña": "contraseña", "nombre": "Lisa", "apellido": "Lisa", "sexo": "mujer", "edad": 36, "ubicacion": (0, 0), "intereses": ["hax", "baño-de-inmersion", "bufandas", "lentes"], "likes": ["ciroluiro", "dio_brando", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY", "matiasbaci": "pito culo caca pedo"}}
    suzi_q = {"contraseña": "contraseña", "nombre": "Suzi", "apellido": "Q", "sexo": "mujer", "edad": 50, "ubicacion": (0, 0), "intereses": ["hax", "fotografia", "japon", "bromas"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    joseph_joestar = {"contraseña": "contraseña", "nombre": "Joseph", "apellido": "Joestar", "sexo": "hombre", "edad": 50, "ubicacion": (50, 10), "intereses": ["hax", "disfraces", "armas", "nueva-york"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    dio_brando = {"contraseña": "contraseña", "nombre": "Dio", "apellido": "Brando", "sexo": "hombre", "edad": 99, "ubicacion": (0, 0), "intereses":["hax", "sangre", "poder", "gatos", "relojes", "cuchillos"], "likes": ["ciroluiro", "matiasbaci", "lisa_lisa"], "mensajes": {"ciroluiro": "nuinos", "matiasbaci": "pito culo caca pedo pis"}}
    erina_obacha = {"contraseña": "contraseña", "nombre": "Erina", "apellido": "Pendleton", "sexo": "mujer", "edad": 18, "ubicacion":  (10, 6), "intereses": ["hax", "medicina", "barro"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    jane_doe = {"contraseña": "contraseña", "nombre": "Jane", "apellido": "Doe", "sexo": "mujer", "edad": 25, "ubicacion": (0, 0), "intereses": ["hax", "asado", "musica", "green-day", "star-wars"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    john_doe = {"contraseña": "contraseña", "nombre": "John", "apellido": "Doe", "sexo": "hombre", "edad": 25, "ubicacion": (0, 0), "intereses": ["hax", "bicicleta", "taekwondo", "buenos-aires", "basquet"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    kakyoin = {"contraseña": "contraseña", "nombre": "Noriaki", "apellido": "Kakyoin", "sexo": "hombre", "edad": 18, "ubicacion": (89, 1), "intereses": ["hax", "chupetines", "cerezas", "esmeraldas", "verde", "lentes"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    von_stroheim = {"contraseña": "contraseña", "nombre": "Rudol", "apellido": "Von Stroheim", "sexo": "hombre", "edad": 27, "ubicacion": (0, 0), "intereses": ["hax", "SS", "alemania", "mechs"], "likes": ["ciroluiro", "dio_brando"], "mensajes": {"ciroluiro": "nuinos", "dio_brando": "WRYYYYYYY"}}
    diccionario = {"juan_perez": juan_perez, "giorno_giovanna": giorno_giovanna, "jotaro_kujo": jotaro_kujo, "lisa_lisa": lisa_lisa, "suzi_q": suzi_q, "joseph_joestar": joseph_joestar, "dio_brando": dio_brando, "erina_obacha": erina_obacha, "jane_doe": jane_doe, "john_doe": john_doe, "kakyoin": kakyoin, "von_stroheim": von_stroheim}
    return diccionario


#if __name__ == "__main__":
#    usuarios = cargar_datos_prueba()
#    for pseudonimo in usuarios:
#        print("{pseudonimo}\n{} {} {} {} {} {} {}".format(usuarios[pseudonimo][contraseña],usuarios[pseudonimo][nombre],usuarios[pseudonimo][apellido],usuarios[pseudonimo][sexo],usuarios[pseudonimo][edad],usuarios[pseudonimo][ubicacion],usuarios[pseudonimo][intereses]) )