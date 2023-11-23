from views import View
import streamlit as st
import pandas as pd
from datetime import datetime,timedelta
import time

class VisualizarAgendamentoUI:
    @staticmethod
    def main():
        st.header('Histórico de atendimentos')
        tab1, tab2= st.tabs(["Pendentes", "Realizadas"])
        with tab1:
            VisualizarAgendamentoUI.pendentes()
        with tab2:
            VisualizarAgendamentoUI.realizadas()



    def pendentes():
        agendas = View.agenda_listar()
        nao_realizados = []
        for a in agendas:
            if a.get_Cliente()==st.session_state["cliente_id"] and a.get_Servico()!=0 and a.get_confirmado()==True:
                if a.get_data()>datetime.today():
                    nao_realizados.append({'Data:': a.get_data().strftime("%d/%m/%Y %H:%M"),'Serviço':a.get_Servico()})
    
        if len(nao_realizados)==0:
            st.write('Nenhum atendimento pendente a ser feito')
        else:
            df= pd.DataFrame(nao_realizados)
            st.dataframe(df,hide_index=True)

    def realizadas():
        agendas = View.agenda_listar()
        realizados=[]
        for a in agendas:
            if a.get_Cliente()==st.session_state["cliente_id"] and a.get_Servico()!=0 and a.get_confirmado()==True:
                if a.get_data()<datetime.today():
                    realizados.append({'Data:': a.get_data().strftime("%d/%m/%Y %H:%M"),'Serviço':a.get_Servico()})
    
        if len(realizados)==0:
            st.write('Nenhum atendimento realizado')
        else:
            df = pd.DataFrame(realizados)
            st.dataframe(df,hide_index=True)

        