# CAPA VISTA

import streamlit as st

# librerias de capa vista

# librerias de capa control
import funciones

def sidebar():
    st.sidebar.title("Cuenta")

    pagina = ''

    if st.sidebar.button("Inicio", key="inicio") or pagina=='':
        pagina='principal'

    if st.sidebar.button("Registrarse", key="registro"):
        pagina = 'registro'

    if st.sidebar.button("Iniciar Sesión", key="ingreso"):
        pagina= 'ingreso'

    if st.sidebar.button("Recetas fit", key="recetas_fit"):
        pagina = 'saludable'

    if st.sidebar.button("Recetas sencillas", key="recetas_sencillas"):
        pagina = 'presupuesto'

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