import streamlit as st
import time
import pandas as pd
from views import View
class ServicoReajusteUI:
    @staticmethod
    def main():
        st.header('Reajuste de preços')
        ServicoReajusteUI.reajuste()

    def reajuste():
        
        col1,col2 = st.columns(2)
        with col1:
            servicos=[]
            for servico in View.servico_listar():
                servicos.append(servico.to_json())
            df = pd.DataFrame(servicos)
            st.dataframe(df,hide_index=True)
        with col2:
            percentual = st.text_input('Informe o reajuste em %')
            if st.button('reajustar'):
                try:
                    View.servico_reajustar(float(percentual))
                    st.success('Reajuste concluído com sucesso')
                    time.sleep(1)
                    st.rerun()
                except ValueError:
                    st.error('Número inválido')
                    time.sleep(1)
                    st.rerun()
            
