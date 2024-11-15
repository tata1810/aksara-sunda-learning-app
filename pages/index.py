import yaml
import traceback
import streamlit as st
import streamlit_authenticator as stauth

from PIL import Image
from gtts import gTTS
from io import BytesIO
from yaml.loader import SafeLoader
from backend.combined import CombinedModels
from streamlit_authenticator.utilities import LoginError
from streamlit_extras.switch_page_button import switch_page

def main():
    st.title(f'Wilujeng Sumping {st.session_state["username"]}!')
    belajar, latihan, transliterasi, tts = st.tabs(['📚 Diajar','🧐 Latihan', '📖 Konversi', '📜 Dengekeun'])

    # Bagian Latihan
    levels = latihan.columns(3)
    with levels[0].container():
        st.image('assets/a.jpg', use_column_width=True)
        if st.button(label='Tingkat 1', type='primary',use_container_width=True):
            if not get_level1(config, st.session_state.username):
                switch_page('level1')
            else:
                st.warning('''
                           Tingkat 1 atos rengse dipigawe,mangga teras ka level 2

                           (Level 1 sudah selesai dikerjakan, silahkan lanjut ke level 2)
                           ''')

    with levels[1].container():
        st.image('assets/a.jpg', use_column_width=True)
        if st.button(label='Tingkat 2', type='primary', use_container_width=True):
            if get_level1(config, st.session_state.username):
                if not get_level2(config, st.session_state.username):
                    switch_page('level2')
                else:
                    st.warning('''
                               Tingkat 2 atos rengse dipigawe,mangga teras ka level 3
                               
                               (Level 2 sudah selesai dikerjakan, silahkan lanjut ke level 3)
                               ''')
            else:
                st.warning('''
                           Tingkat kawitna tacan dipigawe
                           
                           (Level sebelumnya belum dikerjakan)
                           ''')

    with levels[2].container():
        st.image('assets/a.jpg', use_column_width=True)
        if st.button(label='Tingkat 3', type='primary', use_container_width=True):
            if get_level2(config, st.session_state.username):
                if not get_level3(config, st.session_state.username):
                    switch_page('level3')
                else:
                    st.warning('''
                               Tingkat 3 atos rengse dipigawe,mangga ngagawekeun tes ahir
                               
                               (Level 3 sudah selesai dikerjakan, silahkan mengerjakan post-test)
                               ''')
            else:
                st.warning('''
                           Tingkat kawitna tacan dipigawe
                           
                           (Level sebelumnya belum dikerjakan)
                           ''')


    # Bagian Transliterasi
    with transliterasi.form('transliterasi_form', clear_on_submit=True):
        uploaded_image = st.file_uploader(
            'Mangga upload gambar ...', type=['jpg', 'png', 'jpeg']
        )

        submit, clear, _, _ = st.columns(4)
        submit.form_submit_button(label='Transliterasi', use_container_width=True, type='primary')
        clear.form_submit_button(label='Clear', use_container_width=True)

    if uploaded_image:
        try:
            input_path = uploaded_image.name
            file_binary = uploaded_image.read()
            with open(input_path, 'wb') as temp_file:
                temp_file.write(file_binary)

            image = Image.open(uploaded_image)
            transliterasi.image(image, caption=input_path, use_column_width=True)

            # if transliterasi.button(label='Konversi', type='primary', use_container_width=True):
            model = transliterate_model()
            with st.spinner('Nuju memproses gambar ...'):
                results = model.process_image(input_path)

            if results:
                transliterasi.success('Konversi junun (Konversi berhasil)!')
                transliterasi.markdown(f'''
                                        ##### Kenging konversi / (Hasil transliterasi):

                                        ## {results}
                                        ''')

                gtts = gTTS(text=results, lang='su', tld='co.id')
                audio_stream = BytesIO()
                gtts.write_to_fp(audio_stream)

                if transliterasi.button(label='Dengekeun', icon='📣'):
                    transliterasi.audio(audio_stream, autoplay=True)
            else:
                transliterasi.error('''Konversi gagal! Mangga cobi deui
                                    
                                    (Transliterasi Gagal! Silahkan coba lagi)
                                    ''')
        except Exception as e:
            st.error(f'Error: {traceback.format_exc}, \n {e}')

    # Bagian Text-to-Speech menggunakan aksen sunda
    tts.title('Dengekeun')
    text_input = tts.text_area('Asupkeun teks')

    if tts.button(label='Dengekeun', icon='📢'):
        if text_input:
            gtts = gTTS(text=text_input, lang='su', tld='co.id')
            audio_stream = BytesIO()

            gtts.write_to_fp(audio_stream)
            tts.audio(audio_stream)
        else:
            tts.error('''Tulung asupkeun teks
                      
                      (Tolong masukan teks)''')

            
def transliterate_model():
    try:
        yolo_path = '/Users/gataa/University/SKRIPSI/code/models_yolo/new/weights/best.pt'
        effnet_path = '/Users/gataa/University/SKRIPSI/code/models/model_new_efficientnet_v2_995_991.h5'

        return CombinedModels(yolo_path=yolo_path, effnet_path=effnet_path)
    except Exception as e:
        st.error(f'error load model {str(e)}')
        return None
    

def get_pretest(config, username):
    if 'pretest' not in st.session_state:
        st.session_state.pretest = config['credentials']['usernames'][username]['pretest']
    return st.session_state.pretest

def get_pretest_taken(config, username):
    if 'pretest_taken' not in st.session_state:
        st.session_state.pretest_taken = config['credentials']['usernames'][username]['pretest_taken']
    return st.session_state.pretest_taken

def get_level1(config, username):
    if 'level1_passed' not in st.session_state:
        st.session_state.level1_passed = config['credentials']['usernames'][username]['level1_passed']
    return st.session_state.level1_passed

def get_level2(config, username):
    if 'level2_passed' not in st.session_state:
        st.session_state.level2_passed = config['credentials']['usernames'][username]['level2_passed']
    return st.session_state.level2_passed

def get_level3(config, username):
    if 'level3_passed' not in st.session_state:
        st.session_state.level3_passed = config['credentials']['usernames'][username]['level3_passed']
    return st.session_state.level3_passed

############################################################################################
############################################################################################


# Application
if __name__ == '__main__':
    st.write(st.session_state)

    # Loading config file
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.load(file, Loader=SafeLoader)
        
    # Creating the authenticator object
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    try:
        authenticator.login()
    except LoginError as e:
        st.error(e)

    # Authenticating user
    if st.session_state['authentication_status']:
        get_pretest(config, st.session_state['username'])

        if not get_pretest_taken(config, st.session_state.username):
            switch_page('pretest')

        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)

        if authenticator.logout(location='main'):
            config['credentials']['usernames'][st.session_state.username]['logged_in'] = False
        main()

    elif st.session_state['authentication_status'] is False:
        st.error('''
                Ngaran pamaké/sandi salah!
                 
                (Username/password salah)
                 ''')
        st.markdown(f'**Hint: {st.session_state.password_hint}**')

    elif st.session_state['authentication_status'] is None:
        st.warning('''
                   Mangga eusian ngaran pamaké sarta sandi anjeun!
                   
                   (Silahkan isi username dan password anda)
                   ''')
        signup, home, _= st.columns(3)
        if signup.button(label='Belum punya akun', use_container_width=True, type='primary'):
            switch_page('signup')

        if home.button(label='Kembali', use_container_width=True):
            switch_page('home')
