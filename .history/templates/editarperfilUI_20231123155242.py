import streamlit as st
from views import View
import time
class LoginUI:
    @staticmethod
    def main():
        st.header('Login')
        LoginUI.entrar()
    def entrar():
        nome = st.text_input('Informe o nome')
        email = st.text_input('Informe o email')
        fone = st.text_input('Informe o fone')
        senha = st.text_input('Informe a senha')
        