# CAPA VISTA

import streamlit as st

# librerias de capa vista

# librerias de capa control
import funciones


def sidebar():
    # Obtener la página actual de la sesión o establecerla en 'principal' por defecto
    pagina = st.session_state.get('pagina', 'principal')
    
    if st.sidebar.button("Home", key="inicio"):
        st.session_state.pagina = 'principal'

    st.sidebar.title("Recetas")

    if st.sidebar.button("Recetas fit", key="recetas_fit") or pagina == 'saludable':
        st.session_state.pagina = 'saludable'

    if st.sidebar.button("Recetas sencillas", key="recetas_sencillas") or pagina == 'presupuesto':
        st.session_state.pagina = 'presupuesto'

    if st.sidebar.button("Recetas especiales", key="recetas_especiales") or pagina == 'especiales':
            st.session_state.pagina = 'especiales'

    if st.sidebar.button("Recetas horneadas", key="recetas_horneadas") or pagina == 'horneado':
        st.session_state.pagina = 'horneado'
    
    st.sidebar.title("Cuenta")

    if st.sidebar.button("Registrarse", key="registro") or pagina == 'registro':
        st.session_state.pagina = 'registro'

    if st.sidebar.button("Iniciar Sesión", key="ingreso") or pagina == 'ingreso':
        st.session_state.pagina = 'ingreso'

    # Llamar a la función para mostrar la página correspondiente
    funciones.vistas(pagina)




# Pie de pagina aqui se vera el contacto y los desarrolladores
def footer():
    # .reportview-container .main footer { visibility: hidden; }
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
        Desarrollado por: Daniel Garzon Y Luis Moreno | Contacto: dgarzonac@unal.edu.co</a> Y lumorenoc@unal.edu.co</a>
    </footer>
    """, unsafe_allow_html=True)

sidebar()
footer()