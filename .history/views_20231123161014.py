from tkinter import N
from datetime import datetime,timedelta
from models.cliente import Cliente,NCliente
from models.servico import Servico,NServico
from models.agenda import Agenda,NAgenda
class View:

  
  def cliente_inserir(nome,email,fone,senha):
    if nome=='' or email=='' or fone=='' or senha=='':
        raise ValueError('Campos inválidos')
    elif NCliente.email(email)==True:
      raise ValueError('Insira novo email')
    else: 
      cliente=Cliente(0,nome,email,fone,senha)
      NCliente.inserir(cliente)

  
  def cliente_listar():
    return NCliente.listar()
  
  def cliente_listar_id(id):
    if id!=0:
      return NCliente.listar_id(id)
    return None
  
  def cliente_atualizar(id,nome,email,fone,senha):
    if nome=='' or email=='' or fone=='' or senha=='':
        raise ValueError('Campos inválidos')
    elif NCliente.email(email)==True:
      raise ValueError('Email novo email')
    else:
      cliente = Cliente(id,nome,email,fone,senha)
      NCliente.atualizar(cliente)
    
  
  def cliente_excluir(id):
    cliente = Cliente(id,"","","","")
    NCliente.excluir(cliente)
  
 
  
  
  def cliente_login(email,senha):
    for cliente in View.cliente_listar():
      if email==cliente.get_email() and senha ==cliente.get_senha():
        return cliente
    return None
  
  
  def cliente_admin():
    for cliente in View.cliente_listar():
      if cliente.get_nome() == "admin": return
    View.cliente_inserir("admin", "admin", "0000", "admin")

  
  def servico_inserir(descricao,valor,duracao):
    if descricao=='' or valor<0 or duracao<=0:
      raise ValueError('Dados inválidos')
    servico=Servico(0,descricao,valor,duracao)
    NServico.inserir(servico)

  
  def servico_listar():
    return NServico.listar()
  
  def servico_listar_id(id):
      return NServico.listar_id(id)


  
  def servico_atualizar(id,descricao,valor,duracao):
    if descricao=='' or valor<0 or duracao<=0:
      raise ValueError('Dados inválidos')
    servico=Servico(id,descricao,float(valor),int(duracao))
    NServico.atualizar(servico)
    
  
  def servico_excluir(id):
    cliente = Servico(id,"","","")
    NServico.excluir(cliente)

  
  def servico_reajustar(percentual):
    if percentual<0:
      raise ValueError
    for servico in View.servico_listar():
      valor = (servico.get_valor()*(1+(percentual/100)))
      View.servico_atualizar(servico.get_id(),servico.get_descricao(),valor,servico.get_duracao())

  
  def agenda_inserir(data,confirmado,cliente,servico):
      agenda= Agenda(0,data,confirmado,cliente,servico)
      NAgenda.inserir(agenda)

  
  def agenda_listar():
    return NAgenda.listar()
  

  
  def agenda_atualizar(id,data,confirmado,cliente,servico):
    agenda= Agenda(id,data,confirmado,cliente,servico)
    NAgenda.atualizar(agenda)
    
  
  def agenda_excluir(id):
    agenda =Agenda(id,"","","","")
    NAgenda.excluir(agenda)

  
  def agenda_hoje():
    agendas = []
    for horario in View.agenda_listar():
      if horario.get_data().date() == datetime.today().date():
        agendas.append(horario)
    return agendas

  
  def agenda_abrir_agenda_do_dia(data_ini,data_final,intervalo):
    data_hoje =datetime.today()
    if data_ini<=data_hoje or data_final<data_ini or intervalo<=0:
      raise ValueError
    intervalo_ =  timedelta(minutes=intervalo)       
    while data_ini <=data_final:
      NAgenda.inserir(Agenda(0,data_ini,False,0,0))
      data_ini= data_ini + intervalo_

  
    
 