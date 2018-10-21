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
    juan_perez = ["1235JoJo", "Juan", "Perez", "hombre", 34, (1, 2), ["sushi", "roirros", "troirros"]]
    giorno_giovanna = ["contraseña", "Giorno", "Giovanna", "hombre", 18, (0, 0), ["helado", "italia", "taxis", "robar", "oro", "animales", "plantas"]]
    jotaro_kujo = ["contraseña", "Jotaro", "Kujo", "hombre", 28, (0, 0), ["delfines", "fumar", "poker"]]
    lisa_lisa = ["contraseña", "Lisa", "Lisa", "mujer", 36, (0, 0), ["baño-de-inmersion", "bufandas", "lentes"]]
    suzi_q = ["contraseña", "Suzi", "Q", "mujer", 50, (, ), ["fotografia", "japon", "bromas", ""]]
    joseph_joestar = ["contraseña", "Joseph", "Joestar", "hombre", 50, (, ), ["disfraces", "armas", "nueva-york", ""]]
    dio_brando = ["contraseña", "Dio", "Brando", "hombre", 99, (, ), ["sangre", "poder", "gatos", "relojes", "cuchillos"]]
    erina_obacha = ["contraseña", "Erina", "Pendleton", "mujer", 18, (, ), ["medicina", "", "", ""]]
    jane_doe = ["contraseña", "Jane", "Doe", "mujer", 25, (, ), ["asado", "musica", "green-day", "star-wars"]]
    john_doe = ["contraseña", "John", "Doe", "hombre", 25, (, ), ["bicicleta", "taekwondo", "buenos-aires", "basquet"]]
    kakyoin = ["contraseña", "Noriaki", "Kakyoin", "hombre", 18, (, ), ["chupetines", "cerezas", "esmeraldas", "verde", "lentes"]]
    straizzo = ["contraseña", "Dire", "Straizzo", "hombre", 27, (, ), ["", "", "", ""]]
    diccionario = {"juan_perez": juan_perez, "giorno_giovanna": giorno_giovanna, "jotaro_kujo": jotaro_kujo, "lisa_lisa": lisa_lisa, "suzi_q": suzi_q, "joseph_joestar": joseph_joestar, "dio_brando": dio_brando, "erina_obacha": erina_obacha, "jane_doe": jane_doe, "john_doe": john_doe, "kakyoin": kakyoin, "straizzo": straizzo}
    return diccionario