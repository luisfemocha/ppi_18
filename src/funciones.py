# Aqui estan funciones de la pagina para cambio de recetas

# Bibliotecas estándar
from datetime import datetime
import json

# Bibliotecas de terceros
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import streamlit as st

# Tus propios módulos
import conexion

# variables globales
ruta_ingredientes = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/' \
                    'main/src/datos/ingredientes.json'
ruta_normales = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/' \
                'dgarzonac/src/datos/recetas.json'
ruta_saludable = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/' \
                 'main/src/datos/saludables.json'
ruta_presupuesto = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/' \
                   'main/src/datos/presupuesto.json'
ruta_horneados = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/' \
                 'src/datos/horneados.json'
ruta_especiales = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/' \
                  'main/src/datos/especiales.json'
id_rutas = {
    0: 'ingredientes',
    1: 'normales',
    2: 'saludable',
    3: 'presupuesto',
    4: 'horneados',
    5: 'especiales'
}


# Para exportar las rutas / variables globales anteriores
def get_rutas():
    """
    Retorna un diccionario con las rutas asociadas a cada categoría de recetas.

    Retorna:
    - dict: Un diccionario que mapea las categorías de recetas a sus
    respectivas rutas.

    Ejemplo de uso:
    >>> rutas_recetas = get_rutas()
    >>> print(rutas_recetas)
    {0: 'ruta_ingredientes', 1: 'ruta_normales', 2: 'ruta_saludable',
    3: 'ruta_presupuesto', 4: 'ruta_horneados', 5: 'ruta_especiales'}
    """
    return {
        id_rutas[0]: ruta_ingredientes,
        id_rutas[1]: ruta_normales,
        id_rutas[2]: ruta_saludable,
        id_rutas[3]: ruta_presupuesto,
        id_rutas[4]: ruta_horneados,
        id_rutas[5]: ruta_especiales
    }


def contact_us():
    """
    Muestra la página de contacto en la interfaz de Streamlit.

    No retorna ningún valor. Muestra la página de contacto en la interfaz de
    Streamlit.

    Ejemplo de uso:
    >>> contact_us()
    """
    st.title("Contact us")
    st.write("You can contact us at the following email addresses:")
    st.write()


# Para almacenar las recetas en el estado de la sesion
def set_recetas(categoria="*", forzar=False):
    """

    Carga y almacena en la sesión las recetas de una categoría específica o
    de todas las categorías.

    Parámetros:
    - categoria (str): La categoría de recetas que se desea cargar. Si es "*",
    se cargarán todas las categorías.
    - forzar (bool): Indica si se debe forzar la recarga de las recetas,
    incluso si ya están en la sesión.

    Retorna:
    - bool: True si la carga de recetas fue exitosa, False en caso contrario.

    Ejemplo de uso:
    >>> set_recetas(categoria="recetas_normales", forzar=True)
    """
    print('entra a set_recetas()', categoria, forzar)
    rutas = get_rutas()

    def set_receta(categoria, forzar):
        nom_cat = 'recetas_' + categoria
        if nom_cat not in st.session_state or \
                nom_cat + "_json" not in st.session_state or forzar:
            print('se actualiza', cat)
            ruta = rutas[cat]
            json_recetas = cargar_datos(ruta)

            st.session_state[nom_cat + '_json'] = json_recetas

            obj_recetas = {}
            for receta in json_recetas:
                if receta["id"] not in obj_recetas:
                    obj_recetas[receta["id"]] = receta
                else:
                    print("Ya estaba la receta con id", receta["id"])

            st.session_state[nom_cat] = obj_recetas

        else:
            print('no se actualiza', cat)
            obj_recetas = st.session_state[nom_cat]

        return obj_recetas

    if categoria == "*" or categoria is None:
        st.session_state["recetas"] = {}

        # se itera por las categorias guardadas
        for cat in rutas:
            if cat == 'ingredientes':
                if 'ingredientes' not in st.session_state or forzar:
                    lista_ingredientes = pd.read_json(ruta_ingredientes)
                    lista_ingredientes = lista_ingredientes["ingredients"][0]
                    st.session_state['ingredientes'] = lista_ingredientes
                    print('se actualiza ingredientes')

                else:
                    print('no se actualiza ingredientes')

                continue

            else:
                st.session_state["recetas"].update(set_receta(cat, forzar))

    else:
        try:
            if int(categoria) in id_rutas:
                categoria = id_rutas[int(categoria)]
            else:
                print('categoria no esta en id_rutas:', categoria)

        except Exception as e:
            print("Error al castear categoria en set_receta", e)

        finally:
            if categoria in rutas:
                if 'recetas' not in st.session_state:
                    st.session_state['recetas'] = {}
                    return set_receta(categoria, forzar)
            else:
                print('categoria no esta en rutas:', categoria)
                return False


