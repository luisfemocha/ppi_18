# CAPA CONTROL

import json
import requests

import pandas as pd
import streamlit as st

import utils


# Para menor uso de memoria se limita la app en la fase de desarrollo
limite_recetas = 10

# se ajustan los datos para utilizarlos en las funciones
def cargar_recetas(ruta):
    try:
        if ruta.find("raw") > -1:
            response = requests.get(ruta)
        # Confirmar que el request de un resultado exitoso.
            if response.status_code == 200:
        # Usa .json() para archivos JSON, .text para archivos de texto, etc.
                return pd.DataFrame(response.json()) 
            else:
                st.title("Error al leer la url.")
        else:
            with open(ruta, encoding='utf8') as contenido:
                return pd.DataFrame(json.load(contenido))
    except:
        st.title("Error al leer el archivo "+ruta)
        return pd.DataFrame()


# Aqui se despliega el login y el registro de la pagina
def desplegar_form(option):
    # Este es para el registro de la pagina
    if option == 'registro':
        with st.form(key='registration_form'):
            st.header("Registro")
            username = st.text_input('Nombre de usuario')
            password = st.text_input('Contraseña', type='password')
            confirm_password = st.text_input('Confirmar contraseña', type='password')
            register_button = st.form_submit_button('Registrarse')

            # Para llamar a la funcion de registro
            if register_button:
                utils.registro(username, password, confirm_password)

    # Este es para el login de la pagina
    elif option == 'ingreso':
        # with st.form(key='login_form'):
        st.header('Inicio de Sesión')
        username = st.text_input('Nombre de usuario')
        password = st.text_input('Contraseña', type='password')
        login_button = st.button("Iniciar sesión")
        #st.form_submit_button('Iniciar Sesión')

        # Para llamar a la funcion de login
        if login_button:
            st.title("se comienza")
            utils.ingreso(username, password)


# Visualizacion de cada receta
def detalles_abiertos(receta):
    # Verifica si se debe mostrar los detalles de esta receta
    # if receta['id'] in detalles_abiertos and detalles_abiertos[receta['id']]:
    with st.expander(f"Ver Detalles de {receta['name']}"):
        st.subheader(receta["name"])

        # Detalles de la receta (puedes usar un bucle para iterar sobre los datos)
        st.header("Detalles de la Receta")
        st.write(f"**Descripción:** {receta['description']}")
        st.write(f"**Autor:** {receta['author']}")
        st.write(f"**Calificación:** {receta['rattings']}")

        # Ingredientes
        st.header("Ingredientes")
        for i, ingrediente in enumerate(receta["ingredients"]):
            st.write(f"{i + 1}. {ingrediente}")

        # Pasos
        st.header("Pasos")
        for i, paso in enumerate(receta["steps"]):
            st.write(f"{i + 1}. {paso}")

        # Tiempos
        st.header("Tiempos")
        preparacion = receta['times'].get('Preparation', 'No Time')
        cocina = receta['times'].get('Cooking', 'No Time')
        st.write(f"**Preparación:** {preparacion}")
        st.write(f"**Cocción:** {cocina}")

        # Otros detalles
        st.header("Otros Detalles")
        st.write(f"**Porciones:** {receta['serves']}")
        st.write(f"**Dificultad:** {receta['difficult']}")
        st.write(f"**Conteo de votos:** {receta['vote_count']}")
        st.write(f"**Subcategoría:** {receta['subcategory']}")
        st.write(f"**Tipo de platillo:** {receta['dish_type']}")
        st.write(f"**Categoría principal:** {receta['maincategory']}")

# Segun esta funcion se cambian de vistas
def vistas(vista):
    """
    esta Funcion es para cambiar las vistas de la pagina 
    segun el sidebar y la opcion que escoga el usario
    """
    if vista == 'principal':
        pagina_principal()
    elif vista =='saludable':
        recetas_saludables()
    elif vista == 'presupuesto':
        recetas_presupuesto()
    elif vista == 'horneado':
        recetas_horneados()
    elif vista == 'especiales':
        recetas_especiales() 
    elif vista == 'registro':
        desplegar_form('registro')
    elif vista == 'ingreso':
        desplegar_form('ingreso')

# Aqui se mira la pagina principal
def pagina_principal():
    st.title("Appetito") 
    st.text("Daniel")
    st.text("Luis")
    recetas_normales()

