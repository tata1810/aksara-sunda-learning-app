import yaml
import streamlit as st
import streamlit_authenticator as stauth

from PIL import Image
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title='LEVEL 3',
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
    if st.button("Log in"):
        switch_page("home")
    st.stop()

# if 'level3_passed' not in st.session_state:
if st.session_state.level3_passed:
    st.error("Level ini sudah selesai dikerjakan, silahkan lanjut ke level berikutnya")
    if st.button("Kembali"):
        switch_page("index")
    st.stop()
else:
    questions = [
        {
            "question": "Karakter aksara sunda apakah ini?",
            "image": "assets/ga.png",
            "options": ["ngalagena-ga", "swara-i", "rarangken-i", "ngalagena-nga"],
            "answer": "ngalagena-ga"
        },
        {
            "question": "Manakah yang merupakan karakter ngalagena-ma?",
            "image_options": {
                "a": "assets/ga.png",
                "b": "assets/wa.png",
                "c": "assets/ma.png",
                "d": "assets/a.png"
            },
            "answer": "c"
        },
        {
            "question": "Karakter aksara sunda apakah ini?",
            "image": "assets/xa.png",
            "options": ["ngalagena-ma", "ngalagena-xa", "ngalagena-ba", "ngalagena-ka"],
            "answer": "ngalagena-xa"
        },
        {
            "question": "Karakter aksara sunda apakah ini? (contoh penulisan : swara-a)",
            "image": "assets/ya.png",
            "answer": "ngalagena-ya"
        },
        {
            "question": "Manakah yang merupakan karakter ngalagena-fa?",
            "image_options": {
                "a": "assets/ha.png",
                "b": "assets/fa.png",
                "c": "assets/pa.png",
                "d": "assets/ma.png"
            },
            "answer": "b"
        },
        {
            "question": "Karakter aksara sunda apakah ini? (contoh penulisan : swara-a)",
            "image": "assets/va.png",
            "answer": "ngalagena-va"
        },
        {
            "question": "Karakter aksara sunda apakah ini?",
            "image": "assets/u.png",
            "options": ["swara-u", "swara-i", "rarangken-u", "ngalagena-nga"],
            "answer": "swara-u"
        },
        {
            "question": "Karakter aksara sunda apakah ini? (contoh penulisan : swara-a)",
            "image": "assets/e.png",
            "answer": "swara-e"
        },
        {
            "question": "Manakah yang merupakan karakter ngalagena-za?",
            "image_options": {
                "a": "assets/o.png",
                "b": "assets/ga.png",
                "c": "assets/nga.png",
                "d": "assets/za.png"
            },
            "answer": "d"
        },
        {
            "question": "Karakter aksara sunda apakah ini?",
            "image": "assets/sa.png",
            "options": ["ngalagena-ra", "swara-e", "rarangken-ya", "ngalagena-sa"],
            "answer": "ngalagena-sa"
        },
        {
            "question": "Karakter aksara sunda apakah ini?",
            "image": "assets/wa.png",
            "options": ["ngalagena-ga", "swara-u", "ngalagena-wa", "ngalagena-fa"],
            "answer": "ngalagena-wa"
        },
        {
            "question": "Manakah yang merupakan karakter swara-u?",
            "image_options": {
                "a": "assets/za.png",
                "b": "assets/u.png",
                "c": "assets/i.png",
                "d": "assets/nga.png"
            },
            "answer": "b"
        },
        {
            "question": "Karakter Aksara Sunda apakah ini? (contoh penulisan : swara-a)",
            "image": "assets/nga.png",
            "answer": "ngalagena-nga"
        },
        {
            "question": "Manakah yang merupakan karakter Rarangken-ka?",
            "image_options": {
                "a": "assets/ka.png",
                "b": "assets/sa.png",
                "c": "assets/ra.png",
                "d": "assets/xa.png"
            },
            "answer": "c"
        },
        {
            "question": "Manakah yang merupakan karakter Rarangken-da?",
            "image_options": {
                "a": "assets/ja.png",
                "b": "assets/ba.png",
                "c": "assets/nya.png",
                "d": "assets/da.png"
            },
            "answer": "d"
        }
    ]

    if 'level3_score' not in st.session_state:
        st.session_state.level3_score = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    authenticator.logout()
    st.header('Level 3')

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
                        st.image(img, caption=label, width=20, use_column_width=True)  # Ensures images are responsive and fit in the columns
                        option_labels.append(label)
                    
            if 'options' in q:
                user_answer = st.radio('Pilih jawaban:', q['options'], key=f'q{st.session_state.current_question}')
            else:
                user_answer = st.text_input('Masukan jawaban:', key=f'q{st.session_state.current_question}')

            prev_soal, next_soal = st.columns(2)

            if st.session_state.current_question < len(questions) - 1:
                st.warning('Tidak dapat kembali ke soal berikutnya, harap dikerjakan dengan baik sesuai instruksi')

            if st.button(label='Jawab', type='primary', use_container_width=True):
                if user_answer.lower() == q['answer'].lower():
                    st.session_state.level3_score += 1
                    st.success('jawaban benar')
                else:
                    st.error('jawaban salah')
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.session_state.level3_score < 10:
                st.error('Nilai anda belum cukup untuk mengambil post-test, silahkan mengulang. Semangat 💪')
                st.write(f'Skor Anda: {st.session_state.level3_score}')
                if st.button(label='Kembali', icon='👉🏼'):
                    st.session_state.level3_score = 0
                    st.session_state.current_question = 0
                    switch_page('index')
                if st.button(label='Ambil Tes', icon='👉🏼'):
                    st.session_state.level3_score = 0
                    st.session_state.current_question = 0

            elif st.session_state.level3_score >= 10 and st.session_state.level3_score <15:
                st.warning('Level 3 selesai, anda bisa menyempurnakan nilai sekarang atau lanjut ke post-test')
                st.write(f'Skor Anda: {st.session_state.level3_score}')
                if st.button(label='Kembali', icon='👉🏼'):
                    config['credentials']['usernames'][st.session_state.username]['level3'] = st.session_state.level3_score
                    config['credentials']['usernames'][st.session_state.username]['level3_passed'] = True
                    st.session_state.level3_passed = True
                    
                    with open('config.yaml', 'w', encoding='utf-8') as file:
                        yaml.dump(config, file, default_flow_style=False)    
                    
                    switch_page('index')
                if st.button(label='Mau mengulang', icon='👉🏼'):
                    st.session_state.level3_score = 0
                    st.session_state.current_question = 0
            else:
                st.success('Level 3 selesai dengan nilai sempurna 🎉')
                st.write(f'Skor Anda: {st.session_state.level3_score}')
                if st.button(label='Kembali', icon='👉🏼'):
                    config['credentials']['usernames'][st.session_state.username]['level3'] = st.session_state.level3_score
                    config['credentials']['usernames'][st.session_state.username]['level3_passed'] = True
                    st.session_state.level3_passed = True

                    with open('config.yaml', 'w', encoding='utf-8') as file:
                        yaml.dump(config, file, default_flow_style=False) 

                    switch_page('index')