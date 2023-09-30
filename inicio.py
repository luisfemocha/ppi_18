# Se importan las librerias especificadas en el informe 01 y Streamlit
import streamlit as st

import numpy as np
import pandas as pd
import matplotlib

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