# se ajustan los datos para utilizarlos en las funciones
def cargar_datos(ruta):
    """
    Carga datos desde una URL o archivo local y devuelve un DataFrame
    de pandas.

    Parámetros:
    - ruta (str): Ruta a los datos. Puede ser una URL que contenga "raw" o una
    ruta de archivo local.

    Retorna:
    - pandas.DataFrame: Un DataFrame que contiene los datos cargados desde
    la ruta especificada.

    Ejemplo de uso:
    >>> ruta_url = "https://ejemplo.com/datos.json"
    >>> df_datos = cargar_datos(ruta_url)

    >>> ruta_local = "datos_locales.json"
    >>> df_datos_locales = cargar_datos(ruta_local)
    """
    try:
        if ruta.find("raw") > -1:
            response = requests.get(ruta)
            # Confirmar que el request de un resultado exitoso.
            if response.status_code == 200:
                # Usa .json() para archivos JSON, .text para
                # Archivos de texto, etc.
                return response.json()
            else:
                st.title("Error al leer la url.")
        else:
            with open(ruta, encoding='utf8') as contenido:
                return pd.DataFrame(json.load(contenido))
    except Exception as e:
        st.title("Error al leer el archivo " + ruta, e)
        return pd.DataFrame()


# Visualizacion de cada receta
def detalles_abiertos(recipe):
    """
    Muestra los detalles de una receta, incluyendo información sobre la
    descripción,
    el autor, la calificación, ingredientes, pasos, tiempos, nutrientes y
    otros detalles.

    Parámetros:
    - recipe (dict): Diccionario que contiene la información de la receta.

    No retorna ningún valor. Muestra los detalles de la receta en la interfaz
    de Streamlit.

    Ejemplo de uso:
    >>> receta_ejemplo = {"name": "Spaghetti Bolognese",
    "description": "Classic Italian dish...", "author": "Chef123", ...}
    >>> detalles_abiertos(receta_ejemplo)
    """
    # Verifica si se debe mostrar los detalles de esta receta
    # if receta['id'] in detalles_abiertos and detalles_abiertos[receta['id']]:
    with st.expander(f"View Details of {recipe['name']}"):
        st.subheader(recipe["name"])

        if 'logged_in' in st.session_state and st.session_state['logged_in']:
            if recipe["id"] in st.session_state.cuenta['favorites']:
                if st.button(
                        "Remove recipe from favorites",
                        key="unfav-" + recipe["id"]
                ):
                    print('se elimina la receta de favoritas')
                    st.session_state.cuenta['favorites'].remove(recipe["id"])
                    del st.session_state.favoritas[recipe["id"]]
                    conexion.actualizar_usuario(st.session_state.cuenta)
                    # vistas("home")
            else:
                if st.button(
                        "Add recipe to favorites", key="fav-" + recipe["id"]
                ):
                    print('Se agrega a favoritas la receta')
                    # print(recipe)
                    print(recipe["id"])

                    try:
                        print("se intenta encontrar la receta con el id")

                        print(
                            st.session_state['recetas_normales'][recipe["id"]])

                        if 'favoritas' not in st.session_state:
                            st.session_state['favoritas'] = {}
                        st.session_state.favoritas[recipe["id"]] = recipe
                        st.session_state.cuenta['favorites'].append(
                            recipe["id"])

                        conexion.actualizar_usuario(st.session_state.cuenta)
                        # vistas("home")
                    except Exception as e:
                        print("error a la hora de agregar favorita", e)

        # Detalles de la receta
        st.header("Recipe Details")
        st.write(f"**Description:** {recipe['description']}")
        st.write(f"**Author:** {recipe['author']}")
        st.write(f"**Rating:** {recipe['rattings']}")

        # Ingredientes
        st.header("Ingredients")
        for i, ingredient in enumerate(recipe["ingredients"]):
            st.write(f"{i + 1}. {ingredient}")

        # Pasos
        st.header("Steps")
        for i, step in enumerate(recipe["steps"]):
            st.write(f"{i + 1}. {step}")

        # Tiempos
        st.header("Times")
        preparation = recipe['times'].get('Preparation', 'No Time')
        cooking = recipe['times'].get('Cooking', 'No Time')
        st.write(f"**Preparation:** {preparation}")
        st.write(f"**Cooking:** {cooking}")

        if recipe['nutrients']:
            # Nutrientes
            st.header("Nutrients")

            for nutrient, cantidad in recipe['nutrients'].items():
                st.write(f"{nutrient}: {cantidad}")

            names_nurients = list(recipe['nutrients'].keys())

            # Convierte los valores a números usando NumPy
            values_nutrients = np.array(
                [float(value[:-1]) for value in recipe['nutrients'].values()]
            )

            # Grafica de los nutrientes
            plt.figure(figsize=(6, 4))
            plt.pie(values_nutrients, labels=names_nurients, autopct='%1.1f%%')
            st.pyplot(plt)

        # Otros detalles
        st.header("Other Details")
        st.write(f"**Servings:** {recipe['serves']}")
        st.write(f"**Difficulty:** {recipe['difficult']}")
        st.write(f"**Vote Count:** {recipe['vote_count']}")
        st.write(f"**Subcategory:** {recipe['subcategory']}")
        st.write(f"**Dish Type:** {recipe['dish_type']}")
        st.write(f"**Main Category:** {recipe['maincategory']}")

        # Buscar comentarios de una receta
        st.header("Comments")
        id_receta = recipe["id"]

        try:
            comentarios = conexion.get_comentarios(id_receta)
        except Exception as e:
            comentarios = None
            print('Error al conseguir comentarios', e)

        # Muestra los comentarios existentes
        if comentarios:
            for comentario in comentarios:
                # Convierte la fecha del comentario a un objeto datetime
                date_coment = datetime.strptime(
                    comentario['date_coment'], "%Y-%m-%d %H:%M:%S.%f"
                )
                # Formatea la fecha para mostrar solo el día y la hora hasta
                # los minutos en formato de 12 horas
                formatted_date = date_coment.strftime("%Y-%m-%d %I:%M %p")
                st.write(
                    f"{comentario['username']} said on {formatted_date}: "
                    f"{comentario['comentario']}"
                )
        else:
            st.write("No comments yet.")

        if st.session_state['logged_in']:
            # Formulario para agregar comentarios
            st.subheader("Add Comment")
            usuario = st.session_state.nombre
            nuevo_comentario = st.text_area(
                "Add your comment:", key=f'comentario_unico_{recipe["id"]}'
            )
            if st.button(
                    "Add Comment",
                    key=f'anadir_comentario_unico_{recipe["id"]}'
            ):
                if nuevo_comentario:  # Verifica si el comentario no está vacío
                    try:
                        # Agregar lógica para guardar el nuevo comentario en tu
                        # base de datos
                        conexion.insertar_comentario(
                            usuario, id_receta, nuevo_comentario
                        )
                    except Exception as e:
                        st.write(f"Error al insertar comentario: {e}")
                else:
                    st.write(
                        "Por favor, escriba un comentario antes de enviar."
                    )


