import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title='Home',
    page_icon='🏠',
    initial_sidebar_state='collapsed',
    layout='centered'
)

for key in st.session_state.keys():
    del st.session_state[key]

st.markdown("""
            # 👋🏻 **Wilujeung Sumping di Pembelajaran Aksara Sunda**
            ##### Silahkan sign up atau log in jika sudah memiliki akun
            ---
            """)

signup, login = st.columns(2)
if signup.button(label='Belum punya akun', type='primary', use_container_width=True):
    switch_page('signup')
    
if login.button(label='Sudah ada akun', use_container_width=True):
    switch_page('index')