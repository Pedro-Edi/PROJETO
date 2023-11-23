import streamlit as st
from views import View
import pandas as pd
from datetime import datetime
import time

class AbrirAgendaUI:
    @staticmethod
    def main():
        st.header("Cadastro")
        AbrirAgendaUI.abrir()
    def abrir():
        
        data_input = st.text_input("informe a data inicial (dia/mes/ano)")
        h_i = st.text_input("informe a hora inicial (H\:M)")
        h_F = st.text_input("informe a hora final (H\:M)")
        intervalo = st.text_input("informe o intervalo")

                    
        if st.button('inserir'):
            try:
                data_ini = datetime.strptime(f'{data_input} {h_i}',"%d/%m/%Y %H:%M")
                data_final = datetime.strptime(f"{data_ini.date()} {h_F}","%Y-%m-%d %H:%M")

                View.agenda_abrir_agenda_do_dia(data_ini,data_final,int(intervalo))
                st.success('inserido')
                time.sleep(1)
                #st.rerun()
            except ValueError:
                st.error('Campo(s) inválidos')
                time.sleep(1)
                st.rerun()
        
            