
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

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": LoginUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Servicos","Manter Agenda","Abrir Agenda do Dia","Serviço Reajuste","Confirmar Agendamento","Editar Perfil"])
    if op == "Manter Clientes": ManterClienteUI.main()
    if op == "Manter Servicos": ManterServicoUI.main()
    if op == "Manter Agenda": ManterAgendaUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()
    if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
    if op == "Serviço Reajuste": ServicoReajusteUI.main()
    if op == "Confirmar Agendamento": ConfirmarAgendamentoUI.main()

  def menu_cliente():
    op = st.sidebar.selectbox("Menu", ["Abrir Conta","Agenda de Hoje","Agendar horário","Visualizar agendamentos","Editar Perfil"])
    if op == "Abrir Conta": AbrirContaUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()
    if op == "Agenda de Hoje": AgendaHojeUI.main()
    if op == "Agendar horário": AgendarHorarioUI.main()
    if op == "Visualizar agendamentos": VisualizarAgendamentoUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      if st.session_state["cliente_nome"] == "admin": IndexUI.menu_admin()
      else: IndexUI.menu_cliente()
      IndexUI.btn_logout()  

  def main():
    View.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()
