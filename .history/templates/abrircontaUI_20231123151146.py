import streamlit as st
from views import View
import time
class AbrirContaUI:
    @staticmethod
    def main():
        st.header('Abrir conta')
        AbrirContaUI.abrir()
    def abrir():
        nome = st.text_input('Informe o seu nome')
        email = st.text_input('Informe o seu email')
        fone = st.text_input('Informe o fone')
        senha = st.text_input('Informe a senha')
        if st.button('cadastrar'):
            try:
                View.cliente_inserir(nome,email,fone,senha)
                st.success('Cliente inserido com sucesso')
                time.sleep(1)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
                time.sleep(1)
                st.rerun()


AbrirContaUI.main()