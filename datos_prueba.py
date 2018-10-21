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
    giorno_giovanna = ["contraseña", "Giorno", "Giovanna", "hombre", 18, (0, 0), ["helado", "italia", "taxis", "robar"]]
    jotaro_kujo = ["contraseña", "Jotaro", "Kujo", "hombre", 28, (0, 0), ["delfines", "fumar", "poker"]]
    lisa_lisa = ["contraseña", "Lisa", "Lisa", "mujer", 36, (0, 0), ["baño-de-inmersion", "bufandas", "lentes"]]
    suzi_q = ["contraseña", "", "", "", , (, ), ["fotografia", "japon", "bromas", ""]]
    joseph_joestar = ["contraseña", "", "", "", , (, ), ["disfraces", "armas", "nueva-york", ""]]
    dio_brando = ["contraseña", "", "", "", , (, ), ["sangre", "poder", "gatos", "relojes", "cuchillos"]]
    erina_pendleton = ["contraseña", "", "", "", , (, ), ["medicina", "", "", ""]]


    diccionario = {"juan_perez": juan_perez, "giorno_giovanna": giorno_giovanna, "jotaro_kujo": jotaro_kujo, "lisa_lisa": lisa_lisa, "suzi_q": suzi_q, "joseph_joestar": joseph_joestar, "dio_brando": dio_brando, "erina_pendleton": erina_pendleton, , }

    return diccionario