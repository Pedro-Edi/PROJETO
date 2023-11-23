from logging import PlaceHolder
import streamlit as st
from views import View
import time
import pandas as pd
class ManterServicoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3 ,tab4= st.tabs(["listar", "inserir", "atualizar","excluir"])
        with tab1:
            ManterServicoUI.listar()
        with tab2:
            ManterServicoUI.inserir() 
        with tab3:
            ManterServicoUI.atualizar()
        with tab4:
            ManterServicoUI.excluir()

    def listar():
        if len(View.servico_listar())==0:
            st.write('Nenhum serviço encontrado')
        else:
            servicos=[]
            for servico in View.servico_listar():
                servicos.append(servico.to_json())
            df = pd.DataFrame(servicos)
            st.dataframe(df,hide_index=True)

    def inserir():
        desc = st.text_input('Informe a descrição')
        valor = st.text_input('Informe o valor')
        dura = st.text_input('Informe a duração em minutos')
        if st.button('inserir'):
            try:
                View.servico_inserir(desc, float(valor), int(dura))
                st.success('Serviço inserido com sucesso')
                time.sleep(2)
                st.rerun()
            except ValueError:
                st.error('Dados inválidos')
                time.sleep(2)
                st.rerun()
    def atualizar():
        servicos = View.servico_listar()
        if len(servicos)==0:
            st.write('Nenhum serviço encontrado')
        else:
            op = st.selectbox('Atualização de serviços',servicos,placeholder='Selecione um serviço',index=None)
            id = op.get_id() if op!=None else None
            desc = st.text_input('informe a nova descrição',op.get_descricao() if op!=None else None)
            valor = st.text_input('informe o novo valor',op.get_valor() if op!=None else None)
            dura = st.text_input('informe a nova duração',op.get_duracao() if op!=None else None)
            if st.button('atualizar'):
                try:
                    View.servico_atualizar(id,desc, float(valor),int(dura))
                    st.success('Serviço atualizado com sucesso')
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
    def excluir():
        servicos = View.servico_listar()
        if len(servicos)==0:
            st.write('Nenhum serviço encontrado')
        else:
            op = st.selectbox('Exclusão de serviços',servicos,placeholder='Selecione um serviço',index=None)
            if st.button('excluir'):
                View.servico_excluir(op.get_id() if op!=None else None)
                st.success('Serviço excluído com sucesso')
                #time.sleep(2)
                #st.rerun()
       


        