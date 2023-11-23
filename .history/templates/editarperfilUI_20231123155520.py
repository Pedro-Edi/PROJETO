import streamlit as st
from views import View
import time
class LoginUI:
    @staticmethod
    def main():
        st.header('Login')
        LoginUI.entrar()
    def entrar():
        if st.session_state["cliente_id"]!=0:
            nome = st.text_input('Informe o nome')
            email = st.text_input('Informe o email')
            fone = st.text_input('Informe o fone')
            senha = st.text_input('Informe a senha')
            if st.button('confirmar'):
                View.agenda_atualizar(st.session_state["cliente_id"],nome,email,fone,senha)
                time.sleep(1)
                st.rerun()        