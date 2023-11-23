import streamlit as st
from views import View
import pandas as pd
from datetime import datetime
import time
class ManterAgendaUI:
    @staticmethod
    def main():
        st.header("Cadastro")
        tab1, tab2, tab3 ,tab4= st.tabs(["listar", "inserir", "atualizar","excluir"])
        with tab1:
            ManterAgendaUI.listar()
        with tab2:
            ManterAgendaUI.inserir() 
        with tab3:
            ManterAgendaUI.atualizar()
        with tab4:
            ManterAgendaUI.excluir()
        
    def listar():
        if len(View.agenda_listar())==0:
            st.write('Nenhuma agenda encontrada')
        else:
            agendas=[]
            for agenda in View.agenda_listar():
                agendas.append(agenda.to_json())
            df = pd.DataFrame(agendas)
            st.dataframe(df,hide_index=True)

    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        if len(clientes)==0 or len(servicos)==0:
            st.write('Para fazer uma agenda é necessário de ao menos um cliente e um serviço já cadastrados')        
        else:
            data_input = st.text_input('informe a data (dia/mes/ano h\:m)')
            op1=st.selectbox('Cliente',clientes,placeholder='Selecione algum cliente',index=None)
            op2=st.selectbox('Serviço',servicos,placeholder='Selecione algum serviço',index=None)
            if st.button('inserir'):
                try:
                    format="%d/%m/%Y %H:%M"
                    View.agenda_inserir(datetime.strptime(data_input,format),True,op1.get_nome() if op1!=None else '',op2.get_descricao() if op2!=None else '')
                    st.success('Agenda inserida com sucesso')
                    time.sleep(1)
                    st.rerun()
                except ValueError:
                    st.error('Data inválida')
                    time.sleep(1)
                    st.rerun()
                

    def atualizar():
        agendas = View.agenda_listar()
        
        
        if len(agendas)==0:
            st.write('Nenhuma agenda encontrada')
        else:            
            op1=st.selectbox('Atualização de agenda',agendas,placeholder='Selecione alguma agenda',index=None)
            id = op1.get_id() if op1!=None else None
            data_input= st.text_input('informe a nova data(dia/mes/ano h\m)', op1.get_data().strftime('%d/%m/%Y %H:%M') if op1!=None else None)

            clientes = View.cliente_listar()
            cliente_atual = View.cliente_listar_id(op1.get_Cliente() if op1!=None else None)
            if cliente_atual is not None:
                cliente = st.selectbox("Selecione o novo cliente", clientes,placeholder='Selecione um novo cliente', index=clientes.index(cliente_atual))
            else:  
                cliente = st.selectbox("Selecione o novo cliente", clientes,placeholder='Selecione um novo cliente',index=None)
            servicos = View.servico_listar()
            servico_atual = View.servico_listar_id(op1.get_Servico() if op1!=None else None)
            if servico_atual is not None:
                servico = st.selectbox("Selecione o novo serviço", servicos, index=servicos.index(servico_atual))
            else:
                servico = st.selectbox("Selecione o novo serviço", servicos,placeholder='Selecione um novo serviçp',index=None)

            if st.button('atualizar'):

                try:
                    View.agenda_atualizar(id,datetime.strptime(data_input,"%d/%m/%Y %H:%M"),op1.get_confirmado(), cliente.get_id(), servico.get_id())
                    st.success('Agenda atualizada com sucesso')
                    time.sleep(2)
                    st.rerun()
                except ValueError:
                    st.error('Dados inválidos')
                    time.sleep(2)
                    st.rerun()

    
    def excluir():
        agendas = View.agenda_listar()
        if len(agendas)==0:
            st.write('Nenhuma agenda encontrada')
        else:
                
            op1=st.selectbox('Exclusão de agenda',agendas,placeholder='Selecione alguma agenda',index=None)
            if st.button('excluir'):
                View.agenda_excluir(op1.get_id() if op1!=None else None)
                st.success('Agenda excluída com sucesso')
                time.sleep(2)
                st.rerun()
       

        