# Segun esta funcion se cambian de vistas
def vistas(vista):
    """
    Cambia las vistas de la página según la opción que el usuario elija en
    la barra lateral.

    Parámetros:
    - vista (str): La vista a la que se desea cambiar. Puede ser 'home',
    'saludable', 'presupuesto', 'horneado', 'especiales', 'signup', 'login',
    o 'favorites'.

    No retorna ningún valor. Muestra la página correspondiente en la interfaz
    de Streamlit.

    Ejemplo de uso:
    >>> vistas('saludable')
    """

    if vista == 'home':
        home_page()
    elif vista == 'saludable':
        recetas_saludables()
    elif vista == 'presupuesto':
        recetas_presupuesto()
    elif vista == 'horneado':
        recetas_horneados()
    elif vista == 'especiales':
        recetas_especiales()
    elif vista == 'contact_us':
        contact_us()
    elif vista == 'signup':
        conexion.sign_up()
    elif vista == 'login':
        conexion.log_in()
    elif vista == 'favorites':
        conexion.recetas_favoritas()
    elif vista == 'account':
        detalles_cuenta()
    else:
        print("Error en funcion vistas. Caso no apreciado " + vista)


def filtrar_ingredientes(ingredientes_deseados,
                         ingredientes_excluir,
                         df_recetas):
    """
    Filtra un DataFrame de recetas en función de los ingredientes deseados y
    los ingredientes a excluir.

    Parámetros:
    - ingredientes_deseados (list): Lista de ingredientes que se
    desean incluir en las recetas.
    - ingredientes_excluir (list): Lista de ingredientes que se
    deben excluir de las recetas.
    - df_recetas (pandas.DataFrame): DataFrame que contiene las recetas,
    con una columna llamada 'ingredients' que contiene listas de ingredientes.

    Retorna:
    - pandas.DataFrame: Un nuevo DataFrame que contiene solo las recetas
    que cumplen con los criterios de filtrado.

    Ejemplo de uso:
    >>> ingredientes_deseados = ['pollo', 'cebolla']
    >>> ingredientes_excluir = ['azúcar', 'gluten']
    >>> df_recetas_filtrado = filtrar_ingredientes(
        ingredientes_deseados,
        ingredientes_excluir,
        df_recetas)
    """

    # Crear una máscara para los ingredientes deseados
    mask_deseados = np.array([
        any(
            ingrediente in ing
            for ing in x
            for ingrediente in ingredientes_deseados
        )
        if ingredientes_deseados else True
        for x in df_recetas['ingredients']
    ])

    # Crear una máscara para los ingredientes a excluir
    mask_excluir = np.array([
        all(
            ingrediente not in ing
            for ing in x
            for ingrediente in ingredientes_excluir
        )
        if ingredientes_excluir else True
        for x in df_recetas['ingredients']
    ])

    # Aplicar ambas máscaras y actualizar el DataFrame original
    df_recetas = df_recetas[mask_deseados & mask_excluir]

    return df_recetas


def home_page():
    """
    Despliega la página principal de la aplicación "Appetito".

    Esta función establece las funciones que deben implementarse para
    garantizar la correcta visualización de la página principal. Muestra el
    título "Appetito" y llama a la función 'recetas_normales()' para mostrar
    las recetas normales en la página principal.
    """
    st.title("Appetito")
    recetas_normales()


