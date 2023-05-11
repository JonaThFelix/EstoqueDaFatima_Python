"""
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

PROJETO DO INTERDISCIPLINAR DE 2023.1 DA TURMA DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - ADS2NAB (2022.2)
FACULDADE: UNIBRA (CENTRO UNIVERSITÁRIO BRASILEIRO)
GRUPO DE DESENVOLVIMENTO POO: JONATHAN, HENRIQUE, ELIAS, VICTOR
ORIENTADORA: ALINE FARIAS


>> PARA FUNCIONAMENTO DO CÓDIGO É NECESSÁRIO INSTALAR ALGUNS PACKAGES DO PYTHON

1 - Ter o Python da versão 3.10 ou superior: (https://www.python.org/)
2 - Instalar na máquina local, (não rodar no replit ou compilador online)

Recomendações: Recomendamos os compiladores:
* Pycharm (https://www.jetbrains.com/pt-br/pycharm/)
* VScode (https://code.visualstudio.com/)

-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

>> RECURSOS PARA O SOFTWARE
>> instalando package
>> Verificação de pacotes e versões: pip freeze


1 - pip install tkinter | versão utilizada: nativo com python
2 - pip install customtkinter | versão utilizada: 5.1.2
3 - pip install webbrowser | versão utilizada: 6.0
4 - pip install sqlite3 | versão utilizada: 1.2.0
5 - pip install pandas | versão utilizada: 2.0.0
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

>> RECURSOS PARA BANCO DE DADOS

1 - DB BROWSER : Download: https://sqlitebrowser.org/dl/

-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

>> É doce, mas não é mole não !!!

"""
#--------------------------------------------------------------------------------

#IMPORTS AQUI
from cProfile import label
import webbrowser
import tkinter as tk
from base import *
import customtkinter
from datetime import date
from PIL import Image, ImageTk
#--------------------------------------------------------------------------------
#CONSULTA NOS DICIONARIOS/TUPLAS
Venda = registroVenda()
Compra = registroCompra()
Usuarios = bancoDeUsuarios()
Estoque = estoqueTotal()
#--------------------------------------------------------------------------------

# ---------------------------------FUNÇAO JANELA DE TRANSAÇOES-----------------------------------


# ---------------------------LAYOUT JANELA DE LOGIN--------------------------------
window = customtkinter.CTk(fg_color='#efe1e1')
#img = tk.PhotoImage(file='icon/logoinicio.png')
#label_img = customtkinter.CTkLabel(master=window, image=img, text="")
#label_img.place(x=310, y=25)
#--------------------------------------------------------------------------------
#ADICIONA IMAGEM DE LOGIN
my_image = customtkinter.CTkImage(light_image=Image.open('icon/login.png'),
                                  dark_image=Image.open('icon/login.png'),
                                  size=(150, 100))
LabelImagem = customtkinter.CTkLabel(
                       window, text='', image=my_image).place(x=265, y=25)

#--------------------------------------------------------------------------------
#INICIANDO TELA NO CENTRO DO MONITOR
largura = 700 
altura = 400
largura_tela = window.winfo_screenwidth()
altura_tela = window.winfo_screenheight()
posX = largura_tela / 2 - largura / 2
posY = altura_tela / 2 - altura / 2
window.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
#--------------------------------------------------------------------------------
#TITULO NOME DA JANELA LOGIN
window.title("Unibra | ADS | Controle de Estoque")
window.configure(background='#efe1e1')  # BACKGROUND LOGIN
window.resizable(width=False, height=False)
#--------------------------------------------------------------------------------
#BACKGROUND TELA DE LOGIN
quadrado = customtkinter.CTkFrame(
    window, width=320, height=230, fg_color='pink',border_width=0, corner_radius=15)
quadrado.place(x=180, y=125)
#--------------------------------------------------------------------------------
# CAMPO DE USUARIO
entrada1 = customtkinter.CTkEntry(
    window, fg_color='white', placeholder_text='Usuario',width=250,border_width=0, height=35, text_color='black')
entrada1.place(x=215, y=154)
#--------------------------------------------------------------------------------
#CAMPO SENHA
entrada2 = customtkinter.CTkEntry(
    window, fg_color='white', placeholder_text='Senha',width=250,border_width=0, height=35, text_color='black', show='*')
entrada2.place(x=215, y=190)  
#--------------------------------------------------------------------------------
#BOTÃO LOGIN
botao1 = customtkinter.CTkButton(window, fg_color='#CD5C5C',hover_color='#292929' , text=" » LOGIN « ", width=300, height=30, command=lambda: acesso(entrada1, entrada2, aviso, window)
                                 ).place(x=191, y=275)
#--------------------------------------------------------------------------------
#BOTÃO REGISTRAR
botaoRegistrar = customtkinter.CTkButton(window, fg_color='pink',bg_color='pink', hover_color='pink' ,width=30, height=10 ,text_color='black', text=" » REGISTRAR « ", command=lambda: acesso(criaJanelaGerenciamento())
                                         ).place(x=370, y=235)
#--------------------------------------------------------------------------------
# BOTÃO SAIR
botao2 = customtkinter.CTkButton(
    window, fg_color='#CD5C5C',hover_color='#292929', text=" » SAIR « ",width=300, height=30, command=window.destroy)
botao2.place(x=191, y=310)
#--------------------------------------------------------------------------------
# RODAPÉ
credito = customtkinter.CTkLabel(
    window, text_color='black', text='"Unibra 2023.1 | ADS2NAB | Devs: Jonathan Felix, Henrique Pinheiro, Victor Lopes, Elias Rodrigues, Pablo Ferreira "')
credito.place(x=30, y=375)
#--------------------------------------------------------------------------------
# AVISO SENHA INCORRETA
aviso = tk.Label(text="")
aviso.place(x=218, y=225)
aviso["bg"] = "pink"
aviso['fg'] = '#8B0000'
#--------------------------------------------------------------------------------

window.mainloop() 
