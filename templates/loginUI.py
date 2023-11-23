import streamlit as st
from views import View
import time
class LoginUI:
    @staticmethod
    def main():
        st.header('Login')
        LoginUI.entrar()
    def entrar():
        email = st.text_input('Informe seu email')
        senha = st.text_input('Informe sua senha')
        if st.button('login'):
            cliente = View.cliente_login(email,senha)
            if cliente is not None:
                st.success('Login realizado com sucesso')
                st.success('Bem vindo, ' + cliente.get_nome())
                st.session_state['cliente_id']= cliente.get_id()
                st.session_state['cliente_nome']= cliente.get_nome()
            else:
                st.error('Usuário ou senha inválido(s)')
            time.sleep(1)
            st.rerun()