# Se muestran las recetas sin clasificacion alguna
def recetas_normales():
    """
    Muestra las recetas sin clasificación alguna en la interfaz de Streamlit.
    Permite al usuario filtrar las recetas por ingredientes, dificultad y
    subcategoría. Además, verifica si el usuario está loggeado para ofrecerle
    la opción de agregar recetas a favoritos.

    No retorna ningún valor. Muestra las recetas y opciones de filtrado en la
    interfaz de Streamlit.

    Detalles de la función:

    - Verifica si el usuario está loggeado; si no lo está, muestra un mensaje
    de bienvenida y motivación para registrarse o iniciar sesión.

    - Carga o recupera las recetas normales y las almacena en la sesión de
    Streamlit para ahorrar memoria en futuras consultas.

    - Permite al usuario filtrar las recetas por ingredientes deseados,
    ingredientes a excluir, dificultad y subcategoría.

    - Muestra las recetas filtradas en la interfaz de Streamlit, con opciones
    de paginación para navegar entre las recetas.

    - Cada receta se presenta con una imagen y ofrece la posibilidad de ver
    detalles adicionales mediante la función 'detalles_abiertos'.

    Ejemplo de uso:
    >>> recetas_normales()
    """
    # Verifica si el usuario está loggeado
    if (st.session_state['logged_in'] is False or
            st.session_state['logged_in'] is None):
        # Para motivar a el usuario a registrarse o iniciar sesión
        st.title("Welcome to Appetito To know many more recipes, " +
                 "log in or sign up!")

    if 'recetas_normales_json' not in st.session_state:
        # Ruta del archivo recetas saludables json
        json_recetas_normales = cargar_datos(ruta_normales)
        st.session_state['recetas_normales_json'] = json_recetas_normales
        df_recetas_normales = pd.DataFrame(json_recetas_normales)

        # Desde este punto se puede revisar si existe 'recetas_normales' en la
        # session_state, pero para evitar problemas se crea el objeto.

        # Se crea un objeto para almacenar las recetas
        print("no estaba la receta")
        obj_recetas_normales = {}
        for receta_n in json_recetas_normales:
            if receta_n["id"] not in obj_recetas_normales:
                obj_recetas_normales[receta_n["id"]] = receta_n
            else:
                print("Ya estaba la receta con id", receta_n["id"])
        st.session_state['recetas_normales'] = obj_recetas_normales

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = {}
        st.session_state['recetas'].update(obj_recetas_normales)
    else:
        df_recetas_normales = pd.DataFrame(
            st.session_state['recetas_normales_json']
        )

    if 'ingredientes' not in st.session_state:
        # Leer la lista de ingredientes
        lista_ingredientes = pd.read_json(ruta_ingredientes)
        lista_ingredientes = lista_ingredientes["ingredients"][0]
        st.session_state['ingredientes'] = lista_ingredientes
    else:
        lista_ingredientes = st.session_state['ingredientes']

    # Buscador de recetas
    buscador = st.text_input("Search for a recipe", "")

    with st.expander("Filters"):
        # Crear una caja de selección para el filtro de dificultad
        ingredientes_deseados = st.multiselect(
            "Select ingredients:", lista_ingredientes
        )

        # Seleccionar ingredientes a excluir
        ingredientes_excluir = st.multiselect(
            "Select ingredients to exclude:", lista_ingredientes
        )

        # Seleccionar dificultad de preparacion
        difficult = st.selectbox(
            'Select difficulty level',
            ['All', 'Easy', 'More effort', 'A challenge']
        )

        # Seleccionar subcategoria de recetas
        subcategory = st.selectbox(
            'Select subcategory',
            ['All', "Lunch recipes", "Dinner recipes", "Breakfast recipes",
             "Storecupboard", "Cheese recipes", "Desserts",
             "Fish and seafood", "Pasta", "Chicken", "Meat", "Vegetarian"
             ]
        )

    if buscador:
        df_recetas_normales = df_recetas_normales[
            df_recetas_normales['name'].str.contains(buscador, case=False)
        ]

    # Filtrar las recetas basándose en dificultad, subcategoría e ingredientes
    if ingredientes_deseados or ingredientes_excluir:
        df_recetas_normales = filtrar_ingredientes(
            ingredientes_deseados, ingredientes_excluir, df_recetas_normales
        )

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'All':
        df_recetas_normales = df_recetas_normales[
            df_recetas_normales['difficult'] == difficult
            ]

    # Filtrar las recetas basándose en la subcategoría
    if subcategory != 'All':
        df_recetas_normales = df_recetas_normales[
            df_recetas_normales['subcategory'] == subcategory
            ]

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_normales) // recetas_por_pagina
    if len(df_recetas_normales) % recetas_por_pagina > 0:
        total_paginas += 1

    # Verifica si hay páginas para mostrar
    if total_paginas > 0:
        # Crea un selector para la página
        pagina = st.selectbox('Select a page',
                              options=range(1, total_paginas + 1))

        # Filtra el DataFrame para obtener solo recetas de página seleccionada
        inicio = (pagina - 1) * recetas_por_pagina
        fin = inicio + recetas_por_pagina
        df_recetas_pagina = df_recetas_normales.iloc[inicio:fin]

        # Ahora puedes mostrar las recetas de df_recetas_pagina
        for _, receta in df_recetas_pagina.iterrows():
            st.markdown(
                f"""
                <div style="
                    border: 2px solid #ccc; padding: 5px; text-align: center;
                ">
                    <img src="{receta['image']}" alt="Imagen de la receta" 
                    style="max-width: 100%; border-radius: 5px;">
                </div>
                """,
                unsafe_allow_html=True,
            )
            detalles_abiertos(receta)
    else:
        st.title("No recipes to display.")


