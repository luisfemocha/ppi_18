# CONTROL TIER

import json
import requests

import pandas as pd
import streamlit as st

import matplotlib.pyplot as plt

import conexion

# variables globales
ruta_ingredientes = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/'\
                    'main/src/datos/ingredientes.json'
ruta_normales = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/'\
                'dgarzonac/src/datos/recetas.json'
ruta_saludable = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/'\
                 'main/src/datos/saludables.json'
ruta_presupuesto = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/'\
                   'main/src/datos/presupuesto.json'
ruta_horneados = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/'\
                 'src/datos/horneados.json'
ruta_especiales = 'https://raw.githubusercontent.com/Luisfemocha/ppi_18/main/'\
                  'src/datos/especiales.json'

# Para exportar las rutas / variables globales anteriores
def get_rutas():
    return {
        'ingredientes': ruta_ingredientes,
        'normales': ruta_normales,
        'saludable': ruta_saludable,
        'presupuesto': ruta_presupuesto,
        'horneados': ruta_horneados,
        'especiales': ruta_especiales
    }


# se ajustan los datos para utilizarlos en las funciones
def cargar_datos(ruta):
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
    except:
        st.title("Error al leer el archivo "+ruta)
        return pd.DataFrame()

 
# Visualizacion de cada receta
def detalles_abiertos(recipe):
    # Verifica si se debe mostrar los detalles de esta receta
    # if receta['id'] in detalles_abiertos and detalles_abiertos[receta['id']]:
    with st.expander(f"View Details of {recipe['name']}"):
        st.subheader(recipe["name"])

        if 'logged_in' in st.session_state and st.session_state['logged_in']:
            if st.button("Add recipe to favorites", key="fav-"+recipe["id"]):
                print('Se agrega a favoritas la receta')
                # print(recipe)
                print(recipe["id"])

                try:
                    print("se intenta encontrar la receta con el id")

                    print(st.session_state['recetas_normales'][recipe["id"]])
                except:
                    print("paila")

        # Detalles de la receta (puedes usar un bucle para iterar sobre los datos)
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

        if recipe['nutrients'] != {}: 
            # Nutrientes
            st.header("Nutrients")
            for nutrient in recipe['nutrients']:
                cantidad = recipe['nutrients'].get(nutrient, 'No Nutrient')
                st.write(f"{nutrient}: {cantidad}")
            names_nurients = list(recipe['nutrients'].keys())
            values_nutrients = list(recipe['nutrients'].values())
            values_nutrients = [value[:-1] for value in values_nutrients]

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


# Segun esta funcion se cambian de vistas
def vistas(vista):
    """
    This function changes page views according to the sidebar and the option
    the user chooses.
    """

    if vista == 'home':
        home_page()
    elif vista =='saludable':
        recetas_saludables()
    elif vista == 'presupuesto':
        recetas_presupuesto()
    elif vista == 'horneado':
        recetas_horneados()
    elif vista == 'especiales':
        recetas_especiales() 
    elif vista == 'signup':
        conexion.sign_up()
    elif vista == 'login':
        conexion.log_in()


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


