import json
class Cliente:

  def __init__(self, id, nome, email, fone,senha):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
    self.__senha = senha

  def get_id(self): return self.__id
  def get_nome(self):   return self.__nome
  def get_email(self):  return self.__email
  def get_fone(self):   return self.__fone
  def get_senha(self):   return self.__senha
  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_fone(self, fone): self.__fone = fone
  def set_email(self, email):   self.__email = email
  def set_senha(self, senha):   self.__senha = senha
  def __eq__(self,x):
    if x is not None:
      if self.__id == x.__id and self.__nome ==x.__nome and self.__email == x.__email and self.__fone == x.__fone and self.__senha == x.__senha:
          return True
      else:
          return False
  def to_json(self):
    return {
      "id" : self.get_id(),
      "nome" : self.get_nome(),
      "email" : self.get_email(),
      "fone": self.get_fone(),
      "senha": self.get_senha()
    }
  def to_json_sem_senha(self):
    return {
      "id" : self.get_id(),
      "nome" : self.get_nome(),
      "email" : self.get_email(),
      "fone": self.get_fone(),
    }
  
  def __str__(self):
      return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__senha}"

class NCliente:
  __clientes = []

  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0
    for cliente in cls.__clientes:
      id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)
    NCliente.salvar()

  @classmethod
  def listar(cls):
    NCliente.abrir()
    return cls.__clientes

  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in NCliente.listar():
      if cliente.get_id() == id:
        return cliente
    return None

  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = NCliente.listar_id(obj.get_id())
    if cliente!=None:
      cliente.set_nome(obj.get_nome())
      cliente.set_email(obj.get_email())
      cliente.set_fone(obj.get_fone())
      cliente.set_senha(obj.get_senha())
    NCliente.salvar()

  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = NCliente.listar_id(obj.get_id())
    if cliente!=None:
      cls.__clientes.remove(cliente)
    NCliente.salvar()
  
  @classmethod
  def email(cls, email):
    NCliente.abrir()
    if cls.__clientes is not None:
      for cliente in cls.__clientes:
          if cliente.get_email()==email:
            return True
    return False

  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
          c = Cliente(obj["id"], obj["nome"],obj["email"], obj["fone"],obj["senha"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    clientes_salvar=[]
    with open("clientes.json", mode="w") as arquivo:
      for cliente in cls.__clientes:
        clientes_salvar.append(cliente.to_json())
      json.dump(clientes_salvar, arquivo,indent=4)