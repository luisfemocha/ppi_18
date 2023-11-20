# CAPA DATOS

# En este archivo se manejara el inicio de sesion y registro
from datetime import datetime
import re

import streamlit as st
from streamlit import session_state

from funciones import *
from deta import Deta

# Clave para Deta Base
DETA_KEY = "e0m3ypPCenY_6yhHxaZYb4LDBhYTD3DKPsnd9ABPk5gN"

# Inicializar conexión a Deta Base
deta = Deta(DETA_KEY)

# Inicializar Base de Datos de Deta para usuarios
db = deta.Base('Appetito_usuarios')

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    
def insert_user(username, password):
    """
    Inserta un nuevo usuario en la base de datos.

    Parameters:
    - username (str): Nombre de usuario.
    - password (str): Contraseña del usuario.

    Returns:
    - dict: Información del usuario insertado.
    """
    date_joined = str(datetime.now())
    user_data = {
        'username': username,
        'password': password,
        'date_joined': date_joined,
        'favorites': []
    }
    return db.put(user_data)


def actualizar_usuarios():
    """
    Obtiene la lista de usuarios almacenados en la base de datos.

    Returns:
    - list: Lista de usuarios.
    """
    usuarios = db.fetch()
    return usuarios.items


def get_usernames():
    """
    Obtiene la lista de nombres de usuario almacenados en la base de datos.

    Returns:
    - list: Lista de nombres de usuario.
    """
    usuarios = db.fetch()
    usernames = []
    for usuario in usuarios.items:
        usernames.append(usuario['username'])
    return usernames


def validate_username(username):
    """
    Valida si el nombre de usuario cumple con ciertos requisitos.
    Parameters:
    - username (str): Nombre de usuario a validar.

    Returns:
    - bool: True si el nombre de usuario es válido, False de lo contrario.
    """
    pattern = r"^[a-zA-Z0-9_]*$"
    return bool(re.match(pattern, username))


def sign_up():
    """
    Muestra un formulario de registro y realiza la validación y
    registro del usuario.

    Este formulario incluye campos para el nombre de usuario, contraseña,
    confirmación de contraseña y una casilla de verificación para aceptar
    el acuerdo de tratamiento de datos personales.

    Una vez que el usuario completa el formulario y hace clic en el botón
    de registro, se realizan las siguientes
    validaciones:
    - Verifica que el nombre de usuario no exista previamente en la base
      de datos.
    - Verifica que el nombre de usuario tenga al menos 4 caracteres.
    - Verifica que el nombre de usuario solo contenga caracteres
      alfanuméricos y guiones bajos.
    - Verifica que se haya proporcionado una contraseña.
    - Verifica que las contraseñas coincidan.
    - Verifica que el usuario haya aceptado el acuerdo de tratamiento de
      datos personales.

    Si todas las validaciones son exitosas, se registra el nuevo usuario
    en la base de datos.

    """
    # Enlace a la política de privacidad
    data_policy_link = (
        "https://www.privacypolicies.com/live/"
        "510a8632-963e-45eb-b10b-dd5bf94ba46d")

    # Iniciar un formulario en Streamlit
    with st.form(key='registration_form'):
        st.header("Register")
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        confirm_password = st.text_input('Confirm Password', type='password')

        # Agregar casilla de verificación para el acuerdo de tratamiento
        # De datos personales
        data_agreement = st.checkbox(
            f'I agree to the [processing of my personal data]'
            f'({data_policy_link})')
        register_button = st.form_submit_button('Register')

        # Para llamar a la función de registro
        if register_button:
            # Imprimir resultado de la validación del nombre de usuario
            print(validate_username(username))
            # Validaciones del formulario
            if username in get_usernames():
                st.error('The user already exists, please enter another')
            if len(username) < 4:
                st.error('Username must be at least 4 characters long.')
            if not validate_username(username):
                st.error('Username can only contain alphanumeric characters'
                         'and underscores.')
            elif not password:
                st.error('You must specify a password.')
            elif password != confirm_password:
                st.error('Passwords don\'t match.')
            elif not data_agreement:
                st.error('In order to signup you must accept the personal data'
                         'agreement')
            else:
                # Registrar nuevo usuario si todas las validaciones son
                # exitosas y informarle que se ha registrado correctamente
                insert_user(username, password)
                st.write('You have successfully registered!')


