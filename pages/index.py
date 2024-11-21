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

st.set_page_config(
    page_title='Index',
    initial_sidebar_state='collapsed',
)

def get_pretest(config, username):
    if 'pretest' not in st.session_state:
        st.session_state.pretest = config['credentials']['usernames'][username]['pretest']
    return st.session_state.pretest

def get_pretest_taken(config, username):
    if 'pretest_taken' not in st.session_state:
        st.session_state.pretest_taken = config['credentials']['usernames'][username]['pretest_taken']
    return st.session_state.pretest_taken

def get_posttest(config, username):
    if 'posttest' not in st.session_state:
        st.session_state.posttest = config['credentials']['usernames'][username]['posttest']
    return st.session_state.posttest

def get_posttest_taken(config, username):
    if 'posttest_taken' not in st.session_state:
        st.session_state.posttest_taken = config['credentials']['usernames'][username]['posttest_taken']
    return st.session_state.posttest_taken

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

def transliterate_model():
    try:
        yolo_path = 'models/best_yolo.pt'
        effnet_path = 'models/effnet.keras'

        return CombinedModels(yolo_path=yolo_path, effnet_path=effnet_path)
    
    except Exception as e:
        st.error(f'error load model {str(e)}')
        return None
    
# =============================================================================================================

def main():
    st.title(f'Wilujeng Sumping {st.session_state["username"]}!')
    belajar, latihan, transliterasi, tts = st.tabs(['📚 Diajar','🧐 Latihan', '📖 Konversi', '📜 Dengekeun'])

    # Bagian Belajar
    st.markdown("""
        <style>
        .justified-text {
            text-align: center;
            text-justify: inter-word;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    with belajar:
        #   INI!!
        st.write(f'Skor Pre Test anda: {get_pretest(config, st.session_state.username)}')
        st.header("Diajar Aksara Sunda (Belajar Aksara Sunda)")
        st.subheader("📖 Aksara Sunda Swara")
        swara1 = belajar.columns(4)
        swara2 = belajar.columns(4)

        st.subheader("📖 Aksara Ngalagena")
        ngalagena1 = belajar.columns(4)
        ngalagena2 = belajar.columns(4)
        ngalagena3 = belajar.columns(4)
        ngalagena4 = belajar.columns(4)
        ngalagena5 = belajar.columns(4)
        ngalagena6 = belajar.columns(4)

        st.subheader("📖 Aksara Rarangken")
        rarangken1 = belajar.columns(4)
        rarangken2 = belajar.columns(4)
        rarangken3 = belajar.columns(4)
        rarangken4 = belajar.columns(4)

        # Aksara Swara
        with swara1[0].container():
                    st.image('assets/a.jpg', use_container_width=True)
                    if st.button(label='Swara - a', type='secondary', use_container_width=True):
                        @st.dialog("Swara - a")
                        def pop():
                            st.write("Ini adalah aksara swara 'a'. Aksara swara - a melambangkan bunyi vokal 'a' seperti dalam kata 'amarah'")
                        if "pop" not in st.session_state:
                            pop()
        with swara1[1].container():
            st.image('assets/i.jpg', use_container_width=True)
            if st.button(label='Swara - i', type='secondary', use_container_width=True):
                @st.dialog("Swara - i")
                def pop():
                    st.write("Ini adalah aksara swara 'i'. Aksara swara - i melambangkan bunyi vokal 'i' seperti dalam kata 'iring'")
                if "pop" not in st.session_state:
                    pop()
        with swara1[2].container():
            st.image('assets/u.jpg', use_container_width=True)
            if st.button(label='Swara - u', type='secondary', use_container_width=True):
                @st.dialog("Swara - u")
                def pop():
                    st.write("Ini adalah aksara swara 'u'. Aksara swara - u melambangkan bunyi vokal 'u' seperti dalam kata 'urang'")
                if "pop" not in st.session_state:
                    pop()
        with swara1[3].container():
            st.image('assets/e.jpg', use_container_width=True)
            if st.button(label='Swara - e', type='secondary', use_container_width=True):
                @st.dialog("Swara - e")
                def pop():
                    st.write("Ini adalah aksara swara 'e'. Aksara swara - e melambangkan bunyi vokal 'e' seperti dalam kata 'ema'")
                if "pop" not in st.session_state:
                    pop()

        with swara2[0].container():
            st.image('assets/o.jpg', use_container_width=True)
            if st.button(label='Swara - o', type='secondary', use_container_width=True):
                @st.dialog("Swara - o")
                def pop():
                    st.write("Ini adalah aksara swara 'o'. Aksara swara - o melambangkan bunyi vokal 'o' seperti dalam kata 'opak'")
                if "pop" not in st.session_state:
                    pop()
        with swara2[1].container():
            st.image('assets/ee.jpg', use_container_width=True)
            if st.button(label='Swara - é', type='secondary', use_container_width=True):
                @st.dialog("Swara - é")
                def pop():
                    st.write("Ini adalah aksara swara 'é'. Aksara swara - é melambangkan bunyi vokal 'é' seperti dalam kata 'épés' (uang)")
                if "pop" not in st.session_state:
                    pop()
        with swara2[2].container():
            st.image('assets/eu.jpg', use_container_width=True)
            if st.button(label='Swara - eu', type='secondary', use_container_width=True):
                @st.dialog("Swara - eu")
                def pop():
                    st.write("Ini adalah aksara swara 'eu'. Aksara swara - eu melambangkan bunyi vokal 'eu' seperti dalam kata 'heureuy' (bercanda)")
                if "pop" not in st.session_state:
                    pop()

        # Aksara Ngalagena
        with ngalagena1[0].container():
            st.image('assets/ba.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ba', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ba")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ba'. Aksara ngalagena - ba merupakan konsonan dasar yang dibaca 'ba' seperti dalam kata 'bapa'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena1[1].container():
            st.image('assets/ca.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ca', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ca")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ca'. Aksara ngalagena - ca merupakan konsonan dasar yang dibaca 'ca' seperti dalam kata 'carita'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena1[2].container():
            st.image('assets/da.jpg', use_container_width=True)
            if st.button(label='Ngalagena - da', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - da")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'da'. Aksara ngalagena - da merupakan konsonan dasar yang dibaca 'da' seperti dalam kata 'dahar'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena1[3].container():
            st.image('assets/fa.jpg', use_container_width=True)
            if st.button(label='Ngalagena - fa', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - fa")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'fa'. Aksara ngalagena - fa merupakan konsonan untuk kata-kata serapan, seperti dalam kata 'fasilitas', 'fakir', atau 'fitrah'.")
                if "pop" not in st.session_state:
                    pop()

        with ngalagena2[0].container():
            st.image('assets/ga.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ga', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ga")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ga'. Aksara ngalagena - ga merupakan konsonan dasar yang dibaca 'ga' seperti dalam kata 'gajah'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena2[1].container():
            st.image('assets/ha.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ha', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ha")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ha'. Aksara ngalagena - ha merupakan konsonan dasar yang dibaca 'ha' seperti dalam kata 'hade'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena2[2].container():
            st.image('assets/ja.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ja', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ja")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ja'. Aksara ngalagena - ja merupakan konsonan dasar yang dibaca 'ja' seperti dalam kata 'jalan'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena2[3].container():
            st.image('assets/ka.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ka', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ka")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ka'. Aksara ngalagena - ka merupakan konsonan dasar yang dibaca 'ka' seperti dalam kata 'kaca'.")
                if "pop" not in st.session_state:
                    pop()

        with ngalagena3[0].container():
            st.image('assets/la.jpg', use_container_width=True)
            if st.button(label='Ngalagena - la', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - la")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'la'. Aksara ngalagena - la merupakan konsonan dasar yang dibaca 'la' seperti dalam kata 'lamun'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena3[1].container():
            st.image('assets/ma.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ma', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ma")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ma'. Aksara ngalagena - ma merupakan konsonan dasar yang dibaca 'ma' seperti dalam kata 'maca'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena3[2].container():
            st.image('assets/na.jpg', use_container_width=True)
            if st.button(label='Ngalagena - na', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - na")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'na'. Aksara ngalagena - na merupakan konsonan dasar yang dibaca 'na' seperti dalam kata 'naon'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena3[3].container():
            st.image('assets/nga.jpg', use_container_width=True)
            if st.button(label='Ngalagena - nga', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - nga")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'nga'. Aksara ngalagena - nga merupakan konsonan dasar yang dibaca 'nga' seperti dalam kata 'ngala'.")
                if "pop" not in st.session_state:
                    pop()

        with ngalagena4[0].container():
            st.image('assets/nya.jpg', use_container_width=True)
            if st.button(label='Ngalagena - nya', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - nya")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'nya'. Aksara ngalagena - nya merupakan konsonan dasar yang dibaca 'nya' seperti dalam kata 'nyata'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena4[1].container():
            st.image('assets/pa.jpg', use_container_width=True)
            if st.button(label='Ngalagena - pa', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - pa")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'pa'. Aksara ngalagena - pa merupakan konsonan dasar yang dibaca 'pa' seperti dalam kata 'pasar'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena4[2].container():
            st.image('assets/qa.jpg', use_container_width=True)
            if st.button(label='Ngalagena - qa', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - qa")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'qa'. Aksara ngalagena - qa merupakan konsonan untuk kata-kata serapan dari bahasa Arab, seperti dalam kata 'quran', 'qolbu', atau 'qasidah'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena4[3].container():
            st.image('assets/ra.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ra', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ra")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ra'. Aksara ngalagena - ra merupakan konsonan dasar yang dibaca 'ra' seperti dalam kata 'rame'.")
                if "pop" not in st.session_state:
                    pop()

        with ngalagena5[0].container():
            st.image('assets/sa.jpg', use_container_width=True)
            if st.button(label='Ngalagena - sa', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - sa")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'sa'. Aksara ngalagena - sa merupakan konsonan dasar yang dibaca 'sa' seperti dalam kata 'saha'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena5[1].container():
            st.image('assets/ta.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ta', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ta")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ta'. Aksara ngalagena - ta merupakan konsonan dasar yang dibaca 'ta' seperti dalam kata 'tadi'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena5[2].container():
            st.image('assets/va.jpg', use_container_width=True)
            if st.button(label='Ngalagena - va', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - va")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'va'. Aksara ngalagena - va merupakan konsonan untuk kata-kata serapan, seperti dalam kata 'vaksin', 'vitamin', atau 'visi'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena5[3].container():
            st.image('assets/wa.jpg', use_container_width=True)
            if st.button(label='Ngalagena - wa', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - wa")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'wa'. Aksara ngalagena - wa merupakan konsonan dasar yang dibaca 'wa' seperti dalam kata 'wani'.")
                if "pop" not in st.session_state:
                    pop()

        with ngalagena6[0].container():
            st.image('assets/xa.jpg', use_container_width=True)
            if st.button(label='Ngalagena - xa', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - xa")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'xa'. Aksara ngalagena - xa merupakan konsonan untuk kata-kata serapan, seperti dalam kata 'xenon', 'xerox', atau 'xilofon'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena6[1].container():
            st.image('assets/ya.jpg', use_container_width=True)
            if st.button(label='Ngalagena - ya', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - ya")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'ya'. Aksara ngalagena - ya merupakan konsonan dasar yang dibaca 'ya' seperti dalam kata 'yakin'.")
                if "pop" not in st.session_state:
                    pop()
        with ngalagena6[2].container():
            st.image('assets/za.jpg', use_container_width=True)
            if st.button(label='Ngalagena - za', type='secondary', use_container_width=True):
                @st.dialog("Ngalagena - za")
                def pop():
                    st.write("Ini adalah aksara ngalagena 'za'. Aksara ngalagena - za merupakan konsonan untuk kata-kata serapan dari bahasa Arab, seperti dalam kata 'zakat', 'ziarah', atau 'zaman'.")
                if "pop" not in st.session_state:
                    pop()

        # Aksara Rarangken
        with rarangken1[0].container():
            st.image('assets/rarangken-e.jpg', use_container_width=True)
            if st.button(label='Rarangken - e', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - e")
                def pop():
                    st.write("Ini adalah aksara rarangken 'e' (pépét). Aksara rarangken - e ditulis di atas aksara dasar untuk mengubah bunyi vokal menjadi 'e', seperti dalam kata 'séng' (seng).")
                if "pop" not in st.session_state:
                    pop()
        with rarangken1[1].container():
            st.image('assets/rarangken-ee.jpg', use_container_width=True)
            if st.button(label='Rarangken - é', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - é")
                def pop():
                    st.write("Ini adalah aksara rarangken 'é' (pamepet). Aksara rarangken - é ditulis di atas aksara dasar untuk mengubah bunyi vokal menjadi 'é', seperti dalam kata 'méja' (meja).")
                if "pop" not in st.session_state:
                    pop()
        with rarangken1[2].container():
            st.image('assets/rarangken-eu.jpg', use_container_width=True)
            if st.button(label='Rarangken - eu', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - eu")
                def pop():
                    st.write("Ini adalah aksara rarangken 'eu' (panéléng). Aksara rarangken - eu ditulis di atas aksara dasar untuk mengubah bunyi vokal menjadi 'eu' seperti dalam kata 'meunang' (dapat).")
                if "pop" not in st.session_state:
                    pop()
        with rarangken1[3].container():
            st.image('assets/rarangken-h.jpg', use_container_width=True)
            if st.button(label='Rarangken - h', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - h")
                def pop():
                    st.write("Ini adalah aksara rarangken 'h' (pamaéh). Aksara rarangken - h ditulis di bawah aksara dasar untuk menambahkan bunyi 'h' di akhir suku kata, seperti dalam kata 'panah'.")
                if "pop" not in st.session_state:
                    pop()

        with rarangken2[0].container():
            st.image('assets/rarangken-i.jpg', use_container_width=True)
            if st.button(label='Rarangken - i', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - i")
                def pop():
                    st.write("Ini adalah aksara rarangken 'i' (panghulu). Aksara rarangken - i ditulis di atas aksara dasar untuk mengubah bunyi vokal menjadi 'i', seperti dalam kata 'birit' (ekor).")
                if "pop" not in st.session_state:
                    pop()
        with rarangken2[1].container():
            st.image('assets/rarangken-la.jpg', use_container_width=True)
            if st.button(label='Rarangken - la', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - la")
                def pop():
                    st.write("Ini adalah aksara rarangken 'la' (panyuku). Aksara rarangken - la ditulis di bawah aksara dasar untuk menambahkan bunyi 'la', seperti dalam kata 'balap'.")
                if "pop" not in st.session_state:
                    pop()
        with rarangken2[2].container():
            st.image('assets/rarangken-ng.jpg', use_container_width=True)
            if st.button(label='Rarangken - ng', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - ng")
                def pop():
                    st.write("Ini adalah aksara rarangken 'ng' (panyecek). Aksara rarangken - ng ditulis di atas aksara dasar untuk menambahkan bunyi 'ng' di akhir suku kata, seperti dalam kata 'dagang'.")
                if "pop" not in st.session_state:
                    pop()
        with rarangken2[3].container():
            st.image('assets/rarangken-o.jpg', use_container_width=True)
            if st.button(label='Rarangken - o', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - o")
                def pop():
                    st.write("Ini adalah aksara rarangken 'o' (panolong). Aksara rarangken - o ditulis di atas aksara dasar untuk mengubah bunyi vokal menjadi 'o', seperti dalam kata 'tokoh'.")
                if "pop" not in st.session_state:
                    pop()

        with rarangken3[0].container():
            st.image('assets/rarangken-r.jpg', use_container_width=True)
            if st.button(label='Rarangken - r', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - r")
                def pop():
                    st.write("Ini adalah aksara rarangken 'r' (panyakra). Aksara rarangken - r ditulis di atas aksara dasar untuk menambahkan bunyi 'r' setelah konsonan, seperti dalam kata 'krama'.")
                if "pop" not in st.session_state:
                    pop()
        with rarangken3[1].container():
            st.image('assets/rarangken-ra.jpg', use_container_width=True)
            if st.button(label='Rarangken - ra', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - ra")
                def pop():
                    st.write("Ini adalah aksara rarangken 'ra' (pamaeh). Aksara rarangken - ra ditulis di bawah aksara dasar untuk menambahkan bunyi 'ra', seperti dalam kata 'sayur'.")
                if "pop" not in st.session_state:
                    pop()
        with rarangken3[2].container():
            st.image('assets/rarangken-u.jpg', use_container_width=True)
            if st.button(label='Rarangken - u', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - u")
                def pop():
                    st.write("Ini adalah aksara rarangken 'u' (panyuku). Aksara rarangken - u ditulis di bawah aksara dasar untuk mengubah bunyi vokal menjadi 'u', seperti dalam kata 'bulan'.")
                if "pop" not in st.session_state:
                    pop()
        with rarangken3[3].container():
            st.image('assets/rarangken-x.jpg', use_container_width=True)
            if st.button(label='Rarangken - x', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - x")
                def pop():
                    st.write("Ini adalah aksara rarangken 'x' (pamingkal). Aksara rarangken - x ditulis di bawah aksara dasar untuk menambahkan bunyi konsonan tambahan, seperti dalam kata 'nyata'.")
                if "pop" not in st.session_state:
                    pop()

        with rarangken4[0].container():
            st.image('assets/rarangken-ya.jpg', use_container_width=True)
            if st.button(label='Rarangken - ya', type='secondary', use_container_width=True):
                @st.dialog("Rarangken - ya")
                def pop():
                    st.write("Ini adalah aksara rarangken 'ya' (panglayar). Aksara rarangken - ya ditulis di atas aksara dasar untuk menambahkan bunyi 'ya', seperti dalam kata 'sayur'.")
                if "pop" not in st.session_state:
                    pop()


    # Bagian Latihan
    with latihan:
        latihan.subheader("Nguji Kaahlian Anjeun (Uji Kemampuan Anda)")

        levels = latihan.columns(3)
        with levels[0].container():
            st.image('assets/level1.jpeg', use_container_width=True)
            if get_level1(config, st.session_state.username) is False:
                if st.button(label='Selesaikan Tingkat 1', type='secondary', use_container_width=True):
                    switch_page('level1')
            else:
                if st.button(label='Review Tingkat 1', type='secondary', use_container_width=True):
                    switch_page('review1')

        with levels[1].container():
            st.image('assets/level2.jpeg', use_container_width=True)

            if get_level2(config, st.session_state.username) is False:
                if st.button(label='Selesaikan Tingkat 2', type='secondary', use_container_width=True):
                    if get_level2(config, st.session_state.username) is False and get_level1(config, st.session_state.username) is True:
                        switch_page('level2')
                    else: 
                        if get_level1(config, st.session_state.username) is False:
                            st.warning('Ngalakukeun Tingkat Sebelumnya')
            else:
            # if get_level2(config, st.session_state.username) is True:
                if st.button(label='Review Tingkat 2', type='secondary', use_container_width=True):
                    switch_page('review2')

        with levels[2].container():
            st.image('assets/level3.jpeg', use_container_width=True)

            if get_level3(config, st.session_state.username) is False:
                if st.button(label='Selesaikan Tingkat 3', type='secondary', use_container_width=True):
                    if get_level3(config, st.session_state.username) is False and get_level2(config, st.session_state.username) is True:
                        switch_page('level3')
                    else: 
                        if get_level2(config, st.session_state.username) is False or get_level1(config, st.session_state.username) is False:
                            st.warning('Ngalakukeun Tingkat Sebelumnya')
            else:
            # if get_level2(config, st.session_state.username) is True:
                if st.button(label='Review Tingkat 3', type='secondary', use_container_width=True):
                    switch_page('review3')
                    
        if get_level3(config, st.session_state.username) is True and get_posttest_taken(config, st.session_state.username) is False:
            st.success('Selamat telah menyelesaikan ketiga tingkat latihan, anda dapat mengambil Post Test')
            if st.button(label='📝 Ambil Post Test', type='primary', use_container_width=True):
                switch_page('posttest')
        else:
            st.success(f'Post Test sudah dikerjakan! Skor anda: {get_posttest(config, st.session_state.username)}')

    # Bagian Transliterasi
    with transliterasi.form('transliterasi_form', clear_on_submit=True):
        uploaded_image = st.file_uploader(
            'Mangga upload gambar ...', type=['jpg', 'png', 'jpeg']
        )

        submit, clear, _, _ = st.columns(4)
        submit.form_submit_button(label='Konversi', use_container_width=True, type='primary')
        clear.form_submit_button(label='Clear', use_container_width=True)

    if uploaded_image:
        try:
            input_path = uploaded_image.name
            file_binary = uploaded_image.read()
            with open(input_path, 'wb') as temp_file:
                temp_file.write(file_binary)

            image = Image.open(uploaded_image)
            transliterasi.image(image, caption=input_path, use_container_width=True)

            model = transliterate_model()
            with st.spinner('Nuju memproses gambar ...'):
                results = model.process_image(input_path)

            if results:
                transliterasi.success('Konversi junun (Konversi berhasil)!')
                transliterasi.markdown(f'''
                                        ### Kenging konversi / (Hasil Konversi):
                                        ## {results}
                                       ''')
                
                gtts = gTTS(text=results, lang='su', tld='co.id')
                audio_stream = BytesIO()
                gtts.write_to_fp(audio_stream)

                if transliterasi.button(label='Dengekeun', icon='📣'):
                    transliterasi.audio(audio_stream, autoplay=True)
            else:
                transliterasi.error('''Konversi gagal! Mangga cobi deui
                                    (Konversi Gagal! Silahkan coba lagi)
                                    ''')
        except Exception as e:
            st.error(f'Error: {traceback.format_exc}, \n {e}')

    
    # Bagian Text-to-Speech menggunakan aksen sunda
    with tts:
        tts.title('Dengekeun')
        text_input = tts.text_area('Asupkeun teks')

        if tts.button(label='Dengekeun', type='primary', icon='📢'):
            if text_input:
                gtts = gTTS(text=text_input, lang='su', tld='co.id')
                audio_stream = BytesIO()

                gtts.write_to_fp(audio_stream)
                tts.audio(audio_stream, autoplay=True)
            else:
                tts.error('''Tulung asupkeun teks
                        (Tolong masukan teks)''')


############################################################################################
############################################################################################


# Application
if __name__ == '__main__':
    # Load config file
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    # cek autentikasi
    try:
        authenticator.login()
    except LoginError as e:
        st.error(e)

    if st.session_state['authentication_status']:
        get_pretest(config, st.session_state['username'])

        if not get_pretest_taken(config, st.session_state.username):
            switch_page('pretest')

        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)

        logout, _, bantuan = st.columns(3)
        with logout:
            if authenticator.logout():
                config['credentials']['usernames'][st.session_state.username]['logged_in'] = False

        with bantuan:
            if st.button(label='Peryogi Bantuan 🤔', type='secondary', use_container_width=True):
                @st.dialog("🛠️ Pitunjuk Pengunaan Aplikasi")
                def help():
                    st.subheader('💬 Pitunjuk Pengunaan Fitur Latihan sarta Post Test')
                    st.text("- Latihan harus dikerjakan dengan urut mulai dari\ntingkat 1 hingga 3\n- Post Test bisa dikerjakan jika sudah menyelesaikan\nlatihan hingga tingkat 3")
                    st.subheader('💬 Pitunjuk Pengunaan Fitur Konversi')
                    st.text("- Pastikan gambar yang ingin dikonversi bersih dengan\nbackground putih dan bebas dari gangguan untuk\nmemastikan konversi berjalan dengan baik\n- Contoh gambar yang salah:\n(ada bayangan, teks, dan corak lantai)")
                    st.image('assets/contoh1.jpeg')
                    st.text('- Contoh gambar yang benar:\n(tidak ada bayangan, teks, dan corak lantai)')
                    st.image('assets/contoh2.jpeg')

                if "help" not in st.session_state:
                    help()
                    
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
