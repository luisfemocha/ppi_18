import streamlit as st

import inicio
import extras
from control import util

def desplegarForm(option):
    col1, col2 = st.columns(2)

    # Lógica para el registro
    if option == 'registro':
        with st.form(key='registration_form'):
            username = st.text_input('Nombre de usuario')
            password = st.text_input('Contraseña', type='password')
            confirm_password = st.text_input('Confirmar contraseña', type='password')
            register_button = st.form_submit_button('Registrarse')

            # Lógica para el botón de registro
            if register_button:
                util.registro(username, password, confirm_password)

    elif option == 'ingreso':
        with st.form(key='login_form'):
            col2.header('Iniciar Sesión')
            username = st.text_input('Nombre de usuario')
            password = st.text_input('Contraseña', type='password')
            login_button = st.form_submit_button('Iniciar Sesión')

            if login_button:
                util.ingreso(username, password)