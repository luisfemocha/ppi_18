# CAPA DATOS

# En este archivo se realizara la lectura de los dataset para manejarlos en control
import streamlit as st
from deta import Deta

token = st.secrets["token"]
# open(".streamlit/token.txt", "r").read()

espacio = Deta(token)
base = espacio.Base("ppi18_usuarios")

def get_cuentas():
    return base.fetch().items


def check_cuenta(usn, pas):
    # TODO
    print('se revisa si existe y coincide')


def registrar_cuenta(usn, pas):
    # TODO
    print('se guarda la nueva cuenta')
