# CONTROL TIER

import json
import requests

import pandas as pd
import streamlit as st

import utils


# Para menor uso de memoria se limita la app en la fase de desarrollo
limite_recetas = 10

# se ajustan los datos para utilizarlos en las funciones
def cargar_datos(ruta):
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

# Aquí se despliega el login y el registro de la página
def desplegar_form(option):
    # URL del tratamiento de datos personales
    data_policy_link = "https://www.privacypolicies.com/live/510a8632-963e-45eb-b10b-dd5bf94ba46d"

    # Este es para el registro de la página
    if option == 'registro':
        with st.form(key='registration_form'):
            st.header("Registro")
            username = st.text_input('Nombre de usuario')
            password = st.text_input('Contraseña', type='password')
            confirm_password = st.text_input('Confirmar contraseña', type='password')
            
            # Agregar casilla de verificación para el acuerdo de tratamiento de datos personales
            data_agreement = st.checkbox(
                f' Acepto el [ tratamiento de mis datos personales]({data_policy_link})')          
            register_button = st.form_submit_button('Registrarse')

            # Para llamar a la función de registro
            if register_button:
                if username and password and password == confirm_password and data_agreement:
                    if len(username) >= 8 and len(password) >= 8:
                        utils.registro(username, password, confirm_password)
                    else:
                        st.error('Username and password must be at least 8 characters long.')
                elif not username:
                    st.error('You must specify a username.')
                elif not password:
                    st.error('You must specify a password.')
                elif password != confirm_password:
                    st.error('Passwords don\'t match.')
                elif not data_agreement:
                    st.error('In order to signup you must accept the personal data agreement')
                else:
                    st.error('An error has occurred, please try again.')

    # Este es para el login de la página
    elif option == 'ingreso':
        st.header('Inicio de Sesión')
        username = st.text_input('Nombre de usuario')
        password = st.text_input('Contraseña', type='password')
        login_button = st.button("Iniciar sesión")

        # Para llamar a la función de inicio de sesión
        if login_button:
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
    """
    En esta funcion se define las funciones que se 
    van a desplegar en la pagina principal
    """
    st.title("Appetito") 
    recetas_normales()

#Se muestran las erecetas sin clasificacion alguna
def recetas_normales():
    # Ruta del archivo recetas saludables json temporal para usar en consola local
    ruta_normales = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/dgarzonac/src/datos/recetas.json'
    df_recetas_normales = cargar_datos(ruta_normales)
    
    # Leer la lista de ingredientes
    ruta_ingredientes = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/dgarzonac/src/datos/ingredientes.json'
    lista_ingredientes = pd.read_json(ruta_ingredientes)
    lista_ingredientes = lista_ingredientes["ingredients"][0]

    # Crear una caja de selección para el filtro de dificultad
    ingredientes_deseados = st.multiselect("Selecciona los ingredientes:", lista_ingredientes)
    difficult = st.selectbox('Selecciona el nivel de dificultad', ['Todos', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Selecciona la subcategoría', ['Todos', "Lunch recipes", "Dinner recipes", "Breakfast recipes",
                                                               "Storecupboard","Cheese recipes", "Desserts", "Fish and seafood",
                                                               "Pasta", "Chicken", "Meat", "Vegetarian"])

    # Filtrar las recetas basándose en la dificultad,subcategoría y ingredientes
    if ingredientes_deseados:
        df_recetas_normales = df_recetas_normales[df_recetas_normales['ingredients'].apply(
            lambda x: any(ingrediente in ing for ing in x for ingrediente in ingredientes_deseados))]
        
    if difficult != 'Todos':
        df_recetas_normales = df_recetas_normales[
            df_recetas_normales['difficult'] == difficult]
    if subcategory != 'Todos':
        df_recetas_normales = df_recetas_normales[
            df_recetas_normales['subcategory'] == subcategory]

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_normales) // recetas_por_pagina
    if len(df_recetas_normales) % recetas_por_pagina > 0:
        total_paginas += 1

    # Verifica si hay páginas para mostrar
    if total_paginas > 0:
        # Crea un selector para la página
        pagina = st.selectbox('Selecciona una página', options=range(1, total_paginas + 1))

        # Filtra el DataFrame para obtener solo las recetas de la página seleccionada
        inicio = (pagina - 1) * recetas_por_pagina
        fin = inicio + recetas_por_pagina
        df_recetas_pagina = df_recetas_normales.iloc[inicio:fin]

        # Ahora puedes mostrar las recetas de df_recetas_pagina
        for _, receta in df_recetas_pagina.iterrows():
            st.markdown(
                f"""
                <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                    <img src="{receta['image']}" alt="Imagen de la receta" 
                    style="max-width: 100%; border-radius: 5px;">
                </div>
                """,
                unsafe_allow_html=True,
            )
            detalles_abiertos(receta)
    else:
        st.title("No hay recetas para mostrar.")


