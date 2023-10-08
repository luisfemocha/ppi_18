# Se importan las librerias especificadas en el informe 01 y Streamlit
import numpy as np
import pandas as pd

import streamlit as st

import extras
import formularios


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
pagina = "inicio"

if st.sidebar.button("Inicio", key="inicio"):
    pagina = "inicio"

if st.sidebar.button("Registrarse", key="registro"):
    pagina = "registro"

if st.sidebar.button("Iniciar Sesión", key="ingreso"):
    pagina = "ingreso"

if st.sidebar.button("Recetas fit", key="recetas_fit"):
    pagina = "recetas_fit"

if st.sidebar.button("Recetas sencillas", key="recetas_sencillas"):
    pagina = "recetas_sencillas"

if pagina == "inicio":
    # Configurar la aplicacion Streamlit
    st.title("Appetito")
    st.text("Daniel")
    st.text("Luis")

    list_ingredientes = st.multiselect("Selecciona los ingredientes:", utils.get_ingredientes(), key="ingredientes")
    ingredientes_usuario = [ingrediente.lower() for ingrediente in list_ingredientes]

    try:
        if ingredientes_usuario:
            utils.trigger_recetas(ingredientes_usuario)
    except Exception as e:
        print(f"An error occurred: {e}")


elif pagina == "registro":
    formularios.desplegarForm('registro')

elif pagina == "ingreso":
    formularios.desplegarForm('ingreso')

elif pagina == "recetas_fit":
    formularios.recetas_fit()

elif pagina == "recetas_sencillas":
    formularios.recetas_sencillas()
