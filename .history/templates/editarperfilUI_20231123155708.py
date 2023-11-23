import streamlit as st
from views import View
import time
class LoginUI:
    @staticmethod
    def main():
        st.header('Login')
        Edi()
    def editar():
        if st.session_state["cliente_id"]!=0:
            nome = st.text_input('Informe o nome')
            email = st.text_input('Informe o email')
            fone = st.text_input('Informe o fone')
            senha = st.text_input('Informe a senha')
            if st.button('confirmar'):
                View.agenda_atualizar(st.session_state["cliente_id"],nome,email,fone,senha)
                time.sleep(1)
                st.rerun()
        else:
            email = st.text_input('Informe o email')
            fone = st.text_input('Informe o fone')
            senha = st.text_input('Informe a senha')
            if st.button('confirmar'):
                try:
                    View.agenda_atualizar(st.session_state["cliente_id"],"admin",email,fone,senha)
                    time.sleep(1)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(1)
                    st.rerun()

                    