import datetime
import json
import streamlit as st


class Agenda:

  def __init__(self, id, data, confirmado, Cliente, Servico):
    self.__id = id
    self.__data = data
    self.__confirmado = confirmado
    self.__Cliente = Cliente
    self.__Servico = Servico
    
  def get_id(self): return self.__id
  def get_data(self): return self.__data
  def get_confirmado(self): return self.__confirmado
  def get_Cliente(self):  return  self.__Cliente
  def get_Servico(self):  return  self.__Servico
  def set_id(self,id): self.__id = id
  def set_data(self, data): self.__data = data
  def set_confirmado(self, confirmado): self.__confirmado = confirmado
  def set_Cliente(self, Cliente): self.__Cliente = Cliente
  def set_Servico(self, Servico): self.__Servico= Servico
  def to_json(self):
    return{
      "id":self.get_id(),
      "data": self.get_data().strftime('%d/%m/%Y %H:%M'), 
      "confirmado": self.get_confirmado(),
      "cliente": self.get_Cliente(),
      "servico": self.get_Servico(),
    }

  def __str__(self):
    return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {'Não confirmado' if self.__confirmado==False else 'Confirmado'} - {self.__Cliente} - {self.__Servico}"



class NAgenda:
  __agendas = []

  @classmethod
  def inserir(cls, obj):
    NAgenda.abrir()
    id = 0
    for agenda in cls.__agendas:
      id = agenda.get_id()
    obj.set_id(id + 1)
    cls.__agendas.append(obj)
    NAgenda.salvar()

  @classmethod
  def listar_id(cls, id):
    NAgenda.abrir()
    for agenda in cls.__agendas:
      if agenda.get_id() == id:
        return agenda
    return None

  @classmethod
  def listar(cls):
    NAgenda.abrir()
    return cls.__agendas

  @classmethod
  def atualizar(cls, obj):
    NAgenda.abrir()
    agenda = NAgenda.listar_id(obj.get_id())
    if agenda!=None:
      agenda.set_data(obj.get_data())
      agenda.set_confirmado(obj.get_confirmado())
      agenda.set_Cliente(obj.get_Cliente())
      agenda.set_Servico(obj.get_Servico())
    NAgenda.salvar()

  @classmethod
  def excluir(cls, obj):
    NAgenda.abrir()
    agenda = NAgenda.listar_id(obj.get_id())
    if agenda!=None:
      cls.__agendas.remove(agenda)
    NAgenda.salvar()

  @classmethod
  def abrir(cls):
    try:
      cls.__agendas = []
      with open("agendas.json", mode="r") as arquivo:
        agendas_json = json.load(arquivo)
        for obj in agendas_json:
          data = datetime.datetime.strptime(obj["data"], "%d/%m/%Y %H:%M")
          a = Agenda(obj["id"], data, obj["confirmado"], obj["cliente"],
                     obj["servico"])
          cls.__agendas.append(a)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("agendas.json", mode="w") as arquivo:
      agendas_json = []
      for agenda in cls.__agendas:
        agendas_json.append(agenda.to_json())
      json.dump(agendas_json, arquivo, indent=4)