import streamlit as st

def main():
    # Fondo de pantalla JPG
    page_bg_img = '''
    <style>
    body {
        background-image: url("images/fondo.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

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


    # Agregar el mapa de Google Maps
    st.markdown(
        """
        <h2 style='text-align: center;'>Encuéntranos aquí:</h2>
        <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3127.923467676142!2d-0.49335172408821404!3d38.37389187184051!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd62374a634fad5d%3A0xa2d601fed82852d1!2sBarber%20Shop%20Zouhair!5e0!3m2!1ses!2ses!4v1729082694427!5m2!1ses!2ses" 
        width="600" 
        height="450" 
        style="border:0;" 
        allowfullscreen="" 
        loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade"></iframe>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()




