# CAPA VISTA

import streamlit as st
# librerias de capa vista
import funciones  

def sidebar():
    """
    esta es la funcion del sidebar segun esto se llama a la opcion de la
    aplicacion que desee el usario, para mirar una categoria de recetas
    o estar en la pagina principal
    """
    # Obtener la página actual de la sesión o establecerla en 'principal' 
    # Por defecto
    pagina = st.session_state.get('pagina', 'principal')
    
    # Esta pagina home es la pagina principal y de inicio cuando el usuario 
    # Recien entra a la pagina
    if st.sidebar.button("Home", key="inicio"):
        st.session_state.pagina = 'principal'

    # Esta es la parte de recetas
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
    </footer>
    """, unsafe_allow_html=True)

# Se llama siemopre sidebar y footer por que siempre son visibles
sidebar()
footer()