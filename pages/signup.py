import yaml
import streamlit as st
import streamlit_authenticator as stauth

from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page
from streamlit_authenticator.utilities import RegisterError



def main():
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    back, _, _, _ = st.columns(4)
    if back.button(label='Kembali', use_container_width=True):
        switch_page('home')

    try:
        (email_of_registered_user,
            username_of_registered_user,
            name_of_registered_user) = authenticator.register_user()

        if email_of_registered_user:
            st.success('Berhasil membuat akun')

            config['credentials']['usernames'][username_of_registered_user]['pretest'] = 0
            config['credentials']['usernames'][username_of_registered_user]['pretest_taken'] = False
            config['credentials']['usernames'][username_of_registered_user]['level1'] = 0
            config['credentials']['usernames'][username_of_registered_user]['level2'] = 0
            config['credentials']['usernames'][username_of_registered_user]['level3'] = 0
            config['credentials']['usernames'][username_of_registered_user]['level1_passed'] = False
            config['credentials']['usernames'][username_of_registered_user]['level2_passed'] = False
            config['credentials']['usernames'][username_of_registered_user]['level3_passed'] = False
            config['credentials']['usernames'][username_of_registered_user]['posttest'] = 0
            config['credentials']['usernames'][username_of_registered_user]['posttest_taken'] = False

            with open('config.yaml', 'w', encoding='utf-8') as file:
                yaml.dump(config, file, default_flow_style=False)

            switch_page('index')

    except RegisterError as e:
        st.error(e)



if __name__ == '__main__':
    if st.session_state:    
        if st.session_state.authentication_status:
            switch_page('index')
        else:
            main()
    else:
        main()
