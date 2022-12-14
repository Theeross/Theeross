import os
import time
from agendamento import Agendamento
global eventos_usuarios
import re 
import sqlite3
from tkinter import *

usuarios = []
email = []
eventos_usuarios = {}

a = '#BCD2EE'
p = '#000000'
v = '#B22222'

class Usuario:
  def __init__(self):
    self.__nome = ''
    self.__email = ''
    self.__senha = ''

  def realizar_cadastro(self):
    janela_cadastro = Tk()
    janela_cadastro.title('Planner.cadastro')
    janela_cadastro.configure(background = a)
    janela_cadastro.geometry('400x300+200+200')
    texto_inicio = Label(janela_cadastro, background = a, foreground = v, text = '- CADASTRO -')
    texto_inicio.place(x = '150', y = '20')
    
    texto_nome = Label(janela_cadastro, background = a, foreground = v,  text = 'Nome: ')
    texto_nome.place(x = '70', y = '60')
    entrada = Entry(janela_cadastro)
    entrada.place(x = '120', y = '60')

    texto_email = Label(janela_cadastro, background = a, foreground = v, text = 'Email: ')
    texto_email.place(x = '70', y = '90')
    entrada1 = Entry(janela_cadastro)
    entrada1.place(x = '120', y = '90')

    texto_senha = Label(janela_cadastro, background = a, foreground = v, text = 'Senha: ')
    texto_senha.place(x = '70', y = '120')
    entrada2 = Entry(janela_cadastro)
    entrada2.place(x = '120', y = '120')
    
    def bt_click():
      self.__nome = entrada.get().title()
      resposta_nome['text'] = ('nome:', self.__nome)
      while True:
        self.__email = entrada1.get().lower()
        if self.__email[-10:] != '@gmail.com':
          print('\033[0;49;31m/email inválido! (use @gmail.com)/\033[m')
          time.sleep(4)
          os.system('clear')
          janela_cadastro.destroy()
          self.realizar_cadastro()
        else:
          resposta_email['text'] = ('email:', self.__email)
          break

      while True: 
        self.__senha = entrada2.get()
        if (len(self.__senha)<8) or not re.search("[a-z]", self.__senha) or not re.search("[A-Z]", self.__senha) or not re.search("[0-9]", self.__senha) or not re.search("[!#$%&()*+,-./:;<=>?@[\]^_`{|}~']", self.__senha) or re.search("\s", self.__senha):
          print('\033[0;49;31m/senha fraca!/\033[m')
          print('\nAVISO: \n mínimo 8 caracteres \n letras minúsculas [az] \n letras maiúsculas [AZ] \n pelo menos 1 número ou dígito entre [0-9] \n pelo menos 1 caractere especial')
          time.sleep(4)
          os.system('clear')
          janela_cadastro.destroy()
          self.realizar_cadastro()
            
        else:
          resposta_senha['text'] = ('senha:', self.__senha)
          break

      email.append(self.__email)
      usuarios.extend((self.__nome, self.__email, self.__senha))
      self.bancodedados()
    
      texto_nome.destroy()
      texto_email.destroy()
      texto_senha.destroy()
      entrada.destroy()
      entrada1.destroy()
      entrada2.destroy()
      botao.destroy()
      def bt_click1():
        janela_cadastro.destroy()
      
      botao1 = Button(janela_cadastro, text = 'voltar', command = bt_click1)
      botao1.place(x = '60', y = '150')

    botao = Button(janela_cadastro, text = 'enviar', command = bt_click)
    botao.place(x = '70', y = '160')

    resposta_nome = Label(janela_cadastro, background = a, text = '')
    resposta_nome.place(x = '60', y = '60')
    resposta_email = Label(janela_cadastro, background = a, text = '')
    resposta_email.place(x = '60', y = '90')
    resposta_senha = Label(janela_cadastro, background = a, text = '')
    resposta_senha.place(x = '60', y = '120')
    
    janela_cadastro.mainloop()

  def fazer_login(self):
    janela_login = Tk()
    janela_login.title('planner.login')
    janela_login.geometry('400x300+200+200')
    texto_inicio = Label(janela_login, text = '- LOGIN -')
    texto_inicio.place(x = '160', y = '20')
    
    texto_email = Label(janela_login, text = 'email: ')
    texto_email.place(x = '70', y = '60')
    entrada = Entry(janela_login)
    entrada.place(x = '120', y = '60')

    def bt_click():
      email_digitado = entrada.get()
      if email_digitado in email:
        resposta_email['text'] = ('email:', email_digitado)
        texto_email.destroy()
        entrada.destroy()
        botao.destroy()
        resposta_email.destroy()
        self.senha_login(email_digitado, janela_login, resposta_email)

      else:
        print('\033[0;49;31m/email não existente/\033[m')
        time.sleep(4)
        os.system('clear')
        janela_login.destroy()
        self.fazer_login()
      
    botao = Button(janela_login, text = 'enviar', command = bt_click)
    botao.place(x = '70', y = '90')

    resposta_email = Label(janela_login, text = '')
    resposta_email.place(x = '60', y = '60')

    janela_login.mainloop()
    
  def senha_login(self, email_digitado, janela_login, resposta_email):
    texto_senha = Label(janela_login, text = 'senha: ')
    texto_senha.place(x = '70', y = '60')
    entrada = Entry(janela_login)
    entrada.place(x = '120', y = '60')
    
    def bt_click():
      senha_digitada = entrada.get()
      if senha_digitada != usuarios[rsenha + 1]:
        print("\033[0;49;31m/senha incorreta/\033[m")
        time.sleep(4)
        os.system('clear')
        self.senha_login(email_digitado, janela_login, resposta_email)

      else:
        self.escolher_funcoes(email_digitado, rsenha, janela_login)
    
    botao = Button(janela_login, text = 'enviar', command = bt_click)
    botao.place(x = '70', y = '90')
    
    rsenha = usuarios.index(email_digitado)

  def escolher_funcoes(self, email_digitado, rsenha, janela_login):
    janela_escolher_funcoes = Tk()
    janela_escolher_funcoes.title('planner.escolha')
    janela_escolher_funcoes.geometry('400x300+200+200')
    texto_inicio = Label(janela_escolher_funcoes, text = 'PLANNER - BEM VINDO')
    texto_inicio.place(x = '150', y = '20')
    texto_dados = Label(janela_escolher_funcoes, text = '1 - dados do usuário')
    texto_dados.place(x = '50', y = '50')
    texto_agenda = Label(janela_escolher_funcoes, text = '2 - agenda')
    texto_agenda.place(x = '50', y = '70')
    texto_sair = Label(janela_escolher_funcoes, text = '3 - sair')
    texto_sair.place(x = '50', y = '90')
    entrada = Entry(janela_escolher_funcoes)
    entrada.place(x = '50', y = '120')

    def bt_click():
      try:
        if int(entrada.get()) == 1:
          self.exibir_dados(email_digitado, rsenha)
        elif int(entrada.get()) == 2:
          os.system('clear')
          self.consultar_agendamento(email_digitado)
          self.escolher_funcoes(email_digitado, rsenha)
        elif int(entrada.get()) == 3:
          janela_login.destroy()
          janela_escolher_funcoes.destroy()
        else:
          raise ValueError()
          
      except(TypeError, ValueError):
        print('\033[0;49;94m\n*eita mano, deu erro aq* \nvoltando...\033[m')
        time.sleep(4)
        os.system('clear')
        self.escolher_funcoes(email_digitado, rsenha)

    botao = Button(janela_escolher_funcoes, text = 'enviar', command = bt_click)
    botao.place(x = '50', y = '150')

    resposta_botao = Label(janela_escolher_funcoes, text = '')
    resposta_botao.place(x = '50', y = '180')
    time.sleep(5)
    janela_escolher_funcoes.mainloop()
      
  def exibir_dados(self, email_digitado, rsenha):
    janela_exibir_dados = Tk()
    janela_exibir_dados.title('planner.dados.do.usuario')
    janela_exibir_dados.geometry('400x300+200+200')
    texto_inicio = Label(janela_exibir_dados, text = 'DADOS DO USUÁRIO')
    texto_inicio.place(x = '150', y = '20')
    
    texto_nome = Label(janela_exibir_dados, text = ('nome: ', usuarios[rsenha - 1]))
    texto_nome.place(x = '50', y = '50')
          
    texto_email = Label(janela_exibir_dados, text = ('email: ', usuarios[rsenha]))
    texto_email = Label(janela_exibir_dados, text = '')
    
    
    texto_senha = Label(janela_exibir_dados, text = ('senha: ', usuarios[rsenha + 1]))
    texto_senha.place(x = '50', y = '90')

    def bt_click():
      janela_exibir_dados.mainloop()
      janela_exibir_dados.destroy()
      
    botao = Button(janela_exibir_dados, text = 'voltar', command = bt_click)
    botao.place(x = '50', y = '130')

    try:
      input('enter para voltar')
      self.escolher_funcoes(email_digitado, rsenha)

    except(ValueError, TypeError):
      print('\033[0;49;94m\n*eita mano, deu erro aq* \nvoltando...\033[m')
      time.sleep(4)
      os.system('clear')
      self.exibir_dados(email_digitado, rsenha)

  def consultar_agendamento(self, email_digitado):
    if email_digitado not in eventos_usuarios.keys():
      eventos_usuarios[email_digitado] = Agendamento()
      self.consultar_agendamento(email_digitado)
    else:
      eventos_usuarios[email_digitado].menu_agendamento()

  def bancodedados(self):
   #conectando
    conexao = sqlite3.connect('usuarios.db')
    
    #definindo um cursor
    cursor = conexao.cursor()
    
    #criando tabela
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
    );
    """)
    
    #inserindo dados
    cursor.execute("""
    INSERT INTO usuarios (nome, email)
    VALUES (?,?)
    """, (self.__nome, self.__email))
    
    conexao.commit()
    
    #desconectando
    conexao.close()
    
  def ler_bd(self):
    #conectando
    conexao = sqlite3.connect('usuarios.db')
    
    #definindo um cursor
    cursor = conexao.cursor()

    print('\ndeu tudo certo *-*\n')
    
    #lendo dados
    cursor.execute("""
    SELECT * FROM usuarios;
    """)
    
    for linha in cursor.fetchall():
        print(linha)
    
    #desconectando
    conexao.close()

    input('\nenter para voltar')
    
  def excluir_dados(self):
    #conectando
    conexao = sqlite3.connect('usuarios.db')
    
    #definindo um cursor
    cursor = conexao.cursor()

    id_usuario = int(input('\nid do usuário: '))
    
    cursor.execute("""
    DELETE FROM usuarios
    WHERE id = ?
    """, (id_usuario,))

    conexao.commit()
    
    print('\nexcluido com sucesso *-*')
    
    #desconectando
    conexao.close()

    input('\nenter para voltar')
      