# Se muestran las recetas saludables
def recetas_saludables():
    """
    Muestra las recetas saludables en la interfaz de Streamlit. Permite al
    usuario filtrar las recetas por ingredientes, dificultad y subcategoría.

    No retorna ningún valor. Muestra las recetas y opciones de filtrado en la
    interfaz de Streamlit.

    Detalles de la función:

    - Carga las recetas saludables desde un archivo JSON y las almacena en la
    sesión de Streamlit para ahorrar memoria en futuras consultas.
    - Permite al usuario filtrar las recetas por ingredientes deseados,
    ingredientes a excluir, dificultad y subcategoría.
    - Muestra las recetas filtradas en la interfaz de Streamlit, con opciones
    de paginación para navegar entre las recetas.
    - Cada receta se presenta con una imagen y ofrece la posibilidad de ver
    detalles adicionales mediante la función 'detalles_abiertos'.

    Ejemplo de uso:
    >>> recetas_saludables()
    """
    # Se revisa si la respuesta del json esta en la sesion para ahorrar memoria
    if 'recetas_saludables_json' not in st.session_state:
        # Ruta del archivo recetas saludables json
        json_recetas_saludables = cargar_datos(ruta_saludable)
        st.session_state['recetas_saludables_json'] = json_recetas_saludables
        df_recetas_saludables = pd.DataFrame(json_recetas_saludables)

        # Se crea un objeto para almacenar las recetas
        print("no estaban las recetas saludables")
        obj_recetas_saludables = {}
        for receta_s in json_recetas_saludables:
            if receta_s["id"] not in obj_recetas_saludables:
                obj_recetas_saludables[receta_s["id"]] = receta_s
            else:
                print("Ya estaba la receta con id", receta_s["id"])
        st.session_state['recetas_saludables'] = obj_recetas_saludables

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = {}
        st.session_state['recetas'].update(obj_recetas_saludables)
    else:
        df_recetas_saludables = pd.DataFrame(
            st.session_state['recetas_saludables_json']
        )

    if 'ingredientes' not in st.session_state:
        # Leer la lista de ingredientes
        lista_ingredientes = pd.read_json(ruta_ingredientes)
        lista_ingredientes = lista_ingredientes["ingredients"][0]
        st.session_state['ingredientes'] = lista_ingredientes
    else:
        lista_ingredientes = st.session_state['ingredientes']

    # Aqui se despliegan las recetas saludables
    st.title("Healthy recipes")

    buscador = st.text_input("Search for a recipe", "")

    with st.expander("Filters"):
        # Crear una caja de selección para el filtro de dificultad
        ingredientes_deseados = st.multiselect(
            "Select ingredients:", lista_ingredientes
        )

        # Crear una caja de selección para el filtro de ingredientes a excluir
        ingredientes_excluir = st.multiselect(
            "Select ingredients to exclude:", lista_ingredientes
        )

        # Crear una caja de selección para el filtro de dificultad
        difficult = st.selectbox(
            'Select the difficulty level',
            ['All', 'Easy', 'More effort', 'A challenge']
        )
        subcategory = st.selectbox(
            'Select the subcategory',
            ['All', 'Smoothies', 'Salads',
             'Dinner', 'Fitness & lifestyle',
             'High protein', 'Keto'
             ]
        )
    # Buscador de recetas
    if buscador:
        df_recetas_saludables = df_recetas_saludables[
            df_recetas_saludables['name'].str.contains(buscador, case=False)
        ]

    # Filtrar las recetas basándose en dificultad, subcategoría e ingredientes
    if ingredientes_deseados or ingredientes_excluir:
        df_recetas_saludables = filtrar_ingredientes(
            ingredientes_deseados, ingredientes_excluir, df_recetas_saludables
        )

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'All':
        df_recetas_saludables = df_recetas_saludables[
            df_recetas_saludables['difficult'] == difficult]
    if subcategory != 'All':
        df_recetas_saludables = df_recetas_saludables[
            df_recetas_saludables['subcategory'] == subcategory]

    if df_recetas_saludables.empty:
        st.title("No healthy recipes available.")
        return None

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_saludables) // recetas_por_pagina
    if len(df_recetas_saludables) % recetas_por_pagina > 0:
        total_paginas += 1

    # Crea un selector para la página
    pagina = st.selectbox('Select a page', options=range(1, total_paginas + 1))

    # Filtra el DataFrame para obtener solo recetas de página seleccionada
    if pagina is not None:
        inicio = (pagina - 1) * recetas_por_pagina
        fin = inicio + recetas_por_pagina
        df_recetas_pagina = df_recetas_saludables.iloc[inicio:fin]

    for index, receta in df_recetas_pagina.iterrows():
        # Mostrar la imagen previa con borde
        st.markdown(
            f"""
            <div style="
                border: 2px solid #ccc; padding: 5px; text-align: center;
            ">
                <img src="{receta['image']}" alt="Imagen de la receta"
                  style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta)


# Se muestras las recetas para un corto presupuesto(sencillaes)
def recetas_presupuesto():
    """
    Muestra recetas simples en la interfaz de Streamlit, con opciones de
    filtrado por ingredientes, dificultad y subcategoría.

    No retorna ningún valor. Muestra las recetas y opciones de filtrado en la
    interfaz de Streamlit.

    Detalles de la función:

    - Carga o recupera las recetas de presupuesto y las almacena en la sesión
    de Streamlit para ahorrar memoria en futuras consultas.

    - Permite al usuario filtrar las recetas por ingredientes deseados,
    ingredientes a excluir, dificultad y subcategoría.

    - Muestra las recetas filtradas en la interfaz de Streamlit, con
    opciones de paginación para navegar entre las recetas.

    - Cada receta se presenta con una imagen y ofrece la posibilidad de ver
    detalles adicionales mediante la función 'detalles_abiertos'.

    Ejemplo de uso:
    >>> recetas_presupuesto()
    """
    if 'recetas_presupuesto_json' not in st.session_state:
        # Ruta del archivo recetas presupuesto json
        json_recetas_presupuesto = cargar_datos(ruta_presupuesto)
        st.session_state['recetas_presupuesto_json'] = json_recetas_presupuesto
        df_recetas_presupuesto = pd.DataFrame(json_recetas_presupuesto)

        # Se crea un objeto para almacenar las recetas
        print("no estaban las recetas presupuesto")
        obj_recetas_presupuesto = {}
        for receta_p in json_recetas_presupuesto:
            if receta_p["id"] not in obj_recetas_presupuesto:
                obj_recetas_presupuesto[receta_p["id"]] = receta_p
            else:
                print("Ya estaba la receta con id", receta_p["id"])
        st.session_state['recetas_presupuesto'] = obj_recetas_presupuesto

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = {}
        st.session_state['recetas'].update(obj_recetas_presupuesto)

    else:
        df_recetas_presupuesto = pd.DataFrame(
            st.session_state['recetas_presupuesto_json']
        )

    if 'ingredientes' not in st.session_state:
        # Leer la lista de ingredientes
        lista_ingredientes = pd.read_json(ruta_ingredientes)
        lista_ingredientes = lista_ingredientes["ingredients"][0]
        st.session_state['ingredientes'] = lista_ingredientes
    else:
        lista_ingredientes = st.session_state['ingredientes']

    # Aqui se despliegan las recetas sencillas
    st.title("Simple Recipes")

    buscador = st.text_input("Search for a recipe", "")

    with st.expander("Filters"):
        # Crear una caja de selección para el filtro de ingredientes deseados
        ingredientes_deseados = st.multiselect(
            "Select ingredients:", lista_ingredientes
        )

        # Crear una caja de seleccion par aingredientes a excluir
        ingredientes_excluir = st.multiselect(
            "Select ingredients to exclude:", lista_ingredientes
        )

        # Crear una caja de selección para el filtro de dificultad
        difficult = st.selectbox(
            'Select the difficulty level',
            ['All', 'Easy', 'More effort', 'A challenge']
        )
        subcategory = st.selectbox(
            'Select the subcategory',
            ['All', 'Budget dinners', 'Batch cooking',
             'Student meals', 'Freezable meals',
             'Slow cooker']
        )

    # Buscador de recetas
    if buscador:
        df_recetas_presupuesto = df_recetas_presupuesto[
            df_recetas_presupuesto['name'].str.contains(buscador, case=False)
        ]

    # Filtrar las recetas basándose en dificultad, subcategoría e ingredientes
    if ingredientes_deseados or ingredientes_excluir:
        df_recetas_presupuesto = filtrar_ingredientes(
            ingredientes_deseados, ingredientes_excluir, df_recetas_presupuesto
        )
    # Verifica si hay recetas para mostrar
    if df_recetas_presupuesto.empty:
        st.title("No simple recipes available.")
        return None

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'All':
        df_recetas_presupuesto = df_recetas_presupuesto[
            df_recetas_presupuesto['difficult'] == difficult]
    if subcategory != 'All':
        df_recetas_presupuesto = df_recetas_presupuesto[
            df_recetas_presupuesto['subcategory'] == subcategory]

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_presupuesto) // recetas_por_pagina
    if len(df_recetas_presupuesto) % recetas_por_pagina > 0:
        total_paginas += 1

    # Crea un selector para la página
    pagina = st.selectbox('Select a page', options=range(1, total_paginas + 1))

    # Filtra el DataFrame para obtener solo recetas de la página seleccionada
    inicio = (pagina - 1) * recetas_por_pagina
    fin = inicio + recetas_por_pagina
    df_recetas_pagina = df_recetas_presupuesto.iloc[inicio:fin]

    for index, receta1 in df_recetas_pagina.iterrows():
        st.markdown(
            f"""
            <div style="
                border: 2px solid #ccc; padding: 5px; text-align: center;
            ">
                <img src="{receta1['image']}" alt="Imagen de la receta"
                style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta1)