#Se muestran las erecetas sin clasificacion alguna
def recetas_normales():
    if (st.session_state['logged_in'] == False or
            st.session_state['logged_in'] == None):
        # Para motivar a el usuario a registrarse o iniciar sesión
        st.title("Welcome to Appetito To know many more recipes, "+
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
                print("Ya estaba la receta con id",receta_n["id"])
        st.session_state['recetas_normales'] = obj_recetas_normales

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = obj_recetas_normales
        else:
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

    # Crear una caja de selección para el filtro de dificultad
    ingredientes_deseados = st.multiselect(
        "Select ingredients:", lista_ingredientes
    )

    difficult = st.selectbox(
        'Select difficulty level',
        ['All', 'Easy', 'More effort', 'A challenge']
    )

    subcategory = st.selectbox(
        'Select subcategory', 
        ['All', "Lunch recipes", "Dinner recipes","Breakfast recipes",
        "Storecupboard","Cheese recipes", "Desserts","Fish and seafood",
        "Pasta", "Chicken", "Meat", "Vegetarian"]
    )


    # Filtrar las recetas basándose en la dificultad, subcategoría e ingredientes
    if ingredientes_deseados:
        df_recetas_normales = df_recetas_normales[
            df_recetas_normales['ingredients'].apply(
                lambda x: any(ingrediente in ing for ing in x for ingrediente in ingredientes_deseados)
            )
        ]

    if difficult != 'All':
        df_recetas_normales = df_recetas_normales[
            df_recetas_normales['difficult'] == difficult
        ]

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
        pagina = st.selectbox('Select a page', options=range(1, total_paginas + 1))

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
        st.title("No recipes to display.")


# Se muestran las recetas saludables
def recetas_saludables():
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
                print("Ya estaba la receta con id",receta_s["id"])
        st.session_state['recetas_saludables'] = obj_recetas_saludables

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = obj_recetas_saludables
        else:
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

    # Crear una caja de selección para el filtro de dificultad
    ingredientes_deseados = st.multiselect(
        "Select ingredients:", lista_ingredientes
    )

    
    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Select the difficulty level',
                              ['All', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Select the subcategory',
                                ['All', 'Smoothies', 'Salads',
                                  'Dinner', 'Fitness & lifestyle', 'High protein', 'Keto'])
    
    # Filtrar las recetas basándose en la dificultad, subcategoría e ingredientes
    if ingredientes_deseados:
        df_recetas_saludables = df_recetas_saludables[
            df_recetas_saludables['ingredients'].apply(
                lambda x: any(ingrediente in ing for ing in x for ingrediente in ingredientes_deseados)
            )
        ]

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

    # Filtra el DataFrame para obtener solo las recetas de la página seleccionada
    if pagina != None:
        inicio = (pagina - 1) * recetas_por_pagina
        fin = inicio + recetas_por_pagina
        df_recetas_pagina = df_recetas_saludables.iloc[inicio:fin]

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
                print("Ya estaba la receta con id",receta_p["id"])
        st.session_state['recetas_presupuesto'] = obj_recetas_presupuesto

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = obj_recetas_presupuesto
        else:
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
    # Crear una caja de selección para el filtro de dificultad
    ingredientes_deseados = st.multiselect(
        "Select ingredients:", lista_ingredientes
    )

    # Filtrar las recetas basándose en la dificultad, subcategoría e ingredientes
    if ingredientes_deseados:
        df_recetas_presupuesto = df_recetas_presupuesto[
            df_recetas_presupuesto['ingredients'].apply(
                lambda x: any(ingrediente in ing for ing in x for ingrediente in ingredientes_deseados)
            )
        ]

    if df_recetas_presupuesto.empty:
        st.title("No simple recipes available.")
        return None

    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Select the difficulty level', ['All', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Select the subcategory', ['All', 'Budget dinners', 'Batch cooking', 'Student meals', 'Freezable meals', 'Slow cooker'])

    # Filtrar las recetas basándose en la dificultad y subcategoría
    if difficult != 'All':
        df_recetas_presupuesto = df_recetas_presupuesto[df_recetas_presupuesto['difficult'] == difficult]
    if subcategory != 'All':
        df_recetas_presupuesto = df_recetas_presupuesto[df_recetas_presupuesto['subcategory'] == subcategory]

    # Define el número de recetas por página
    recetas_por_pagina = 10

    # Calcula el número total de páginas
    total_paginas = len(df_recetas_presupuesto) // recetas_por_pagina
    if len(df_recetas_presupuesto) % recetas_por_pagina > 0:
        total_paginas += 1

    # Crea un selector para la página
    pagina = st.selectbox('Select a page', options=range(1, total_paginas + 1))

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
                print("Ya estaba la receta con id",receta_horneado["id"])
        st.session_state['recetas_horneados'] = obj_recetas_horneados

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = obj_recetas_horneados
        else:
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

    # Crear una caja de selección para el filtro de dificultad
    ingredientes_deseados = st.multiselect(
        "Select ingredients:", lista_ingredientes
    )

    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Select the difficulty level',
                              ['All', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Select the subcategory',
                                ['All', 'Bread', 'Cakes', 'Desserts',
                                  "Kids' baking", 'Quick bakes','Savoury pastries',
                                  'Sweet treats','Vegan baking','Biscuit recipes'])
    
    # Filtrar las recetas basándose en la dificultad, subcategoría e ingredientes
    if ingredientes_deseados:
        df_recetas_horneados = df_recetas_horneados[
            df_recetas_horneados['ingredients'].apply(
                lambda x: any(ingrediente in ing for ing in x for ingrediente in ingredientes_deseados)
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

    # Filtra el DataFrame para obtener solo las recetas de la página seleccionada
    inicio = (pagina - 1) * recetas_por_pagina
    fin = inicio + recetas_por_pagina
    df_recetas_pagina = df_recetas_horneados.iloc[inicio:fin]
    
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
                print("Ya estaba la receta con id",receta_e["id"])
        st.session_state['recetas_horneados'] = obj_recetas_especiales

        if 'recetas' not in st.session_state:
            st.session_state['recetas'] = obj_recetas_especiales
        else:
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

    if df_recetas_especiales.empty:
        st.title("No special recipes available.")
        return None

    # Crear una caja de selección para el filtro de dificultad
    ingredientes_deseados = st.multiselect(
        "Select ingredients:", lista_ingredientes
    )
    # Crear una caja de selección para el filtro de dificultad
    difficult = st.selectbox('Select difficulty level',
                              ['All', 'Easy', 'More effort', 'A challenge'])
    subcategory = st.selectbox('Select subcategory',
                                ['All', 'Birthdays', 'Cocktails', 'Hosting',
                                  'Slow cooker',"Kids' birthdays","Mocktails",
                                  'Picnics','Barbecues','Spring recipes','Special occasions','Teas'])
    
    # Filtrar las recetas basándose en la dificultad, subcategoría e ingredientes
    if ingredientes_deseados:
        df_recetas_especiales = df_recetas_especiales[
            df_recetas_especiales['ingredients'].apply(
                lambda x: any(ingrediente in ing for ing in x for ingrediente in ingredientes_deseados)
            )
        ]
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