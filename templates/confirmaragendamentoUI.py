from views import View
import streamlit as st
import pandas as pd
import time
from datetime import datetime

class ConfirmarAgendamentoUI:
    @staticmethod
    def main():
        st.header('Confirmar agendamento')
        ConfirmarAgendamentoUI.confimar()
    def confimar():
        lista_solicitacao = []
        for agenda in View.agenda_listar():
            hoje= datetime.today()
            if agenda.get_data()> hoje  and agenda.get_Cliente!=0 and agenda.get_Servico()!=0 and agenda.get_confirmado()==False:
                lista_solicitacao.append(agenda.to_json())

        if len(lista_solicitacao)==0:
            st.write('Nenhuma solicitação feita')
        else:
            df = pd.DataFrame(lista_solicitacao)

            st.data_editor(
                df,
                key="my_key",
                column_config={
                    "confirmado": st.column_config.CheckboxColumn(
                        default=False,
                    )
                },
                disabled=["id","data","Cliente","Servico"],
                hide_index=True,)
            editor = st.session_state["my_key"]["edited_rows"]
            if editor:
                for a in lista_solicitacao:
                    agenda = lista_solicitacao.index(a)
                    if editor[agenda]['confirmado']==True:
                      View.agenda_atualizar(a["id"],datetime.strptime(a["data"], "%d/%m/%Y %H:%M"),True,a["cliente"],a["servico"])
                      st.success('Agenda confirmada com sucesso')
                      time.sleep(1)
                      st.rerun()

                
                 

                    