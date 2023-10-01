# Se importan las librerias especificadas en el informe 01 y Streamlit
import streamlit as st

import numpy as np
import pandas as pd
import random

import formularios
import extras

try:
    from control import util
except:
    import os
    import sys

    # Obtiene el directorio del script actual (inicio.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Obtiene el directorio del padre (src)
    parent_dir = os.path.dirname(current_dir)

    # Agrega el directorio del padre al sys.path
    sys.path.append(parent_dir)

    from control import util

try:
    import matplotlib
except:
    # TODO
    print("Problemas para importar matplotlib")

st.sidebar.title("Cuenta")

# Opción para registrarse
if st.sidebar.button("Registrarse"):
    formularios.desplegarForm('registro')

# Opción para iniciar sesión
if st.sidebar.button("Iniciar Sesión"):
    formularios.desplegarForm('ingreso')

# Contenido principal de la aplicación
st.title("Aplicación Principal")
st.write("Este es el contenido principal de tu aplicación.")

# Configurar la aplicacion Streamlit
st.title("Appetito")

# Ingredientes para iniciar la prueba
list_ingredientes = ["pollo", "pasta", "tomate", "queso", "lechuga", "zanahoria", "arroz", "cebolla"]

# Recetas para la prueba
list_recetas = [
    {
        "nombre": "Ensalada César",
        "ingredientes": ["lechuga", "pollo", "crutones", "aderezo"]
    },
    {
        "nombre": "Pasta Marinara",
        "ingredientes": ["pasta", "salsa de tomate", "albahaca", "queso"]
    },
    {
        "nombre": "Arroz con pollo",
        "ingredientes": ["arroz", "pollo", "cebolla", "zanahoria"]
    }
]
# Obtener la divisa de origen y destino
ingredientes_usuario = st.multiselect("Selecciona los ingredientes:", list_ingredientes)
ingredientes_usuario = [ingrediente.lower() for ingrediente in ingredientes_usuario]

if ingredientes_usuario:
    recetas_disponibles = []
    for receta in list_recetas:
        if all(ingrediente in ingredientes_usuario for ingrediente in receta["ingredientes"]):
            recetas_disponibles.append(receta["nombre"])

    if recetas_disponibles:
        st.success("¡Aquí tienes algunas recetas que puedes hacer!")
        st.write(random.choice(recetas_disponibles))
    else:
        st.warning("Lo siento, no encontré ninguna receta con esos ingredientes.")