# Se muestran las recetas saludables
def recetas_saludables():
    # Ruta del archivo recetas saludables json temporal para usar en consola local
    ruta_saludable = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/src/datos/saludables.json'
    df_recetas_saludables = cargar_datos(ruta_saludable)

    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Selecciona el nivel de dificultad',
                              ['Todos', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Selecciona la subcategoría',
                                ['Todos', 'Smoothies', 'Salads',
                                  'Dinner', 'Fitness & lifestyle', 'High protein', 'Keto'])

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'Todos':
        df_recetas_saludables = df_recetas_saludables[
            df_recetas_saludables['difficult'] == difficult]
    if subcategory != 'Todos':
        df_recetas_saludables = df_recetas_saludables[
            df_recetas_saludables['subcategory'] == subcategory]

    if df_recetas_saludables.empty:
        st.title("No hay recetas saludables disponibles.")
        return None

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_saludables) // recetas_por_pagina
    if len(df_recetas_saludables) % recetas_por_pagina > 0:
        total_paginas += 1

    # Crea un selector para la página
    pagina = st.selectbox('Selecciona una página', options=range(1, total_paginas + 1))

    # Filtra el DataFrame para obtener solo las recetas de la página seleccionada
    if pagina != None:
        inicio = (pagina - 1) * recetas_por_pagina
        fin = inicio + recetas_por_pagina
        df_recetas_pagina = df_recetas_saludables.iloc[inicio:fin]

    # Aqui se despliegan las recetas saludables
    st.title("Recetas saludables")

    for index, receta in df_recetas_pagina.iterrows():
        # Mostrar la imagen previa con borde
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta['image']}" alt="Imagen de la receta"
                  style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta)


# Se muestras las recetas para un corto presupuesto(sencillaes)
def recetas_presupuesto():
    # Ruta del archivo recetas presupuesto json 
    ruta_presupuesto = "https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/src/datos/presupuesto.json"
    df_recetas_presupuesto = cargar_datos(ruta_presupuesto)

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

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_presupuesto) // recetas_por_pagina
    if len(df_recetas_presupuesto) % recetas_por_pagina > 0:
        total_paginas += 1

    # Crea un selector para la página
    pagina = st.selectbox('Selecciona una página', options=range(1, total_paginas + 1))

    # Filtra el DataFrame para obtener solo las recetas de la página seleccionada
    inicio = (pagina - 1) * recetas_por_pagina
    fin = inicio + recetas_por_pagina
    df_recetas_pagina = df_recetas_presupuesto.iloc[inicio:fin]

    for index, receta1 in df_recetas_pagina.iterrows():
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
    ruta_horneados = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/src/datos/horneados.json'
    df_recetas_horneados = cargar_datos(ruta_horneados)

    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Selecciona el nivel de dificultad',
                              ['Todos', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Selecciona la subcategoría',
                                ['Todos', 'Bread', 'Cakes', 'Desserts',
                                  "Kids' baking", 'Quick bakes','Savoury pastries',
                                  'Sweet treats','Vegan baking','Biscuit recipes'])

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'Todos':
        df_recetas_horneados = df_recetas_horneados[
            df_recetas_horneados['difficult'] == difficult]
    if subcategory != 'Todos':
        df_recetas_horneados = df_recetas_horneados[
            df_recetas_horneados['subcategory'] == subcategory]

    if df_recetas_horneados.empty:
        st.title("No hay recetas horneadas disponibles.")
        return None

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_horneados) // recetas_por_pagina
    if len(df_recetas_horneados) % recetas_por_pagina > 0:
        total_paginas += 1

    # Crea un selector para la página
    pagina = st.selectbox('Selecciona una página', options=range(1, total_paginas + 1))

    # Filtra el DataFrame para obtener solo las recetas de la página seleccionada
    inicio = (pagina - 1) * recetas_por_pagina
    fin = inicio + recetas_por_pagina
    df_recetas_pagina = df_recetas_horneados.iloc[inicio:fin]

    # Aqui se despliegan las recetas de presupuesto
    st.title("Recetas horneadas")
    
    for index, receta2 in df_recetas_pagina.iterrows():
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta2['image']}" alt="Imagen de la receta" 
                style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta2)


# Se muestran las recetas para ocasiones especiales
def recetas_especiales():
    # Ruta del archivo recetas presupuesto json 
    ruta_especiales = "https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/src/datos/especiales.json"
    df_recetas_especiales = cargar_datos(ruta_especiales)

    if df_recetas_especiales.empty:
        st.title("No  hay recetas especiales disponibles.")
        return None

    st.title("Recetas especiales")

    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Selecciona el nivel de dificultad',
                              ['Todos', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Selecciona la subcategoría',
                                ['Todos', 'Birthdays', 'Cocktails', 'Hosting',
                                  'Slow cooker',"Kids' birthdays","Mocktails",
                                  'Picnics','Barbecues','Spring recipes','Special occasions','Teas'])

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'Todos':
        df_recetas_especiales = df_recetas_especiales[
            df_recetas_especiales['difficult'] == difficult]
    if subcategory != 'Todos':
        df_recetas_especiales = df_recetas_especiales[
            df_recetas_especiales['subcategory'] == subcategory]

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_especiales) // recetas_por_pagina
    if len(df_recetas_especiales) % recetas_por_pagina > 0:
        total_paginas += 1

    # Crea un selector para la página
    pagina = st.selectbox('Selecciona una página', options=range(1, total_paginas + 1))

    # Filtra el DataFrame para obtener solo las recetas de la página seleccionada
    inicio = (pagina - 1) * recetas_por_pagina
    fin = inicio + recetas_por_pagina
    df_recetas_pagina = df_recetas_especiales.iloc[inicio:fin]

    for index, receta1 in df_recetas_pagina.iterrows():
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta1['image']}" alt="Imagen de la receta" 
                style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta1)
