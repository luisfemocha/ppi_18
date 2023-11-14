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
            usn = ''
            if 'key' not in a.keys():
                print('Account without key '+a)
                continue
            else:
                usn = a['key']
                cuentas[usn] = {'username': usn}

            for key in a.keys():
                if key == 'key':
                    continue
                else:
                    cuentas[usn][key] = a[key]

        return cuentas

    except Exception as e:
        return "Error en conexion, intente de nuevo."+e.__str__()


def check_cuenta(usn, pas):
    # TODO
    print('se revisa si existe y coincide')


def registrar_cuenta(usn, pas):
    # TODO
    print('se guarda la nueva cuenta')