#Se muestran las erecetas sin clasificacion alguna
def recetas_normales():
    # Ruta del archivo recetas saludables json temporal para usar en consola local
    ruta_normales = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/src/datos/recipes.json'
    df_recetas_normales = cargar_recetas(ruta_normales)
    lista_ingredientes = "" 
    lista_ingredientes.insert(0,'Todos')
    
    # Crear una caja de selección para el filtro de dificultad
    ingredientes_deseados = st.multiselect("Selecciona los ingredientes:", lista_ingredientes)
    difficult = st.selectbox('Selecciona el nivel de dificultad', ['Todos', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Selecciona la subcategoría', ['Todos', 'Smoothies', 'Salads', 'Dinner', 'Fitness & lifestyle', 'High protein', 'Keto'])

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if ingredientes_deseados:
        df_recetas_normales = df_recetas_normales[df_recetas_normales['ingredients'].apply(lambda x: any(ingrediente in ing for ing in x for ingrediente in ingredientes_deseados))]
    if difficult != 'Todos':
        df_recetas_normales = df_recetas_normales[df_recetas_normales['difficult'] == difficult]
    if subcategory != 'Todos':
        df_recetas_normales = df_recetas_normales[df_recetas_normales['subcategory'] == subcategory]

    if df_recetas_normales.empty:
        st.title("No hay recetas saludables disponibles.")
        return None

    if limite_recetas:
        aux_limite = limite_recetas
    else:
        aux_limite = len(df_recetas_normales)

    for index, receta in df_recetas_normales.iterrows():

        if aux_limite > 0:
            aux_limite -= 1
        else:
            break

        # Mostrar la imagen previa con borde
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta['image']}" alt="Imagen de la receta" style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta)

# Se muestran las recetas saludables
def recetas_saludables():
    # Ruta del archivo recetas saludables json temporal para usar en consola local
    ruta_saludable = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/src/datos/saludables.json'
    df_recetas_saludables = cargar_recetas(ruta_saludable)

    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Selecciona el nivel de dificultad', ['Todos', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Selecciona la subcategoría', ['Todos', 'Smoothies', 'Salads', 'Dinner', 'Fitness & lifestyle', 'High protein', 'Keto'])

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'Todos':
        df_recetas_saludables = df_recetas_saludables[df_recetas_saludables['difficult'] == difficult]
    if subcategory != 'Todos':
        df_recetas_saludables = df_recetas_saludables[df_recetas_saludables['subcategory'] == subcategory]

    if df_recetas_saludables.empty:
        st.title("No hay recetas saludables disponibles.")
        return None

    # Aqui se despliegan las recetas saludables
    st.title("Recetas saludables")

    if limite_recetas:
        aux_limite = limite_recetas
    else:
        aux_limite = len(df_recetas_saludables)

    for index, receta in df_recetas_saludables.iterrows():

        if aux_limite > 0:
            aux_limite -= 1
        else:
            break

        # Mostrar la imagen previa con borde
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta['image']}" alt="Imagen de la receta" style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Crear un elemento expansible con los detalles de la receta
        # with st.expander(f"Ver Detalles de {receta['name']}"):
        #     # Cuando se hace clic en el botón, actualiza la variable de estado
        #     if st.button(f"Ver Detalles de {receta['name']}"):
        #         detalles_abiertos = receta['id']

        #     # Llama a la función para mostrar los detalles
        detalles_abiertos(receta)

# Se muestras las recetas para un corto presupuesto(sencillaes)
def recetas_presupuesto():
    # Ruta del archivo recetas presupuesto json 
    ruta_presupuesto = "https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/src/datos/presupuesto.json"
    df_recetas_presupuesto = cargar_recetas(ruta_presupuesto)

    if df_recetas_presupuesto.empty:
        st.title("No hay recetas sencillas disponibles")
        return None

    st.title("Recetas sencillas")

    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Selecciona el nivel de dificultad', ['Todos', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Selecciona la subcategoría', ['Todos', 'Budget dinners', 'Batch cooking', 'Student meals', 'Freezable meals', 'Slow cooker'])

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'Todos':
        df_recetas_presupuesto = df_recetas_presupuesto[df_recetas_presupuesto['difficult'] == difficult]
    if subcategory != 'Todos':
        df_recetas_presupuesto = df_recetas_presupuesto[df_recetas_presupuesto['subcategory'] == subcategory]

    for index, receta1 in df_recetas_presupuesto.iterrows():
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta1['image']}" alt="Imagen de la receta" style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta1)

# Se muestran las recetas para hornearse
def recetas_horneados():
    # Ruta del archivo recetas presupuesto json 
    ruta_horneados = 'https://raw.githubusercontent.com/Dgarzonac9/pruebappi/main/horneados.json?token=GHSAT0AAAAAACHURJUBCDFFSXUDK75IVUYUZJ6VNOA'
    df_recetas_horneados = cargar_recetas(ruta_horneados)

    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Selecciona el nivel de dificultad', ['Todos', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Selecciona la subcategoría', ['Todos', 'Bread', 'Cakes', 'Desserts', "Kids' baking", 'Quick bakes','Savoury pastries','Sweet treats','Vegan baking','Biscuit recipes'])

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'Todos':
        df_recetas_horneados = df_recetas_horneados[df_recetas_horneados['difficult'] == difficult]
    if subcategory != 'Todos':
        df_recetas_horneados = df_recetas_horneados[df_recetas_horneados['subcategory'] == subcategory]

    if df_recetas_horneados.empty:
        st.title("No hay recetas horneadas disponibles.")
        return None

    # Aqui se despliegan las recetas de presupuesto
    st.title("Recetas horneadas")
    for index, receta2 in df_recetas_horneados.iterrows():
        # Aqui van a ir las recetas de presupuesto
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta2['image']}" alt="Imagen de la receta" style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta2)

# Se muestran las recetas para ocasiones especiales
def recetas_especiales():
    # Ruta del archivo recetas presupuesto json 
    ruta_especiales = "https://raw.githubusercontent.com/Dgarzonac9/pruebappi/main/horneados.json?token=GHSAT0AAAAAACHURJUBCDFFSXUDK75IVUYUZJ6VNOA"
    df_recetas_especiales = cargar_recetas(ruta_especiales)

    if df_recetas_especiales.empty:
        st.title("No  hay recetas especiales disponibles.")
        return None

    st.title("Recetas especiales")

    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Selecciona el nivel de dificultad', ['Todos', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Selecciona la subcategoría', ['Todos', 'Birthdays', 'Cocktails', 'Hosting', 'Slow cooker',"Kids' birthdays","Mocktails",'Picnics','Barbecues','Spring recipes','Special occasions','Teas'])

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'Todos':
        df_recetas_especiales = df_recetas_especiales[df_recetas_especiales['difficult'] == difficult]
    if subcategory != 'Todos':
        df_recetas_especiales = df_recetas_especiales[df_recetas_especiales['subcategory'] == subcategory]

    for index, receta1 in df_recetas_especiales.iterrows():
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta1['image']}" alt="Imagen de la receta" style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta1)