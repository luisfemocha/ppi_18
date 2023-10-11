import streamlit as st

import control.funciones as funciones


def sidebar():
    st.sidebar.title("Cuenta")
    pagina = "inicio"

    if st.sidebar.button("Inicio", key="inicio"):
        pagina = "inicio"
        return "pagina_principal"

    elif st.sidebar.button("Registrarse", key="registro"):
        pagina = "registro"
        funciones.desplegar_form('registro')

    elif st.sidebar.button("Iniciar Sesión", key="ingreso"):
        pagina = "ingreso"
        funciones.desplegar_form('ingreso')

    elif st.sidebar.button("Recetas fit", key="recetas_fit"):
        pagina = "recetas_fit"
        funciones.recetas_fit()

    elif st.sidebar.button("Recetas sencillas", key="recetas_sencillas"):
        pagina = "recetas_sencillas"
        funciones.recetas_sencillas()

    else:
        return None


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


def show_modal(msg):
    # TODO ==> Corregir
    modal_style = """
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    """

    # Contenido del modal
    with st.markdown('<div style="{}">'.format(modal_style), unsafe_allow_html=True):
        with st.container():
            st.write("Alerta")
            st.write("<p>" + msg + "</p>")
            close_button = st.button("Cerrar Modal")

    # Si se hace clic en "Cerrar Modal"
    if close_button:
        # Oculta el modal estableciendo la variable show_modal en False
        show_modal = False
