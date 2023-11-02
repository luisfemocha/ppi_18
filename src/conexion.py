# CAPA DATOS

# En este archivo se realizara la lectura de los dataset para manejarlos en control
import streamlit as st
from deta import Deta

token = st.secrets["token"]
# open(".streamlit/token.txt", "r").read()

espacio = Deta(token)
base = espacio.Base("ppi18_usuarios")

def get_cuentas() -> object:
    try:
        lista_cuentas = base.fetch().items
        cuentas = {}

        for a in lista_cuentas:
            # bandera primer objeto || llave inicial == username
            bpo = None
            for key in a.keys():
                if bpo is None:
                    bpo = a[key]
                    if bpo in cuentas:
                        break
                    else:
                        cuentas[bpo]= {}
                else:
                    cuentas[bpo][key] = a[key]

        return cuentas
    except:
        return "Error en conexion, intente de nuevo."


def check_cuenta(usn, pas):
    # TODO
    print('se revisa si existe y coincide')


def registrar_cuenta(usn, pas):
    # TODO
    print('se guarda la nueva cuenta')
