import streamlit as st

def load_styles():
    with open("styles.html", "r") as f:
        styles = f.read()
    return styles

def main():
    # Cargar estilos desde el archivo HTML
    st.markdown(load_styles(), unsafe_allow_html=True)

    st.image("images/logo.jpg", width=800)

    # Título personalizado con HTML y CSS
    st.markdown(
        """
        <h1 style='text-align: center; color: #4CAF50;'>
            Peluquería Alcaraz & Son
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.write('Bienvenido.')

    if st.button('Escoger Citas'):
        st.session_state['page'] = 'citas'

if __name__ == "__main__":
    main()


