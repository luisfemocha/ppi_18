# Se importan las librerias especificadas en el informe 01 y Streamlit
import streamlit as st

import numpy as np
import pandas as pd

import formularios
import extras

try:
    import control.utils as utils
except:
    import os
    import sys

    # Obtiene el directorio del script actual (inicio.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Obtiene el directorio del padre (src)
    parent_dir = os.path.dirname(current_dir)

    # Agrega el directorio del padre al sys.path
    sys.path.append(parent_dir)

    import control.utils as utils

try:
    import matplotlib
except:
    # TODO
    print("Problemas para importar matplotlib")

st.sidebar.title("Cuenta")
home_page = st.empty()
with home_page:
    if st.sidebar.button("Inicio", key="inicio"):
        # Configurar la aplicacion Streamlit
        st.title("Appetito")
        st.text("Daniel")
        st.text("Luis")

        list_ingredientes = st.multiselect("Selecciona los ingredientes:", utils.get_ingredientes(), key="ingredientes")
        ingredientes_usuario = [ingrediente.lower() for ingrediente in list_ingredientes]

        if ingredientes_usuario:
            utils.trigger_recetas(ingredientes_usuario)
# Opción para registrarse
if st.sidebar.button("Registrarse", key="registro"):
    formularios.desplegarForm('registro')
    home_page.empty()

# Opción para iniciar sesión
if st.sidebar.button("Iniciar Sesión", key="ingreso"):
    formularios.desplegarForm('ingreso')
    home_page.empty()

# Opción para registrarse
if st.sidebar.button("Recetas fit", key="recetas_fit"):
    formularios.recetas_fit()
    home_page.empty()

# Opción para iniciar sesión
if st.sidebar.button("Recetas sencillas", key="recetas_sencillas"):
    formularios.recetas_sencillas()
    home_page.empty()
