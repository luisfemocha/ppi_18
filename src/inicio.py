# PRESENTATION TIER

# No standard imports
# 3rd party library imports
import streamlit as st

# local imports from CONTROL tier
import funciones
from utils import get_user

version = "0.20231102L"

def sidebar():
    """
    This is the sidebar function, it creates a sidebar as its name says in it, it creates buttons according to the
    different views of the webpage.
    If any button is pressed the session_state changes and then the function functions.vista() is called.
    """
    # Get the current page of the session or establish it as 'principal' by default.
    pagina = st.session_state.get('pagina', 'principal')

    # Home is the splash page of the webpage, that is to say, the first view the user sees when entering the page either
    # as unregistered or registered.
    if st.sidebar.button("Home", key="inicio"):
        st.session_state.pagina = 'principal'

    print('User from start '+str(get_user()))
    st.sidebar.title("Recetas")

        # Para desplegar las recetas fit
    if st.sidebar.button("Recetas fit", key="recetas_fit"
                         ) or st.session_state.get('pagina') == 'saludable':
        st.session_state.pagina = 'saludable'

    # Para desplegar las recetas sencillas
    if st.sidebar.button("Recetas sencillas", key="recetas_sencillas"
                         ) or st.session_state.get('pagina') == 'presupuesto':
        st.session_state.pagina = 'presupuesto'
    
    # Para desplegar las recetas especiales
    if st.sidebar.button("Recetas especiales", key="recetas_especiales"
                         ) or st.session_state.get('pagina') == 'especiales':
            st.session_state.pagina = 'especiales'
    
    # Para desplegar las recetas horneadas
    if st.sidebar.button("Recetas horneadas", key="recetas_horneadas"
                         ) or st.session_state.get('pagina') == 'horneado':
        st.session_state.pagina = 'horneado'
    
    # Aqui es la parte de cuenta de la apliacion
    st.sidebar.title("Cuenta")

    # Para reguistrarse
    if st.sidebar.button("Registrarse", key="registro"
                         ) or st.session_state.get('pagina') == 'registro':
        st.session_state.pagina = 'registro'
    
    # Para iniciar sesion
    if st.sidebar.button("Iniciar Sesión", key="ingreso"
                         ) or st.session_state.get('pagina') == 'ingreso':
        st.session_state.pagina = 'ingreso'

    # Llamar a la función para mostrar la página correspondiente
    funciones.vistas(pagina)

# Pie de pagina aqui se vera el contacto y los desarrolladores
def footer():
    """
    Esta funcion es para mirar el nombre de los desarrolladores
    """
    st.markdown("""
    <style>
        /* Se ocultan el header y footer defaults mientras se desarrolla la app */
        .ezrtsby2, .ea3mdgi1 { visibility: hidden; }
        .pie_de_pagina: {
            position: fixed; 
            bottom: 0; 
            width: 100%; 
            height: 50px; 
            background-color: #00000; 
            color: #ffffff; 
            text-align: left; 
            padding-top: 15px; 
            padding-left: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <footer class='pie_de_pagina'>
        Desarrollado por: Daniel Garzon Y Luis Moreno | 
                Contacto: dgarzonac@unal.edu.co</a> Y lumorenoc@unal.edu.co</a>
                
                Version: """ + version + """
    </footer>
    """, unsafe_allow_html=True)

# Se llama siemopre sidebar y footer por que siempre son visibles
sidebar()
footer()