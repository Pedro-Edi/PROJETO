from http import client
from logging import PlaceHolder
import streamlit as st
from views import View
import pandas as pd
import time

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3 ,tab4= st.tabs(["listar", "inserir", "atualizar","excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir() 
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()

    def listar():
        if len(View.cliente_listar())==0:
            st.write('Nenhum cliente encontrado')
        else:
            clientes=[]
            for cliente in View.cliente_listar():
                clientes.append(cliente.to_json_sem_senha())
            df = pd.DataFrame(clientes)
            st.dataframe(df,hide_index=True)

    def inserir():
        nome = st.text_input('Informe o nome')
        email = st.text_input('Informe o email')
        fone = st.text_input('Informe o fone')
        senha = st.text_input('Informe a senha')
        if st.button('inserir'):
            try:
                View.cliente_inserir(nome,email,fone,senha)
                st.success('Cliente inserido com sucesso')
                
            except ValueError as erro:
                st.error(erro)

    def atualizar():
        clientes= View.cliente_listar()
        
        if len(clientes)==0:
            st.write('Nenhum cliente encontrado')
        else:
            op = st.selectbox("Atualização de Clientes",clientes,placeholder='Selecione algum cliente',index=None)
            id = op.get_id() if op!=None else None
            nome = st.text_input("Informe o novo nome",op.get_nome() if op!=None else None)
            email = st.text_input("Informe o novo e-mail",op.get_email() if op!=None else None)
            fone = st.text_input("Informe o novo fone",op.get_fone() if op!=None else None)
            senha=op.get_senha() if op!=None else None

            if st.button("Atualizar"):
                try:
                    View.cliente_atualizar(id, nome, email, fone,senha)
                    st.success("Cliente atualizado com sucesso")
                    time.sleep(1)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(1)
                    st.rerun()

    def excluir():
        clientes = View.cliente_listar()
        if len(clientes)==0:
            st.write('Nenhum cliente encontrado')
        else:
            op = st.selectbox("Exclusão de Clientes",clientes,placeholder='Selecione algum cliente',index=None)
            if st.button('excluir'):
                View.cliente_excluir(op.get_id() if op!=None else None)
                st.success('Cliente excluído com sucesso')
                time.sleep(1)
                st.rerun()
       
        

        