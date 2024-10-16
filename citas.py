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
    
    st.title("Peluquería Alcaraz & Son")
    st.write('Aquí puedes escoger una cita.')

    # Ejemplo básico de formulario para escoger citas
    with st.form(key='citas_form'):
        nombre = st.text_input('Nombre')
        email = st.text_input('Email')
        fecha = st.date_input('Fecha')
        tipo_de_corte = st.selectbox('Tipo de corte', ['Corte', 'Corte y barba', 'Barba'])
        comentarios = st.text_area('Comentarios')
        submit_button = st.form_submit_button(label='Reservar')

        if submit_button:
            st.success(f'Cita reservada para {nombre} el {fecha}.')

if __name__ == "__main__":
    main()