# Se muestran las recetas para hornearse
def recetas_horneados():
    """
    Muestra recetas horneadas en la interfaz de Streamlit, con opciones de
    filtrado por ingredientes, dificultad y subcategoría.

    No retorna ningún valor. Muestra las recetas y opciones de filtrado en
    la interfaz de Streamlit.

    Detalles de la función:

    - Carga o recupera las recetas horneadas y las almacena en la sesión de
    Streamlit para ahorrar memoria en futuras consultas.
    - Permite al usuario filtrar las recetas por ingredientes deseados,
    ingredientes a excluir, dificultad y subcategoría.

    - Muestra las recetas filtradas en la interfaz de Streamlit, con opciones
    de paginación para navegar entre las recetas.

    - Cada receta se presenta con una imagen y ofrece la posibilidad de ver
    detalles adicionales mediante la función 'detalles_abiertos'.

    Ejemplo de uso:
    >>> recetas_horneados()
    """
    if 'recetas_horneados_json' not in st.session_state:
        # Ruta del archivo recetas presupuesto json
        json_recetas_horneados = cargar_datos(ruta_horneados)
        st.session_state['recetas_horneados_json'] = json_recetas_horneados
        df_recetas_horneados = pd.DataFrame(json_recetas_horneados)

        # Se crea un objeto para almacenar las recetas
        print("no estaban las recetas horneadas")
        obj_recetas_horneados = {}
        for receta_horneado in json_recetas_horneados:
            if receta_horneado["id"] not in obj_recetas_horneados:
                obj_recetas_horneados[receta_horneado["id"]] = receta_horneado
            else:
                print("Ya estaba la receta con id", receta_horneado["id"])
        st.session_state['recetas_horneados'] = obj_recetas_horneados

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = {}
        st.session_state['recetas'].update(obj_recetas_horneados)
    else:
        df_recetas_horneados = pd.DataFrame(
            st.session_state['recetas_horneados_json']
        )

    if 'ingredientes' not in st.session_state:
        # Leer la lista de ingredientes
        lista_ingredientes = pd.read_json(ruta_ingredientes)
        lista_ingredientes = lista_ingredientes["ingredients"][0]
        st.session_state['ingredientes'] = lista_ingredientes
    else:
        lista_ingredientes = st.session_state['ingredientes']

    # Display baked recipes here
    st.title("Baked Recipes")

    buscador = st.text_input("Search for a recipe", "")

    with st.expander("Filters"):
        # Crear una caja de selección para el filtro de ingredientes deseados
        ingredientes_deseados = st.multiselect(
            "Select ingredients:", lista_ingredientes
        )

        # Crear una caja de selección para seleccionar ingredientes a excluir
        ingredientes_excluir = st.multiselect(
            "Select ingredients to exclude:", lista_ingredientes
        )

        # Crear una caja de selección para el filtro de dificultad
        difficult = st.selectbox(
            'Select the difficulty level',
            ['All', 'Easy', 'More effort', 'A challenge']
        )
        subcategory = st.selectbox(
            'Select the subcategory',
            ['All', 'Bread', 'Cakes', 'Desserts', "Kids' baking",
             'Quick bakes', 'Savoury pastries', 'Sweet treats', 'Vegan baking',
             'Biscuit recipes']
        )

    # Buscador de recetas
    if buscador:
        df_recetas_horneados = df_recetas_horneados[
            df_recetas_horneados['name'].str.contains(buscador, case=False)
        ]

    # Filtrar las recetas basándose en dificultad, subcategoría e ingredientes
    if ingredientes_deseados or ingredientes_excluir:
        df_recetas_horneados = df_recetas_horneados[
            df_recetas_horneados['ingredients'].apply(
                lambda x: any(
                    ingrediente in ing for ing in x for ingrediente in
                    ingredientes_deseados)
            )
        ]

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'All':
        df_recetas_horneados = df_recetas_horneados[
            df_recetas_horneados['difficult'] == difficult]
    if subcategory != 'All':
        df_recetas_horneados = df_recetas_horneados[
            df_recetas_horneados['subcategory'] == subcategory]

    if df_recetas_horneados.empty:
        st.title("No baked recipes available.")
        return None

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_horneados) // recetas_por_pagina
    if len(df_recetas_horneados) % recetas_por_pagina > 0:
        total_paginas += 1

    # Crea un selector para la página
    pagina = st.selectbox('Select a page', options=range(1, total_paginas + 1))

    # Filtra el DataFrame para obtener solo lo seleccionado
    inicio = (pagina - 1) * recetas_por_pagina
    fin = inicio + recetas_por_pagina
    df_recetas_pagina = df_recetas_horneados.iloc[inicio:fin]

    for index, receta2 in df_recetas_pagina.iterrows():
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc;
            padding: 5px; text-align: center;">
            <img src="{receta2['image']}" alt="Imagen de la receta"
            style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta2)


