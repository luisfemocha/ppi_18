# Aqui estan funciones de la pagina para cambio de recetas

# Bibliotecas estándar
from datetime import datetime
from time import sleep
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


def obtener_datos_github(usuario):
    """
    Obtiene datos del perfil de GitHub de un usuario dado.

    Parámetros:
    - usuario (str): Nombre de usuario de GitHub.

    Retorna:
    - dict: Un diccionario que contiene datos del perfil de GitHub del usuario,
    incluyendo detalles como la URL del perfil, el nombre, la biografía y la
    URL del avatar.
    - None: Si no se puede obtener la información del perfil de GitHub.

    Dependencias:
    - La función utiliza la biblioteca 'requests' para realizar solicitudes
    HTTP a la API de GitHub.

    Ejemplo de uso:
    ```
    usuario = "ejemplo_usuario"
    datos_usuario = obtener_datos_github(usuario)
    if datos_usuario:
        print(f"Nombre: {datos_usuario['name']}")
        print(f"Bio: {datos_usuario['bio']}")
    else:
        print("No se pudo obtener la información del perfil de GitHub.")
    ```
    """
    url = f"https://api.github.com/users/{usuario}"
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        return response.json()
    else:
        # En caso de error en la solicitud, retorna None
        return None

      
def obtener_datos_github(usuario):
    """
    Obtiene datos del perfil de GitHub de un usuario dado.
    Parámetros:
    - usuario (str): Nombre de usuario de GitHub.
    Retorna:
    - dict: Un diccionario que contiene datos del perfil de GitHub del usuario,
     incluyendo detalles como la URL del perfil,
            el nombre, la biografía y la URL del avatar.
    - None: Si no se puede obtener la información del perfil de GitHub.
    Dependencias:
    - La función utiliza la biblioteca 'requests' para realizar solicitudes
    HTTP a la API de GitHub.
    Ejemplo de uso:
    ```
    usuario = "ejemplo_usuario"
    datos_usuario = obtener_datos_github(usuario)
    if datos_usuario:
        print(f"Nombre: {datos_usuario['name']}")
        print(f"Bio: {datos_usuario['bio']}")
    else:
        print("No se pudo obtener la información del perfil de GitHub.")
    ```
    """
    url = f"https://api.github.com/users/{usuario}"
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        return response.json()
    else:
        # En caso de error en la solicitud, retorna None
        return None


