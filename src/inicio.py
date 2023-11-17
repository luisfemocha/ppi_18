# PRESENTATION TIER

# No standard imports
# 3rd party library imports
import streamlit as st

# local imports from CONTROL tier
import funciones

version = "0.20231102L"

def sidebar():
    """
    This is the sidebar function, it creates a sidebar as its name says in it, it creates buttons according to the
    different views of the webpage.
    If any button is pressed the session_state changes and then the function functions.vista() is called.
    """
    # Get the current page of the session or establish it as 'principal' by default.
    user = st.session_state.get('user', None)

    # Home is the splash page of the webpage, that is to say, the first view the user sees when entering the page either
    # as unregistered or registered.
    if st.sidebar.button("Home", key="home"):
        st.session_state.page = 'home'

    if user is not None:
        print('User from start '+str(user))

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

        # Aqui es la parte de cuenta de la apliacion
        st.sidebar.title(user['username'])
        if st.sidebar.button("Account view", key="account"):
            st.session_state.page = 'account'

        if st.sidebar.button("Settings", key="settings"):
            st.session_state.page = 'settings'

        # To login signin - access existing account
        if st.sidebar.button("Log off", key="logoff"):
            st.session_state.page = 'logoff'

    else:
        # Aqui es la parte de cuenta de la apliacion
        st.sidebar.title("Account")
        # To signup - create account
        if st.sidebar.button("Sign up", key="signup"):
            st.session_state.page = 'signup'

        # To login signin - access existing account
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