# Se muestran las recetas para ocasiones especiales
def recetas_especiales():
    """
    Muestra recetas especiales en la interfaz de Streamlit, con
    opciones de filtrado por ingredientes, dificultad y subcategoría.

    No retorna ningún valor. Muestra las recetas y opciones de
    filtrado en la interfaz de Streamlit.

    Detalles de la función:

    - Carga o recupera las recetas especiales y las almacena en la
    sesión de Streamlit para ahorrar memoria en futuras consultas.

    - Permite al usuario filtrar las recetas por ingredientes deseados,
    ingredientes a excluir, dificultad y subcategoría.

    - Muestra las recetas filtradas en la interfaz de Streamlit,
    con opciones de paginación para navegar entre las recetas.

    - Cada receta se presenta con una imagen y ofrece la posibilidad
    de ver detalles adicionales mediante la función 'detalles_abiertos'.

    Ejemplo de uso:
    >>> recetas_especiales()
    """
    if 'recetas_especiales_json' not in st.session_state:
        # Ruta del archivo recetas presupuesto json
        json_recetas_especiales = cargar_datos(ruta_especiales)
        st.session_state['recetas_especiales_json'] = json_recetas_especiales
        df_recetas_especiales = pd.DataFrame(json_recetas_especiales)
        # Se crea un objeto para almacenar las recetas
        print("no estaban las recetas especiales")
        obj_recetas_especiales = {}
        for receta_e in json_recetas_especiales:
            if receta_e["id"] not in obj_recetas_especiales:
                obj_recetas_especiales[receta_e["id"]] = receta_e
            else:
                print("Ya estaba la receta con id", receta_e["id"])
        st.session_state['recetas_horneados'] = obj_recetas_especiales

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = {}
        st.session_state['recetas'].update(obj_recetas_especiales)

    else:
        df_recetas_especiales = pd.DataFrame(
            st.session_state['recetas_especiales_json']
        )

    if 'ingredientes' not in st.session_state:
        # Leer la lista de ingredientes
        lista_ingredientes = pd.read_json(ruta_ingredientes)
        lista_ingredientes = lista_ingredientes["ingredients"][0]
        st.session_state['ingredientes'] = lista_ingredientes
    else:
        lista_ingredientes = st.session_state['ingredientes']

    st.title("Special Recipes")

    buscador = st.text_input("Search for a recipe", "")

    if df_recetas_especiales.empty:
        st.title("No special recipes available.")
        return None

    with st.expander("Filters"):
        # Crear una caja de selección para el filtro de ingredientes deseados
        ingredientes_deseados = st.multiselect(
            "Select ingredients:", lista_ingredientes
        )

        # Crear una caja de selección para seleccionar ingredientes a excluir
        ingredientes_excluir = st.multiselect(
            "Select ingredients to exclude:", lista_ingredientes
        )

        # Crear una caja de selección para el filtro de dificultad
        difficult = st.selectbox(
            'Select difficulty level',
            ['All', 'Easy', 'More effort', 'A challenge']
        )
        subcategory = st.selectbox(
            'Select subcategory',
            ['All', 'Birthdays', 'Cocktails', 'Hosting', 'Slow cooker',
             "Kids' birthdays", "Mocktails", 'Picnics', 'Barbecues',
             'Spring recipes', 'Special occasions', 'Teas']
        )

    # Buscador de recetas
    if buscador:
        df_recetas_especiales = df_recetas_especiales[
            df_recetas_especiales['name'].str.contains(buscador, case=False)
        ]

    # Filtrar las recetas con dificultad, subcategoría e ingredientes
    if ingredientes_deseados or ingredientes_excluir:
        df_recetas_especiales = filtrar_ingredientes(
            ingredientes_deseados, ingredientes_excluir, df_recetas_especiales
        )

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'All':
        df_recetas_especiales = df_recetas_especiales[
            df_recetas_especiales['difficult'] == difficult]
    if subcategory != 'All':
        df_recetas_especiales = df_recetas_especiales[
            df_recetas_especiales['subcategory'] == subcategory]

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_especiales) // recetas_por_pagina
    if len(df_recetas_especiales) % recetas_por_pagina > 0:
        total_paginas += 1

    # Crea un selector para la página
    pagina = st.selectbox('Selecciona una página',
                          options=range(1, total_paginas + 1))

    # Filtra el DataFrame para obtener solo lo seleccionado
    inicio = (pagina - 1) * recetas_por_pagina
    fin = inicio + recetas_por_pagina
    df_recetas_pagina = df_recetas_especiales.iloc[inicio:fin]

    for index, receta1 in df_recetas_pagina.iterrows():
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding:
            5px; text-align: center;">
            <img src="{receta1['image']}" alt="Imagen de la receta"
            style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta1)


