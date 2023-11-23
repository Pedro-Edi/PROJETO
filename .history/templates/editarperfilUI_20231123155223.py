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
        