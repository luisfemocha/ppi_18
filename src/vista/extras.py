import streamlit as st

import extras

def show_modal(msg):
    # TODO ==> Corregir
    modal_style = """
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    """

    # Contenido del modal
    with st.markdown('<div style="{}">'.format(modal_style), unsafe_allow_html=True):
        with st.container():
            st.write("Alerta")
            st.write("<p>"+msg+"</p>")
            close_button = st.button("Cerrar Modal")

    # Si se hace clic en "Cerrar Modal"
    if close_button:
        # Oculta el modal estableciendo la variable show_modal en False
        show_modal = False