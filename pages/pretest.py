import yaml
import streamlit as st
import streamlit_authenticator as stauth

from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title='PRETEST',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.write(st.session_state)

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
    if st.button("log in"):
        switch_page("home")
    st.stop()

if st.session_state.pretest_taken:
    st.error("Pre-test selesai dikerjakan, tidak bisa mengulang!")
    if st.button("Kembali"):
        switch_page("index")
    st.stop()

questions = [
    {
        "question": "Buah apakah ini?",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg",
        "options": ["Apel", "Pisang", "Mangga"],
        "answer": "Apel"
    },
    {
        "question": "Warna apa yang ada pada pisang?",
        "options": ["Hijau", "Kuning", "Merah"],
        "answer": "Kuning"
    },
    {
        "question": "Berapa jumlah jari pada tangan manusia normal?",
        "options": ["3", "5", "7"],
        "answer": "5"
    },
    {
        "question": "Berapakah hasil dari 5 + 4?",
        "answer": "9"
    }
]


if 'pretest_score' not in st.session_state:
    st.session_state.pretest_score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

authenticator.logout()
st.header('Pre Test Aksara Sunda')

with st.container(height=450, border=False):
    if st.session_state.current_question < len(questions) - 1:
        st.warning('Tidak dapat kembali ke soal berikutnya, harap dikerjakan dengan baik sesuai instruksi!')
        q = questions[st.session_state.current_question]
        st.subheader(f'Pertanyaan {st.session_state.current_question + 1}')
        st.write(q['question'])

        if 'image' in q:
            st.image(q['image'], width=100)

        if 'options' in q:
            user_answer = st.radio('Pilih jawaban:', q['options'], key=f'q{st.session_state.current_question}')
        else:
            user_answer = st.text_input('Masukan jawaban:', key=f'q{st.session_state.current_question}')

        prev_soal, next_soal = st.columns(2)

        if st.button(label='Jawab', type='primary', use_container_width=True):
            if user_answer.lower() == q['answer'].lower():
                st.session_state.pretest_score += 1

            st.session_state.current_question += 1
            st.rerun()
    else:
        st.success('Pre Test Selesai!')
        st.write(f'Skor Anda: {st.session_state.pretest_score}')

        if st.button(label='Lanjut', icon='👉🏼', type='primary'):
            # Save Pretest score
            config['credentials']['usernames'][st.session_state.username]['pretest'] = st.session_state.pretest_score
            config['credentials']['usernames'][st.session_state.username]['pretest_taken'] = True

            st.session_state.pretest_taken = True

            with open('config.yaml', 'w', encoding='utf-8') as file:
                yaml.dump(config, file, default_flow_style=False)

            switch_page('index')
    