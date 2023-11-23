from views import View
import streamlit as st
import pandas as pd
from datetime import datetime,timedelta
import time
class AgendarHorarioUI:
    @staticmethod
    def main():
        st.header('Agendar um horário')
        tab1, tab2= st.tabs(["Disponíveis", "Solicitadas"])
        with tab1:
            AgendarHorarioUI.disponiveis()
        with tab2:
            AgendarHorarioUI.solicitadas()


    def disponiveis():
        agendas = View.agenda_listar()
        hoje = datetime.today()
        semana = datetime.today() + timedelta(days=7)
        lista_disponivel = []
        for agenda in agendas:
            if hoje<agenda.get_data()<semana and agenda.get_confirmado() == False:
                if  agenda.get_Cliente() == 0 and agenda.get_Servico() == 0:
                    lista_disponivel.append(agenda)


        if len(lista_disponivel)==0:
            st.write('Nenhuma agenda disponível no momento')
        else:
            df = pd.DataFrame([x.to_json() for x in lista_disponivel])
            st.dataframe(df,hide_index=True)
            

            servicos = View.servico_listar()

            op1 = st.selectbox('Selecione um horario',lista_disponivel,index=None,placeholder="Escolha um horário entre os listados acima")
            op2 = st.selectbox('Selecione um serviço',servicos,index=None,placeholder="Escolha um serviço entre os listados acima")
        

            if st.button('agendar'):
                if op1 and op2:
                    for agenda in agendas:
                        if agenda.get_data()==op1.get_data() and agenda.get_id()==op1.get_id() :
                            View.agenda_atualizar(agenda.get_id(),agenda.get_data(),False,st.session_state['cliente_id'],op2.get_id())
                            st.success('Serviço solicitado com sucesso')
                            break
                else:
                    st.error('Selecione um serviço e um horário')
                    

    def solicitadas():
        agendas =View.agenda_listar()
        lista_solicitacao = []
        hoje = datetime.today()
        semana = datetime.today() + timedelta(days=7)
        for agenda in agendas:
            if hoje<agenda.get_data()<semana and agenda.get_confirmado() == False:
                    if agenda.get_Cliente() == st.session_state['cliente_id'] and  agenda.get_Servico() != 0:
                        lista_solicitacao.append({"Datas":agenda.get_data().strftime('%d/%m/%Y %H:%M'),'Serviço': View.servico_listar_id(agenda.get_Servico())})

        if len(lista_solicitacao)==0:
            st.write('Nenhuma agenda solicitada no momento')
        else:
            df= pd.DataFrame(lista_solicitacao)
            st.dataframe(df,hide_index=True)
