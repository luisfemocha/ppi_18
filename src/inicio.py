# PRESENTATION TIER

# No standard imports
# 3rd party library imports
import streamlit as st
from streamlit import session_state
# local imports from CONTROL tier
import funciones
import streamlit_authenticator as stauth
import conexion

version = "0.20231102L"

st.set_page_config(
    page_title="Appetito",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded")

def sidebar():
    """
    Esta función define y despliega la barra lateral de la aplicación "Appetito". Crea botones,
    según las diferentes vistas de la página web. Si se presiona algún botón, la sesión cambia
    y luego se llama a la función funciones.vistas() para mostrar la página correspondiente.

    """

    # Obtener la página actual de la sesión o establecerla como 'principal' por defecto.
    user = st.session_state.get('user', None)
    authentication_status = st.session_state.get('loged_in', False)
    
    # Home es la página principal de la aplicación, es decir, la primera vista que
    # Ve el usuario al entrar a la página ya sea como no registrado o registrado.
    if st.sidebar.button("Home", key="home"):
        st.session_state.page = 'home'

    if user is not None:
        st.sidebar.title(user['username'])
        print('User from start ' + str(user))

        st.sidebar.title("Recipes")
        # Para desplegar las recetas fit
        if st.sidebar.button("Healthy recipes", key="recetas_fit"):
            st.session_state.page = 'saludable'

        # Para desplegar las recetas sencillas
        if st.sidebar.button("Simple Recipes", key="recetas_sencillas"):
            st.session_state.page = 'presupuesto'

        # Para desplegar las recetas especiales
        if st.sidebar.button("Special Recipes", key="recetas_especiales"):
            st.session_state.page = 'especiales'

        # Para desplegar las recetas horneadas
        if st.sidebar.button("Baked Recipes", key="recetas_horneadas"):
            st.session_state.page = 'horneado'

        # Aquí es la parte de cuenta de la aplicación
        st.sidebar.title(user['username'])
        if st.sidebar.button("Account view", key="account"):
            st.session_state.page = 'account'

        if st.sidebar.button("Settings", key="settings"):
            st.session_state.page = 'settings'

        # Para cerrar sesión - salir
        if st.sidebar.button("Log off", key="logoff"):
            # Aquí puedes agregar la lógica para cerrar la sesión
            # Y reiniciar las variables de estado
            st.session_state.user = None
            st.session_state.authentication_status = False
            st.session_state.page = 'home'

    else:
        # Aquí es la parte de cuenta de la aplicación
        st.sidebar.title("Account")
        # Para registrarse - crear cuenta
        if st.sidebar.button("Sign up", key="signup"):
            st.session_state.page = 'signup'

        # Para iniciar sesión - acceder a una cuenta existente
        if st.sidebar.button("Log In", key="login"):
            st.session_state.page = 'login'

    # Llamar a la función para mostrar la página correspondiente
    page = st.session_state.get('page', 'home')
    funciones.vistas(page)


def footer():
    """
    This function creates the footer in order to view developers info.
    """
    st.markdown("""
    <style>
        .ezrtsby2, .ea3mdgi1 { visibility: hidden; }
        .footer: {
            position: fixed; 
            bottom: 0; 
            width: 100%; 
            height: 50px; 
            background-color: #00000; 
            color: #ffffff; 
            text-align: left; 
            padding-top: 15px; 
            padding-left: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <footer class='footer'>
        Developed by: Daniel Garzon and Luis Moreno | 
        Contact: dgarzonac@unal.edu.co</a> and lumorenoc@unal.edu.co</a>
    </footer>
    """,unsafe_allow_html=True)

# sidebar and footer functions are always called to be always visible



sidebar()
footer()