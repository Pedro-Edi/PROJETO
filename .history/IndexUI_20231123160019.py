import streamlit as st
from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.editarperfilUI import EditarPerfilUI
from templates.servicoreajusteUI import ServicoReajusteUI
from templates.agendahojeUI import AgendaHojeUI
from templates.agendarhorarioUI import AgendarHorarioUI
from templates.visuagendamentoUI import VisualizarAgendamentoUI
from templates.confirmaragendamentoUI import ConfirmarAgendamentoUI
from views import View



class IndexUI:
    def sidebar():
        
        
        if  "cliente_id" not in st.session_state:
            op1 = st.sidebar.selectbox("Menu", ["Abrir Conta","Login"])
            st.sidebar.write("Nenhum usuário entrou no sistema")

            if op1 == "Abrir Conta": AbrirContaUI.main()
            if op1 == "Login": LoginUI.main()
        else:
            if st.session_state['cliente_id']==0:
                op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Servicos","Manter Agenda","Abrir Agenda do Dia","Serviço Reajuste","Confirmar Agendamento","Editar Perfil"])
                st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
                if st.sidebar.button('logout'):
                    del st.session_state["cliente_id"]
                    st.rerun()
                if op == "Manter Clientes": ManterClienteUI.main()
                if op == "Manter Servicos": ManterServicoUI.main()
                if op == "Manter Agenda": ManterAgendaUI.main()
                if op == "Editar Perfil": EditarPerfilUI.main()
                if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
                if op == "Serviço Reajuste": ServicoReajusteUI.main()
                if op == "Confirmar Agendamento": ConfirmarAgendamentoUI.main()
            else:
                op = st.sidebar.selectbox("Menu", ["Abrir Conta","Agenda de Hoje","Agendar horário","Visualizar agendamentos","Editar Perfil"])
                st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
                if op == "Abrir Conta": AbrirContaUI.main()
                                if op == "Editar Perfil": EditarPerfilUI.main()
                if op == "Agenda de Hoje": AgendaHojeUI.main()
                if op == "Agendar horário": AgendarHorarioUI.main()
                if op == "Visualizar agendamentos": VisualizarAgendamentoUI.main()
                if st.sidebar.button('logout'):
                     del st.session_state["cliente_id"]
                     st.rerun()
            

    def main():
        View.cliente_admin()
        IndexUI.sidebar()
        
IndexUI.main()