def detalles_cuenta():
    st.title('Account details')

    # se intenta con st.data_edit pero se prefiere el html markdown
    cuenta_aux = st.session_state.cuenta

    try:
        st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/'
                    'dist/css/bootstrap.min.css" rel="stylesheet" integrity="s'
                    'ha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dw'
                    'wykc2MPK8M2HN" crossorigin="anonymous">'
                    '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2'
                    '/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6Rzs'
                    'ynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cD'
                    'fL" crossorigin="anonymous"></script>',
                    unsafe_allow_html=True
                    )
    except Exception as e:
        print("Error installing Bootstrap." + str(e))

    tabla_html = """
        <table class="table table-dark table-striped-columns">
            <tbody>
                <tr>
                    <th scope="row">username</th>
                    <td id='username'>
                        """ + cuenta_aux['username'] + """
                    </th>
                </tr>
    """

    for atributo_cuenta in cuenta_aux:
        if atributo_cuenta in ['username', 'key']:
            continue
        elif atributo_cuenta == 'password':
            tabla_html += """<tr>
                <th scope='row'>""" + atributo_cuenta + """</th>
                <td> ***** </td>
            </tr>
            """
        else:
            tabla_html += """<tr>
                <th scope='row'>""" + atributo_cuenta + """</th>
                <td>""" + str(cuenta_aux[atributo_cuenta]) + """</td>
            </tr>
            """

    tabla_html += "</tbody></table>"

    st.markdown(tabla_html, unsafe_allow_html=True)

    if st.button(
            'Edit account',
            type='primary',
            disabled=True,
            help='Not ready yet'):
        print('edit')
