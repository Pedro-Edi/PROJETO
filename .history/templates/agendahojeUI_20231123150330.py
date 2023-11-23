import streamlit as st
import pandas as pd
from views import View
from datetime import datetime
class AgendaHojeUI:
    @staticmethod
    def main():
        st.header('Agenda de Hoje')
        tab1,tab2,tab3 = st.tabs(['Disponiveis','Pendentes','Realizados'])
        with tab1:
            AgendaHojeUI.disponiveis()
        with tab2:
            AgendaHojeUI.pendentes()
        with tab3:
            AgendaHojeUI.realizados()

    def disponiveis():
        agendas = View.agenda_hoje()
       
        dic=[]
        for agenda in agendas:
            if agenda.get_Cliente() == 0 and agenda.get_Servico() == 0:
                dic.append(agenda.to_json())
        df = pd.DataFrame(dic)
        st.dataframe(df,hide_index=True)

    def pendentes():

        hoje =datetime.today()
        agendas = View.agenda_hoje()
        dic=[]
        for agenda in agendas:
            if agenda.get_confirmado()==True and agenda.get_data()>hoje and agenda.get_Cliente() ==  st.session_state['cliente_id'] and agenda.get_Servico() != 0:
                dic.append(agenda.to_json())
        df = pd.DataFrame(dic)
        st.dataframe(df,hide_index=True)

    def realizados():
        hoje =datetime.today()
        agendas = View.agenda_hoje()
            dic=[]
            for agenda in agendas:
                if agenda.get_confirmado()==True and agenda.get_data()<hoje and agenda.get_Cliente() ==  st.session_state['cliente_id'] and agenda.get_Servico() != 0:
                    dic.append(agenda.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df,hide_index=True)