def contact_us():
    # Verifica si la solicitud fue exitosa (código 200) antes de intentar
    # obtener los datos
    """
    Renderiza una sección de Contacto en una aplicación web utilizando
    Streamlit.
    Esta función muestra información de contacto y perfiles de GitHub de
    dos desarrolladores.
    Componentes:
    - Título: Muestra el título de la sección como "Contáctanos".
    - Información de Contacto: Informa a los usuarios que pueden contactar al
    equipo mediante direcciones de correo electrónico especificadas.
    - Información del Desarrollador:
        - Obtiene y muestra la información del perfil de GitHub del primer
        desarrollador (Dgarzonac9).
        - Obtiene y muestra la información del perfil de GitHub del segundo
        desarrollador (Luisfemocha).
    Dependencias:
    - La función depende de la función externa `obtener_datos_github` para
    obtener datos del perfil de GitHub.
    Uso:
    - Integra esta función en una aplicación web de Streamlit para mostrar
    detalles de contacto y perfiles de desarrolladores.
    Retorna:
    - La sección de la aplicación web de Streamlit con la información
    de contacto y desarrolladores.
    """
    st.title("Contact us")
    st.write("You can contact us at the following email addresses:")

    st.write()

    # Datos para primer desarrollador
    user1 = "Dgarzonac9"
    user1_data = obtener_datos_github(user1)
    st.write(f"GitHub Profile 1: {user1_data['html_url']}")
    st.write(f"Name: {user1_data['name']}")
    st.write(f"Bio: {user1_data['bio']}")
    st.image(user1_data['avatar_url'],
             caption=f"{user1_data['name']}'s Avatar",
             width=300)

    # Datos para segundo desarrollador
    user2 = "Luisfemocha"
    user2_data = obtener_datos_github(user2)
    st.write(f"GitHub Profile 2: {user2_data['html_url']}")
    st.write(f"Name: {user2_data['name']}")
    st.write(f"Bio: {user2_data['bio']}")
    st.image(user2_data['avatar_url'],
             caption=f"{user2_data['name']}'s Avatar",
             width=300)


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
    # print('entra a set_recetas()', categoria, forzar)
    rutas = get_rutas()

    def set_receta(categoria, forzar):
        nom_cat = 'recetas_' + categoria
        if nom_cat not in st.session_state or \
                nom_cat + "_json" not in st.session_state or forzar:
            # print('se actualiza', cat)
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
                    # print('se actualiza ingredientes')

                else:
                    print('no se actualiza ingredientes')

                continue

            else:
                st.session_state["recetas"].update(set_receta(cat, forzar))

    else:
        try:
            if int(categoria) in id_rutas:
                categoria = id_rutas[int(categoria)]
            # else:
            #    print('categoria no esta en id_rutas:', categoria)

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

        if st.session_state['logged_in']:
            if recipe["id"] in st.session_state.cuenta['favorites']:
                btn_fvrt = st.button(
                    "Remove recipe from favorites",
                    key='unfav-'+recipe['id']
                )

                if btn_fvrt:
                    print('se elimina la receta de favoritas', recipe['id'])
                    st.session_state.cuenta['favorites'].remove(recipe["id"])
                    del st.session_state.favoritas[recipe["id"]]
                    conexion.actualizar_usuario(st.session_state.cuenta)
                    st.write('Receipt removed from favorites.')
                    st.rerun()

            else:
                btn_fvrt = st.button(
                    "Add recipe to favorites",
                    key='fav-'+recipe['id']
                )
                if btn_fvrt:
                    print('Se agrega a favoritas la receta', recipe['id'])
                    # print(recipe)
                    # print(recipe["id"])

                    try:
                        print("se intenta encontrar la receta con el id")

                        # print(
                        #     st.session_state['recetas'][recipe["id"]])

                        if 'favoritas' not in st.session_state:
                            st.session_state['favoritas'] = {}
                        st.session_state.favoritas[recipe["id"]] = recipe
                        st.session_state.cuenta['favorites'].append(
                            recipe["id"]
                        )

                        conexion.actualizar_usuario(st.session_state.cuenta)
                        st.write('Done, receipt added as favorite')
                        st.rerun()

                    except Exception as e:
                        print("error a la hora de agregar favorita", e)
                        st.write('Error, talk to an admin.', datetime.now())

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
        
        comentarios = conexion.get_comentarios(id_receta)

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
                # Verifica si el comentario no está vacío
                if nuevo_comentario:
                    try:
                        # Lógica para guardar el nuevo comentario en la
                        # base de datos
                        conexion.insertar_comentario(
                            usuario, id_receta, nuevo_comentario
                        )
                        st.success("Comment added successfully")
                        st.rerun()
                        nuevo_comentario = ""

                    except Exception as e:
                        st.error(f"Error adding comment: {e}")
                else:
                    st.warning("Please write a comment before submitting.")


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
        return home_page()
    elif vista == 'saludable':
        return recetas_saludables()
    elif vista == 'presupuesto':
        return recetas_presupuesto()
    elif vista == 'horneado':
        return recetas_horneados()
    elif vista == 'especiales':
        return recetas_especiales()
    elif vista == 'contact_us':
        return contact_us()
    elif vista == 'signup':
        return conexion.sign_up()
    elif vista == 'login':
        return conexion.log_in()
    elif vista == 'favorites':
        return conexion.recetas_favoritas()
    elif vista == 'account':
        return detalles_cuenta()
    elif vista == 'edit_account':
        return detalles_cuenta(True)
    elif vista == 'change_password':
        return change_password()
    else:
        print("Error en funcion vistas. Caso no apreciado " + vista)
        return False


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
        # print("no estaba la receta")
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
        # print("no estaban las recetas saludables")
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
        # print("no estaban las recetas presupuesto")
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
        # print("no estaban las recetas horneadas")
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
        # print("no estaban las recetas especiales")
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


