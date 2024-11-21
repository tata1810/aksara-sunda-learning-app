import yaml
import streamlit as st
import streamlit_authenticator as stauth

from PIL import Image
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title='Review Tingkat 2',
    layout='centered',
    initial_sidebar_state='collapsed'
)

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

if not st.session_state.authentication_status:
    st.warning("Belum log in, tidak memiliki akses")
    if st.button("Log in"):
        switch_page("home")
    st.stop()


questions = [
    {
        "question": "Manakah yang merupakan karakter rarangken-eu?",
        "image_options": {
            "a": "assets/rarangken-u.jpg",
            "b": "assets/rarangken-i.jpg",
            "c": "assets/rarangken-o.jpg",
            "d": "assets/rarangken-eu.jpg"
        },
        "answer": "d"
    },
    {
        "question": "Karakter aksara Sunda apakah ini?",
        "image": "assets/rarangken-i.jpg",
        "options": ["rarangken-e", "rarangken-i", "rarangken-u", "rarangken-o"],
        "answer": "rarangken-i"
    },
    {
        "question": "Karakter aksara Sunda apakah ini? (contoh penulisan : rarangken-e)",
        "image": "assets/rarangken-o.jpg",
        "answer": "rarangken-o"
    },
    {
        "question": "Manakah yang merupakan karakter rarangken-ya?",
        "image_options": {
            "a": "assets/rarangken-eu.jpg",
            "b": "assets/rarangken-u.jpg",
            "c": "assets/rarangken-ya.jpg",
            "d": "assets/rarangken-ra.jpg"
        },
        "answer": "c"
    },
    {
        "question": "Karakter aksara Sunda apakah ini? (contoh penulisan : rarangken-e)",
        "image": "assets/rarangken-e.jpg",
        "answer": "rarangken-e"
    },
    {
        "question": "Karakter aksara Sunda apakah ini? (contoh penulisan : rarangken-e)",
        "image": "assets/rarangken-ra.jpg",
        "options": ["rarangken-r", "rarangken-h", "rarangken-ra", "rarangken-i"],
        "answer": "rarangken-ra"
    },
    {
        "question": "Manakah yang merupakan karakter rarangken-u?",
        "image_options": {
            "a": "assets/rarangken-o.jpg",
            "b": "assets/rarangken-u.jpg",
            "c": "assets/rarangken-eu.jpg",
            "d": "assets/rarangken-e.jpg"
        },
        "answer": "b"
    },
    {
        "question": "Karakter aksara Sunda apakah ini? (contoh penulisan : rarangken-e)",
        "image": "assets/rarangken-eu.jpg",
        "answer": "rarangken-eu"
    },
    {
        "question": "Manakah yang merupakan karakter 'ngra'?",
        "image_options": {
            "a": "assets/gar.jpg",
            "b": "assets/ngra.jpg",
            "c": "assets/gra.jpg",
            "d": "assets/ngar.jpg"
        },
        "answer": "b"
    },
    {
        "question": "Kata aksara Sunda apakah yang ditulis (contoh penulisan : ha)",
        "image": "assets/geu.jpg",
        "answer": "geu"
    },
    {
        "question": "Karakter aksara Sunda apakah ini?",
        "image": "assets/mo.jpg",
        "answer": "mo"
    },
    {
        "question": "Manakah yang merupakan karakter 'lé'?",
        "image_options": {
            "a": "assets/lo.jpg",
            "b": "assets/la.jpg",
            "c": "assets/lee.jpg",
            "d": "assets/l.jpg"
        },
        "answer": "c"
    },
    {
        "question": "Karakter aksara Sunda apakah ini? (contoh penulisan: ha)",
        "image": "assets/ke.jpg",
        "answer": "ke"
    },
    {
        "question": "Karakter aksara Sunda apakah ini? (contoh penulisan: ha)",
        "image": "assets/tya.jpg",
        "answer": "tya"
    },
    {
        "question": "Karakter aksara Sunda apakah ini? (contoh penulisan: ha)",
        "image": "assets/d.jpg",
        "answer": "d"
    }
]

if 'review2' not in st.session_state:
    st.session_state.review2 = 0
if 'current_question2' not in st.session_state:
    st.session_state.current_question2 = 0

if st.button(label='Kembali'):
    switch_page('index')
st.header('Review Tingkat 2')

with st.container():
    st.write(f'Jawaban Benar: {st.session_state.review2}')
    if st.session_state.current_question2 < len(questions):
        q = questions[st.session_state.current_question2]
        st.subheader(f'Pertanyaan {st.session_state.current_question2 + 1}')
        st.write(q['question'])

        if 'image' in q:
            st.image(q['image'], width=150)

        if "image_options" in q:
            columns = st.columns(4)
            option_labels = []
            for idx, (label, img_path) in enumerate(q["image_options"].items()):
                col = columns[idx % 4]  

                with col:
                    img = Image.open(img_path)
                    img = img.resize((200, 200))  
                    st.image(img, caption=label, width = 20, use_container_width=True)  
                    option_labels.append(label)
                
        if 'options' in q:
            user_answer = st.radio('Pilih jawaban:', q['options'], key=f'q{st.session_state.current_question2}')
        else:
            user_answer = st.text_input('Masukan jawaban:', key=f'q{st.session_state.current_question2}')

        prev_soal, next_soal = st.columns(2)
        if st.button(label='Jawab', type='primary', use_container_width=True):
            if user_answer.lower() == q['answer'].lower():
                st.session_state.review2 += 1
            st.session_state.current_question2 += 1
            st.rerun()
    else:
        st.success('Review Tingkat 2 Selesai')
        if st.button(label='Kembali', icon='👉🏼'):
            st.session_state.review2 = 0
            st.session_state.current_question2 = 0 
            switch_page('index')