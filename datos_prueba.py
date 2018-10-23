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
    juan_perez = ["1235JoJo", "Juan", "Perez", "hombre", 34, (1, 2), ["hax", "sushi", "roirros", "troirros"]]
    giorno_giovanna = ["contraseña", "Giorno", "Giovanna", "hombre", 18, (0, 0), ["hax", "helado", "italia", "taxis", "robar", "oro", "animales", "plantas"]]
    jotaro_kujo = ["contraseña", "Jotaro", "Kujo", "hombre", 28, (0, 0), ["hax", "delfines", "fumar", "poker"]]
    lisa_lisa = ["contraseña", "Lisa", "Lisa", "mujer", 36, (0, 0), ["hax", "baño-de-inmersion", "bufandas", "lentes"]]
    suzi_q = ["contraseña", "Suzi", "Q", "mujer", 50, (0, 0), ["hax", "fotografia", "japon", "bromas"]]
    joseph_joestar = ["contraseña", "Joseph", "Joestar", "hombre", 50, (50, 10), ["hax", "disfraces", "armas", "nueva-york"]]
    dio_brando = ["contraseña", "Dio", "Brando", "hombre", 99, (0, 0), ["hax", "sangre", "poder", "gatos", "relojes", "cuchillos"]]
    erina_obacha = ["contraseña", "Erina", "Pendleton", "mujer", 18, (10, 6), ["hax", "medicina", "barro"]]
    jane_doe = ["contraseña", "Jane", "Doe", "mujer", 25, (0, 0), ["hax", "asado", "musica", "green-day", "star-wars"]]
    john_doe = ["contraseña", "John", "Doe", "hombre", 25, (0, 0), ["hax", "bicicleta", "taekwondo", "buenos-aires", "basquet"]]
    kakyoin = ["contraseña", "Noriaki", "Kakyoin", "hombre", 18, (95, 1), ["hax", "chupetines", "cerezas", "esmeraldas", "verde", "lentes"]]
    von_stroheim = ["contraseña", "Rudol", "Von Stroheim", "hombre", 27, (0, 0), ["hax", "SS", "alemania", "mechs"]]
    diccionario = {"juan_perez": juan_perez, "giorno_giovanna": giorno_giovanna, "jotaro_kujo": jotaro_kujo, "lisa_lisa": lisa_lisa, "suzi_q": suzi_q, "joseph_joestar": joseph_joestar, "dio_brando": dio_brando, "erina_obacha": erina_obacha, "jane_doe": jane_doe, "john_doe": john_doe, "kakyoin": kakyoin, "von_stroheim": von_stroheim}
    return diccionario


#if __name__ == "__main__":
#    usuarios = cargar_datos_prueba()
#    for pseudonimo in usuarios:
#        print("{pseudonimo}\n{} {} {} {} {} {} {}".format(usuarios[pseudonimo][0],usuarios[pseudonimo][1],usuarios[pseudonimo][2],usuarios[pseudonimo][3],usuarios[pseudonimo][4],usuarios[pseudonimo][5],usuarios[pseudonimo][6]) )