def detalles_cuenta(edit=False):
    cuenta_aux = conexion.refresh_active_user(st.session_state.cuenta['key'])

    # print(cuenta_aux)
    if edit:
        st.title('Edit account')
    else:
        st.title('Account details')

    try:
        # En el siguiente markdown se importa el css y js de Bootstrap
        st.markdown(
            '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css'
            '/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous"'
            'integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXE'
            'V/Dwwykc2MPK8M2HN">'

            '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js'
            '/bootstrap.bundle.min.js" crossorigin="anonymous"'
            'integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/'
            'o0jlpcV8Qyq46cDfL"></script>',
            unsafe_allow_html=True
        )

    except Exception as e:
        print("Error installing Bootstrap." + str(e))

    # se guardan las clases que se le agregaran a cada fila y columna
    row_class = 'row border border-secondary'
    col_class = 'col text-end border-end border-secondary'

    if not edit:
        tabla_html = f"""
            <div id='account_father' class='container'>
                <div class='{row_class} rounded-top'>
                    <div class='{col_class}'>username</div>
                    <div class='col'>{cuenta_aux['username']}</div>
                </div>
        """
    else:
        edit_values = {}

        edit_values['username'] = st.text_input(
            'Username',
            placeholder=cuenta_aux['username'],
            disabled=True,
            help="Can't change your username, only an admin can."
        )

    for atributo_cuenta in cuenta_aux:
        aux_valor = cuenta_aux[atributo_cuenta]
        if edit:
            tipo = 'default'
            disabled = False
            help = "Leave it blank if you don't want to change it."

        if atributo_cuenta in ['username', 'key']:
            continue

        elif atributo_cuenta == 'password':
            # si el atributo es la contrasenia la censura
            aux_valor = "*****"
            if edit:
                tipo = 'password'

        elif atributo_cuenta == 'favorites':
            # si el atributo es favoritos, en la base de datos se guardan los
            # id de las recetas, pero al usuario se le muestra el nombre
            aux_favorito = []
            for a in cuenta_aux[atributo_cuenta]:
                try:
                    aux_favorito.append(st.session_state['recetas'][a]['name'])
                except Exception as e:
                    print('No se encontro la receta', e)
                    # print(st.session_state['recetas'])

            aux_valor = aux_favorito

            if edit:
                disabled = True
                help = "Can't change favorites list from here."

        if edit:
            edit_values[atributo_cuenta] = st.text_input(
                atributo_cuenta,
                type=tipo, placeholder=aux_valor, disabled=disabled, help=help
            )
        else:
            tabla_html += f"""<div class='{row_class}'>
                    <div class='{col_class}'>{atributo_cuenta}</div>
                    <div class='col'>{str(aux_valor)}</div>
                </div>
            """

    if edit:
        if st.button('Edit'):
            st.write("You have 10 seconds to regret that.")
            new_values = {'key': st.session_state.cuenta['key']}
            for valor in edit_values:
                if edit_values[valor] is not None and edit_values[valor] != '':
                    if (valor == 'email' and
                            not conexion.es_correo_valido(edit_values[valor])):
                        st.error("Please enter a valid email")
                        continue
                    new_values[valor] = edit_values[valor]
                    st.write(valor + " -> " + edit_values[valor])

            if len(new_values) > 1:
                if st.button("CANCEL CHANGES"):
                    st.write('No changes made')
                    print('Changes canceled.')
                    st.rerun()

                sleep(10)

                print('Se hace el cambio')
                print(conexion.actualizar_usuario(new_values))
                st.session_state.page = 'account'
                st.rerun()
            else:
                st.write("No changes made")

        if st.button("Restore changes"):
            st.session_state.page = 'account'
            st.rerun()

    else:
        tabla_html += "</div><br>"

        try:
            st.markdown(tabla_html, unsafe_allow_html=True)
        except Exception as e:
            st.write("Error while showing attributes")
            print('No se pudieron mostrar los atributos del usuario', e)

        if st.button(
                'Edit account',
                help='Click to change your attributes'
        ):
            st.session_state.page = 'edit_account'
            st.rerun()
            return True


def change_password():
    st.title("Forgot my password")
    st.write("You can write a new password. Please confirm it.")

    user = st.session_state['user_change_pass']
    password = st.text_input(
        "Password",
        type='password',
        key='pass360'
    )
    password2 = st.text_input(
        "Confirm password",
        type='password',
        key='conf_pass365'
    )
    if st.button("Change", key='btn367'):
        if password == password2:
            if user['password'] == password:
                st.write(
                    "Password not changed, is the "
                    "same as the old one.")
            else:
                new_user = {
                    'key': user['key'],
                    'password': password
                }
                print("Respuesta al olvide contrasena")
                print(conexion.actualizar_usuario(new_user))
                st.write("Password successfully changed")
        else:
            st.error("Password must match.")
