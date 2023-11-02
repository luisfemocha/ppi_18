# CONTROL TIER
# In this file the functions that manage the data and logics of the app.

from typing import Dict, Any

import streamlit as st

# DATA Tier import
import conexion

# CONTROL Tier import
import funciones

user = None

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
    accounts: object = conexion.get_cuentas()
    print("Successful get accounts:\n" + str(accounts))

    if type(accounts) is dict:
        if len(accounts) > 0:
            print('Accounts are found')

            if usn in accounts:
                if accounts[usn]['password'] == pas:
                    print('Login successful')

                    user = accounts[usn]

                    st.session_state.pagina = 'principal'
                else:
                    print('Incorrect password')
            else:
                print('User not found')
        else:
            print("There are not accounts")
    else:
        print('Wrong data type of accounts')


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


def get_user():
    return user