import streamlit as st
from views import View
import time
class EditarPerfilUI:
    @staticmethod
    def main():
        st.header('Login')
        EditarPerfilUI.editar()
    def editar():
        if st.session_state["cliente_id"]!=0:
            nome = st.text_input('Informe o novo nome')
            email = st.text_input('Informe o novo email')
            fone = st.text_input('Informe o novo fone')
            senha = st.text_input('Informe a senha')
            if st.button('confirmar'):
                try:
                    View.cliente_atualizar(st.session_state["cliente_id"],nome,email,fone,senha)
                    st.success('Perfil atualizado com sucesso')
                    time.sleep(1)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(1)
                    st.rerun()
        else:
            email = st.text_input('Informe o novo email')
            fone = st.text_input('Informe o novo fone')
            senha = st.text_input('Informe a nova senha')
            if st.button('confirmar'):
                try:
                    View.cliente_atualizar(st.session_state["cliente_id"],"admin",email,fone,senha)
                    st.success('Perfil atualizado com sucesso')
                    time.sleep(1)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(1)
                    st.rerun()

                    