def log_in():
    """
    Muestra un formulario de inicio de sesión y realiza la autenticación del
    usuario.

    Este formulario incluye campos para el nombre de usuario y la contraseña.
    Cuando el usuario hace clic en el botón "Log in", se realiza la
    autenticación verificando las credenciales proporcionadas con los
    usuarios almacenados en la base de datos.

    Si las credenciales son correctas, el usuario se autentica y se almacena
    su estado de inicio de sesión en la variable de estado de Streamlit.
    Se proporciona la opción de cerrar sesión si el usuario está autenticado.
    """
    st.title("Log in")

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    # Botón para iniciar sesión
    if st.button("Log in"):
        cuenta = validar_credenciales(username, password)
        if cuenta:
            # Establecer el estado de inicio de sesión y el nombre de
            # Usuario en la variable de estado de Streamlit
            st.session_state['logged_in'] = True
            st.session_state.nombre = username
            if st.session_state['logged_in']:
                st.write("Logged in as: " + username)
                st.session_state.nombre = username
                st.session_state.cuenta = cuenta
                st.experimental_rerun()
        else:
            st.error("Incorrect Username/Password")
            st.session_state['logged_in'] = False

    # Mostrar botón para cerrar sesión si el usuario está autenticado
    if st.session_state['logged_in']:
        if st.button("Log out"):
            # Cerrar sesión y restablecer variables de estado
            st.session_state['logged_in'] = False
            st.session_state.nombre = None
            st.write("Logged out")
            st.experimental_rerun()



def recetas_favoritas():
    """
    Muestra las recetas favoritas del usuario.
    """

    if not st.session_state['logged_in']:
        st.title("USER NOT LOGGED IN")
        return False
    else:
        st.title("Favorite Recipes")
        if 'favoritas' in session_state:
            recetas_favoritas = session_state.favoritas
        else:
            ids_favoritas = session_state.cuenta['favorites']

            if 'recetas' not in st.session_state:
                if 'recetas_normales' not in st.session_state:
                    rutas = get_rutas()
                    ruta_normales = rutas['normales']
                    json_recetas_normales = cargar_datos(ruta_normales)

                    if 'recetas_normales' not in st.session_state:
                        # Se crea un objeto para almacenar las recetas
                        print("no estaba la receta")
                        obj_recetas_normales = {}
                        for receta_normal in json_recetas_normales:
                            if receta_normal["id"] not in obj_recetas_normales:
                                obj_recetas_normales[receta_normal["id"]] = receta_normal
                            else:
                                print("Ya estaba la receta con id",receta_normal["id"])
                        st.session_state['recetas_normales'] = obj_recetas_normales

                        if 'recetas' not in st.session_state:
                            st.session_state['recetas'] = obj_recetas_normales
                        else:
                            st.session_state['recetas'].update(obj_recetas_normales)
            else:
                recetas = session_state.recetas

            recetas_favoritas = {}
            for receta in ids_favoritas:

                if
                recetas_favoritas[receta]

        if (recetas_favoritas is None or recetas_favoritas == [] or
            len(recetas_favoritas)<1):
            st.title("User doesn't have any favorite recipes yet.")

def validar_credenciales(username, password):
    """
    Valida las credenciales del usuario con los usuarios
    almacenados en la base de datos.

    Parameters:
    - username (str): Nombre de usuario proporcionado.
    - password (str): Contraseña proporcionada.

    Returns:
    - bool: True si las credenciales son válidas,
      False de lo contrario.
    """
    usuarios = db.fetch()
    for usuario in usuarios.items:
        if usuario['username'] == username and usuario['password'] == password:
            return usuario
    return False