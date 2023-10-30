# CAPA CONTROL

# En este archivo de van a poner las funciones que van a manejar los datos y la lógica de la aplicación.

import streamlit as st

# import desde la capa de datos
import conexion

cuentas = []

def registro(usn, pas, conf):
    if pas == conf:
        # TODO
        #  vista.extras.show_modal("se realiza el registro")
        st.write("se registra")
        print("se realiza el registro")
    else:
        # TODO
        #  vista.extras.show_modal("No coinciden las contraseñas")
        st.write("no se registra")
        print("no coinciden las contraseñas")


def ingreso(usn, pas):
    cuentas = cuentas = conexion.get_cuentas()
    print("se obtienen las cuentas\n" + str(cuentas))

    st.title("Se obtienen las cuentas\n" + str(cuentas))

    if (type(cuentas) is list):
        if (len(cuentas) >0):
            print("se tiene alguna cuenta")
        else:
            print("funcion vacia")


def get_ingredientes():
    return ["pollo", "pasta", "tomate", "queso", "lechuga", "zanahoria", "arroz", "cebolla"]


def get_recetas():
    return [
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


def trigger_recetas(ingredientes_usuario):
    list_recetas = utils.get_recetas()
    recetas_disponibles = []

    for receta in list_recetas:
        if all(ingrediente in ingredientes_usuario for ingrediente in receta["ingredientes"]):
            recetas_disponibles.append(receta["nombre"])

    if recetas_disponibles:
        st.success("¡Aquí tienes algunas recetas que puedes hacer!")
        st.write(random.choice(recetas_disponibles))
    else:
        st.warning("Lo siento, no encontré ninguna receta con esos ingredientes.")
