import yaml
import streamlit as st
import streamlit_authenticator as stauth

from PIL import Image
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title='Review Tingkat 1',
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

# Restrict access if not authenticated
if not st.session_state.authentication_status:
    st.warning("Belum log in, tidak memiliki akses")
    if st.button("Log in"):
        switch_page("home")
    st.stop()


questions = [
    {
        "question": "Karakter aksara sunda apakah ini?",
        "image": "assets/ga.jpg",
        "options": ["ngalagena-ga", "swara-i", "rarangken-i", "ngalagena-nga"],
        "answer": "ngalagena-ga"
    },
    {
        "question": "Manakah yang merupakan karakter ngalagena-ma?",
        "image_options": {
            "a": "assets/ga.jpg",
            "b": "assets/wa.jpg",
            "c": "assets/ma.jpg",
            "d": "assets/a.jpg"
        },
        "answer": "c"
    },
    {
        "question": "Karakter aksara sunda apakah ini?",
        "image": "assets/xa.jpg",
        "options": ["ngalagena-ma", "ngalagena-xa", "ngalagena-ba", "ngalagena-ka"],
        "answer": "ngalagena-xa"
    },
    {
        "question": "Karakter aksara sunda apakah ini? (contoh penulisan : swara-a)",
        "image": "assets/ya.jpg",
        "answer": "ngalagena-ya"
    },
    {
        "question": "Manakah yang merupakan karakter ngalagena-fa?",
        "image_options": {
            "a": "assets/ha.jpg",
            "b": "assets/fa.jpg",
            "c": "assets/pa.jpg",
            "d": "assets/ma.jpg"
        },
        "answer": "b"
    },
    {
        "question": "Karakter aksara sunda apakah ini? (contoh penulisan : swara-a)",
        "image": "assets/va.jpg",
        "answer": "ngalagena-va"
    },
    {
        "question": "Karakter aksara sunda apakah ini?",
        "image": "assets/u.jpg",
        "options": ["swara-u", "swara-i", "rarangken-u", "ngalagena-nga"],
        "answer": "swara-u"
    },
    {
        "question": "Karakter aksara sunda apakah ini? (contoh penulisan : swara-a)",
        "image": "assets/e.jpg",
        "answer": "swara-e"
    },
    {
        "question": "Manakah yang merupakan karakter ngalagena-za?",
        "image_options": {
            "a": "assets/o.jpg",
            "b": "assets/ga.jpg",
            "c": "assets/nga.jpg",
            "d": "assets/za.jpg"
        },
        "answer": "d"
    },
    {
        "question": "Karakter aksara sunda apakah ini?",
        "image": "assets/sa.jpg",
        "options": ["ngalagena-ra", "swara-e", "rarangken-ya", "ngalagena-sa"],
        "answer": "ngalagena-sa"
    },
    {
        "question": "Karakter aksara sunda apakah ini?",
        "image": "assets/wa.jpg",
        "options": ["ngalagena-ga", "swara-u", "ngalagena-wa", "ngalagena-fa"],
        "answer": "ngalagena-wa"
    },
    {
        "question": "Manakah yang merupakan karakter swara-u?",
        "image_options": {
            "a": "assets/za.jpg",
            "b": "assets/u.jpg",
            "c": "assets/i.jpg",
            "d": "assets/nga.jpg"
        },
        "answer": "b"
    },
    {
        "question": "Karakter Aksara Sunda apakah ini? (contoh penulisan : swara-a)",
        "image": "assets/nga.jpg",
        "answer": "ngalagena-nga"
    },
    {
        "question": "Manakah yang merupakan karakter Rarangken-ka?",
        "image_options": {
            "a": "assets/ka.jpg",
            "b": "assets/sa.jpg",
            "c": "assets/ra.jpg",
            "d": "assets/xa.jpg"
        },
        "answer": "a"
    },
    {
        "question": "Manakah yang merupakan karakter Rarangken-da?",
        "image_options": {
            "a": "assets/ja.jpg",
            "b": "assets/ba.jpg",
            "c": "assets/nya.jpg",
            "d": "assets/da.jpg"
        },
        "answer": "d"
    }
]

authenticator.logout()
st.header('Review Tingkat 1')

with st.container():
    if st.session_state.current_question < len(questions):
        q = questions[st.session_state.current_question]
        st.subheader(f'Pertanyaan {st.session_state.current_question + 1}')
        st.write(q['question'])

        if 'image' in q:
            st.image(q['image'], width=150)

        if "image_options" in q:
            columns = st.columns(4)
            option_labels = []
            for idx, (label, img_path) in enumerate(q["image_options"].items()):
                col = columns[idx % 4]  # Alternate between the two columns

                # Display the image in the appropriate column
                with col:
                    img = Image.open(img_path)
                    img = img.resize((200, 200))  # Resize image to a uniform size
                    st.image(img, caption=label, width = 20, use_column_width=True)  # Ensures images are responsive and fit in the columns
                    option_labels.append(label)
                
        if 'options' in q:
            user_answer = st.radio('Pilih jawaban:', q['options'], key=f'q{st.session_state.current_question}')
        else:
            user_answer = st.text_input('Masukan jawaban:', key=f'q{st.session_state.current_question}')

        prev_soal, next_soal = st.columns(2)
        if st.button(label='Jawab', type='primary', use_container_width=True):
            if user_answer.lower() == q['answer'].lower():
                st.success('jawaban benar')
            else:
                st.error('jawaban salah')
            st.session_state.current_question += 1
            st.rerun()
    else:
        st.session_state.current_question = 0 
        switch_page('index')