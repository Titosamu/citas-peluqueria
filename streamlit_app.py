import streamlit as st
import home
import citas

# Inicializar la variable de estado para la página
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Función para cargar la página correcta
def load_page(page):
    if page == 'home':
        home.main()
    elif page == 'citas':
        citas.main()

# Cargar la página actual
load_page(st.session_state['page'])
