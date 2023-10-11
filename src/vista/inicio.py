# Se importan las librerias especificadas en el informe 01 y Streamlit
import streamlit as st

# librerias de paquete
import extras

# librerias de capa control
# from control import utils
import control.utils as utils

listener_lateral = None


def pagina_principal():
    listener_lateral = extras.sidebar()
    # Pagina principal
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

    extras.footer()


pagina_principal()

if listener_lateral != None and listener_lateral != "pagina_principal":
    pagina_principal()
