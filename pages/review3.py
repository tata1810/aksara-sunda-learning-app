import yaml
import streamlit as st
import streamlit_authenticator as stauth

from PIL import Image
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title='Review Tingkat 3',
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
        "question": "Gambar tersebut merupakan karakter untuk kata apa? (format jawaban: 'tulis jawaban')",
        "image": "assets/sunda.jpg",
        "answer": "sunda"
    },
    {
        "question": "Manakah yang merupakan karakter untuk kata 'bandung'? (format jawaban: a/b/c/d)",
        "image_options": {
            "a": "assets/bandung.jpg",
            "b": "assets/banadung.jpg",
            "c": "assets/bangadung.jpg",
            "d": "assets/boladung.jpg"
        },
        "answer": "a"
    },
    {
        "question": "Karakter pada gambar tersebut untuk kata apa? (format jawaban: 'tulis jawaban')",
        "image": "assets/dayeuh.jpg",
        "answer": "dayeuh"
    },
    {
        "question": "Gambar di bawah ini adalah karakter untuk kata? (format jawaban: 'tulis jawaban')",
        "image": "assets/leuweung.jpg",
        "answer": "leuweung"
    },
    {
        "question": "Manakah yang merupakan karakter untuk kata 'kasep'? (format jawaban: a/b/c/d)",
        "image_options": {
            "a": "assets/kasapa.jpg",
            "b": "assets/karep.jpg",
            "c": "assets/kasrep.jpg",
            "d": "assets/kasep.jpg"
        },
        "answer": "d"
    },
    {
        "question": "Gambar di bawah ini adalah karakter untuk kata apa? (format jawaban: 'tulis jawaban')",
        "image": "assets/gunung.jpg",
        "answer": "gunung"
    },
    {
        "question": "Gambar ini menunjukkan karakter untuk kata apa? (format jawaban: 'tulis jawaban')",
        "image": "assets/hya.jpg",
        "answer": "hya"
    },
    {
        "question": "Gambar tersebut adalah karakter untuk kata? (format jawaban: 'tulis jawaban')",
        "image": "assets/siliwangi.jpg",
        "answer": "siliwangi"
    },
    {
        "question": "Karakter pada gambar ini merupakan kata apa? (format jawaban: 'tulis jawaban')",
        "image": "assets/wilujeng.jpg",
        "answer": "wilujeng"
    },
    {
        "question": "Manakah yang merupakan karakter untuk kata 'katre'? (format jawaban: a/b/c/d)",
        "image_options": {
            "a": "assets/sahre.jpg",
            "b": "assets/katre.jpg",
            "c": "assets/lotre.jpg",
            "d": "assets/ratre.jpg"
        },
        "answer": "b"
    },
    {
        "question": "Manakah yang merupakan karakter untuk kata 'naga'? (format jawaban: a/b/c/d)",
        "image_options": {
            "a": "assets/ngaga.jpg",
            "b": "assets/naga.jpg",
            "c": "assets/nanga.jpg",
            "d": "assets/naza.jpg"
        },
        "answer": "b"
    },
    {
        "question": "Gambar di bawah ini adalah karakter untuk kata apa? (format jawaban: 'tulis jawaban')",
        "image": "assets/ciherang.jpg",
        "answer": "ciherang"
    },
    {
        "question": "Gambar ini menunjukkan karakter untuk kata? (format jawaban: 'tulis jawaban')",
        "image": "assets/mangga.jpg",
        "answer": "mangga"
    },
    {
        "question": "Gambar pada soal ini menunjukkan karakter untuk kata? (format jawaban: 'tulis jawaban')",
        "image": "assets/dengekeun.jpg",
        "answer": "dengekeun"
    },
    {
        "question": "Manakah yang merupakan karakter untuk kata 'kremesan'? (format jawaban: a/b/c/d)",
        "image_options": {
            "a": "assets/krameusan.jpg",
            "b": "assets/kermesan.jpg",
            "c": "assets/kremesan.jpg",
            "d": "assets/keumesan.jpg"
        },
        "answer": "c"
    }
]

if 'review3' not in st.session_state:
    st.session_state.review3 = 0
if 'current_question3' not in st.session_state:
    st.session_state.current_question3 = 0

if st.button(label='Kembali'):
    switch_page('index')
st.header('Review Tingkat 3')

with st.container():
    st.write(f'Jawaban Benar: {st.session_state.review3}')
    if st.session_state.current_question3 < len(questions):
        q = questions[st.session_state.current_question3]
        st.subheader(f'Pertanyaan {st.session_state.current_question3 + 1}')
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
            user_answer = st.radio('Pilih jawaban:', q['options'], key=f'q{st.session_state.current_question3}')
        else:
            user_answer = st.text_input('Masukan jawaban:', key=f'q{st.session_state.current_question3}')

        prev_soal, next_soal = st.columns(2)
        if st.button(label='Jawab', type='primary', use_container_width=True):
            if user_answer.lower() == q['answer'].lower():
                st.session_state.review3 += 1
            st.session_state.current_question3 += 1
            st.rerun()
    else:
        st.success('Review Tingkat 3 Selesai')
        if st.button(label='Kembali', icon='👉🏼'):
            st.session_state.review3 = 0
            st.session_state.current_question3 = 0 
            switch_page('index')