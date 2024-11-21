import yaml
import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title='POSTTEST',
    layout='centered',
    initial_sidebar_state='collapsed'
)

with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

def get_posttest_taken(config, username):
    if 'posttest_taken' not in st.session_state:
        st.session_state.posttest_taken = config['credentials']['usernames'][username]['posttest_taken']
    return st.session_state.posttest_taken

if not st.session_state.authentication_status:
    st.warning("Belum log in, tidak memiliki akses")
    if st.button("Log in"):
        switch_page("home")
    st.stop()

if get_posttest_taken(config, st.session_state.username) is False and not st.session_state.level3_passed:
    st.error("Tingkat Latihan belum dikerjakan semua!")
    if st.button("Kembali"):
        switch_page("index")

elif st.session_state.posttest_taken:
    st.write(f'Skor Anda: {st.session_state.posttest_score}')
    st.error("Post Test selesai dikerjakan, tidak bisa mengulang!")
    if st.button("Kembali"):
        switch_page("index")
    st.stop()

else:
    questions = [
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: satukata)",
            "image": "assets/diajar.jpg",
            "answer": "diajar"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: dua kata)",
            "image": "assets/aksarasunda.jpg",
            "answer": "aksara sunda"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: dua kata)",
            "image": "assets/asikkalintang.jpg",
            "answer": "asik kalintang"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: satukata)",
            "image": "assets/atikan.jpg",
            "answer": "atikan"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: dua kata)",
            "image": "assets/ujipangabisa.jpg",
            "answer": "uji pangabisa"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: satukata)",
            "image": "assets/aplikasi.jpg",
            "answer": "aplikasi"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: satukata)",
            "image": "assets/maraneh.jpg",
            "answer": "maraneh"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: dua kata)",
            "image": "assets/wawasandunya.jpg",
            "answer": "wawasan dunya"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: dua kata)",
            "image": "assets/nalikatradisional.jpg",
            "answer": "nalika tradisional"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: satukata)",
            "image": "assets/nyerat.jpg",
            "answer": "nyerat"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: dua kata)",
            "image": "assets/bangsaindonesia.jpg",
            "answer": "bangsa indonesia"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: dua kata)",
            "image": "assets/asaltanagi.jpg",
            "answer": "asal tanagi"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: satukata)",
            "image": "assets/urang.jpg",
            "answer": "urang"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: dua kata)",
            "image": "assets/resepeksplorasi.jpg",
            "answer": "resep eksplorasi"
        },
        {
            "question": "Gambar tersebut dapat dibaca sebagai? (contoh penulisan: satukata)",
            "image": "assets/maos.jpg",
            "answer": "maos"
        }
    ]

    if 'posttest_score' not in st.session_state:
        st.session_state.posttest_score = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    st.header('Post Test Aksara Sunda')

    with st.container():
        if st.session_state.current_question < len(questions):
            if st.button(label='⚠️ Lihat Pitunjuk Pengerjaan Sebelum Mengerjakan Soal', type='secondary', use_container_width=False):
                @st.dialog("🛠️ Pitunjuk Pengerjaan")
                def help():
                    st.subheader('💬 Pitunjuk Post Test')
                    st.text("- Pre Test terdiri dari 15 soal\n- Pastikan jawaban anda benar karena tidak dapat\nkembali ke soal berikutnya.\n- Ikuti petunjuk contoh penulisan jawaban\n")

                if "help" not in st.session_state:
                    help()

            q = questions[st.session_state.current_question]
            st.subheader(f'Pertanyaan {st.session_state.current_question + 1}')
            st.write(q['question'])

            if 'image' in q:
                st.image(q['image'])

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
                user_answer = st.radio('Pilih jawaban:', q['options'], key=f'q{st.session_state.current_question}')
            else:
                user_answer = st.text_input('Masukan jawaban:', key=f'q{st.session_state.current_question}')
            prev_soal, next_soal = st.columns(2)

            if st.button(label='Jawab', type='primary', use_container_width=True):
                if user_answer.lower() == q['answer'].lower():
                    st.session_state.posttest_score += 1

                st.session_state.current_question += 1
                st.rerun()
        else:
            st.success('Post Test Lengkep! (Post Test Selesai)')
            st.write(f'Skor Anda: {st.session_state.posttest_score}')

            if st.button(label='Kembali', icon='📚', type='primary'):
                config['credentials']['usernames'][st.session_state.username]['posttest'] = st.session_state.posttest_score
                config['credentials']['usernames'][st.session_state.username]['posttest_taken'] = True

                st.session_state.posttest_taken = True

                with open('config.yaml', 'w', encoding='utf-8') as file:
                    yaml.dump(config, file, default_flow_style=False)

                switch_page('index')
        