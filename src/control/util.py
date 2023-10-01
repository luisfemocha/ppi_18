# En este archivo de van a poner las funciones que van a manejar los datos y la lógica de la aplicación.

import streamlit as st

import vista
from datos import conexion

def ingreso(usn,pas, conf):
    if (pas == conf):
        # TODO
        #  vista.extras.show_modal("se realiza el registro")
        st.write("se registra")
        print("se realiza el registro")
    else:
        # TODO
        #  vista.extras.show_modal("No coinciden las contraseñas")
        st.write("no se registra")
        print("no coinciden las contraseñas")

def registro(usn,pas):
    print("a")