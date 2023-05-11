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

Obs.: Só use o comando CREATE TABLE se não houver o arquivo produto.db na pasta do arquivo.
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

>> É doce, mas não é mole não !!!

"""


import pandas as pd
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
import customtkinter
from datetime import date

# --------------------------------------------- 1 - CRIAÇÃO E CONEXAO COM SQLITE -------------------------------------------------------------#
#  SE O CÓDIGO DA CRIAÇÃO RODAR E CRIAR O produto.db na máquina, se faz necessário tornar esse código COMENTÁRIO para não gerar um duplo banco
# PARA INICIAR E CRIAR UM .db EM MAQUINA NOVA SEM TER BANCO DE DADOS, DESCOMENTE O CÓDIGO E COMENTE O 2

# conexao = sqlite3.connect('produtos.db')
# c = conexao.cursor()
# c.execute('''CREATE TABLE produtos (
#     nome text,
#     quantidade interger,
#     precovenda real,
#     precocompra real,
#     linha text,
#     genero text,
#     tipo text,
#     validade text,
#     lote text
#     )
#  ''')

# conexao.commit()
# conexao.close()


# -------------------------------------------- 2- CRIAÇÃO DA TABELA USUARIOS --------------------------------------------------

# conexao = sqlite3.connect('usuarios.db')
# c = conexao.cursor()
# c.execute('''CREATE TABLE usuarios (
#     nome text,
#     cpf text,
#     telefone text,
#     senha text,
#     nivel int
#     )
#  ''')


# ------------------------------------------ 3 - CRIAÇÃO DA TABELA DE VENDAS --------------------------------------------------
# conexao = sqlite3.connect('vendas.db')
# c = conexao.cursor()
# c.execute('''CREATE TABLE vendas (
#     nome text,
#     precoVenda real,
#     lote text
#     )
#  ''')




dicionarioVenda = {}
dicionarioCompra = {}
dicionarioUsuario = {}
listaVenda = []
listaCompra = []
dicionarioEstoque = {}
dicAcesso = {}


def registroVenda():
    return dicionarioVenda


def registroCompra():
    return dicionarioCompra


def bancoDeUsuarios():
    return dicionarioUsuario


def estoqueTotal():
    return dicionarioEstoque


def criaJanelaTransacao():
    # ----------------------FUNCIONAMENTO DA JANELA TRANSAÇAO-----------------------------
    # -----------------------------------VENDAS--------------------------------------------
    def registraTransacaoVenda():
        chaveVenda = produtoEntrada.get()
        quantidadeVenda = quantidadeEntrada.get()
        precoVenda = precoEntrada.get()
        linVenda = precoLinha.get()
        genVenda = generoEntrada.get()
        tipoVenda = tipoEntrada.get()
        validadeVenda = validadeEntrada.get()
        loteVenda = loteEntrada.get()

        tuplaVenda = (quantidadeVenda, precoVenda, linVenda,
                      genVenda, tipoVenda, validadeVenda, loteVenda)
        if chaveVenda in dicionarioVenda and chaveVenda in dicionarioEstoque:
            listaVenda = dicionarioVenda[chaveVenda]
            listaVenda.append(tuplaVenda)
            # ---------------------->>> ESCREVER NO ARQUIVO
            dicionarioVenda[chaveVenda] = listaVenda
        else:
            if chaveVenda in dicionarioEstoque:
                listaVenda = []
                listaVenda.append(tuplaVenda)
                dicionarioVenda[chaveVenda] = listaVenda
        if chaveVenda in dicionarioEstoque:
            dicionarioEstoque[chaveVenda] += -int(tuplaVenda[0])
            if dicionarioEstoque[chaveVenda] <= 0:
                dicionarioEstoque.pop(chaveVenda)

        else:
            dicionarioEstoque[chaveVenda] = -int(tuplaVenda[0])
            if dicionarioEstoque[chaveVenda] < 0:
                dicionarioEstoque.pop(chaveVenda)

        print(dicionarioVenda)
        print(dicionarioEstoque)

    # ------------------------------------COMPRAS-------------------------------------------
    def registraTransacaoCompra():
        chaveCompra = produtoEntrada.get()
        quantidadeCompra = quantidadeEntrada.get()
        precoCompra = precoEntrada.get()
        linCompra = precoLinha.get()
        genCompra = generoEntrada.get()
        tipoCompra = tipoEntrada.get()
        validadeCompra = validadeEntrada.get()
        loteCompra = loteEntrada.get()
        

        tuplaCompra = (quantidadeCompra, precoCompra, linCompra,
                       genCompra, tipoCompra, validadeCompra, loteCompra)
        if chaveCompra in dicionarioCompra:
            listaCompra = dicionarioCompra[chaveCompra]
            listaCompra.append(tuplaCompra)
            # ---------------------->>> ESCREVER NO ARQUIVO
            dicionarioCompra[chaveCompra] = listaCompra
        else:
            listaCompra = []
            listaCompra.append(tuplaCompra)
            dicionarioCompra[chaveCompra] = listaCompra
        if chaveCompra in dicionarioEstoque:
            dicionarioEstoque[chaveCompra] += int(tuplaCompra[0])

        else:
            dicionarioEstoque[chaveCompra] = int(tuplaCompra[0])

        print(dicionarioCompra)
        print(dicionarioEstoque)

    # --------------------------------- INSERIR DADOS EM COMPRAS/PRODUTOS -------------------------------------------#
    def cadastrar_produto():
            conexao = sqlite3.connect('produtos.db')
            c = conexao.cursor()
            c.execute(" INSERT INTO produtos VALUES (:nome, :quantidade,:precoVenda, :precoCompra, :linha, :genero, :tipo, :validade,:lote)",
                  {
                    'nome': produtoEntrada.get(),
                    'quantidade': quantidadeEntrada.get(),
                    'precoVenda': precoEntrada.get(),
                    'precoCompra': precoEntrada.get(),
                    'linha': precoLinha.get(),
                    'genero': generoEntrada.get(),
                    'tipo': tipoEntrada.get(),
                    'validade': validadeEntrada.get(),
                    'lote': loteEntrada.get(),
                    
                  }
                  )
            conexao.commit()
            conexao.close()

    # ---------------------------- INSERIR DADOS EM VENDAS -------------------------------------------------------------#

    def cadastrar_vendas():
            conexao = sqlite3.connect('vendas.db')
            c = conexao.cursor()
            c.execute(" INSERT INTO vendas VALUES (:nome, :precoVenda,:lote)",
                  {
                    'nome': produtoEntrada.get(),
                    'precoVenda':precoEntrada.get(),
                    'lote': loteEntrada.get(),
                  }
                  )
            conexao.commit()
            conexao.close()

    # -----------------LAYOUT JANELA TRANSAÇAO--------------------
    janelaTransacao = customtkinter.CTk(fg_color='#efe1e1')

    largura = 680
    altura = 400
    largura_tela = janelaTransacao.winfo_screenwidth()
    altura_tela = janelaTransacao.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura / 2
    janelaTransacao.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
    janelaTransacao.title("Registrar Transação")
    janelaTransacao.resizable(width=False, height=False)

    # --------------------LAYOUT DOS BOTOES--------------------------
    produto = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Produto:")
    produto.place(x=60, y=20)

    produtoEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Nome do produto...', width=150)
    produtoEntrada.place(x=200, y=20)

    produtoQuantidade = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Quantidade:")
    produtoQuantidade.place(x=60, y=50)

    quantidadeEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Quantidade do produto...', width=150)
    quantidadeEntrada.place(x=200, y=50)

    produtoLinha = produto = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Linha:")
    produtoLinha = produtoLinha.place(x=60, y=80)

    precoLinha = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Linha do produto...', width=150)
    precoLinha.place(x=200, y=80)

    produtoGenero = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Genero:")
    produtoGenero.place(x=60, y=110)

    generoEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Genero do produto...', width=150)
    generoEntrada.place(x=200, y=110)

    tipoProduto = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Tipo:")
    tipoProduto.place(x=60, y=140)

    tipoEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Tipo do produto...', width=150)
    tipoEntrada.place(x=200, y=140)

    precoProduto = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Preço:")
    precoProduto.place(x=60, y=170)

    precoEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Preço do produto...', width=150)
    precoEntrada.place(x=200, y=170)

    validade = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Validade:")
    validade.place(x=60, y=200)

    validadeEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Validadedo produto...', width=150)
    validadeEntrada.place(x=200, y=200)

    lote = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Lote:")
    lote.place(x=60, y=230)

    loteEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Lote do Produto...', width=150)
    loteEntrada.place(x=200, y=230)

    descricao = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Descrição dos produto  :")
    descricao.place(x=450, y=20)

    descricaoEntrada = customtkinter.CTkTextbox(janelaTransacao, fg_color='white', text_color='black', width=250, height=180,
                                                border_color='black', border_width=2, corner_radius=15)
    descricaoEntrada.place(x=390, y=40)

    botaoVenda = customtkinter.CTkButton(janelaTransacao, fg_color='#305bd5',hover_color='#292929' ,text="Registrar Venda",
                                         command=lambda:[registraTransacaoVenda(),cadastrar_vendas()])
    botaoVenda.place(x=180, y=300)


    botaoCompra = customtkinter.CTkButton(janelaTransacao, fg_color='#0f9e41',hover_color='#292929' , text="Registrar Compra",
                                          command=lambda:[registraTransacaoCompra(),cadastrar_produto()])
    botaoCompra.place(x=340, y=300)


    botaoCancela = customtkinter.CTkButton(janelaTransacao, fg_color='#ec1e1e',hover_color='#292929' , text="Voltar",
                                           command=janelaTransacao.destroy)
    botaoCancela.place(x=250, y=350)
    # botaoCancela["bg"] = "#FFE4B5"

    # For realizar o comando INSERT no banco de dados, deve primeiro ter o próprio CREATE TABLE
    # For utilizar o INSERT, por no command a função do INSERT definida na linha 79 = ficará assim: command=cadastrar_produto
    '''botaoCadastroBDD = customtkinter.CTkButton(janelaTransacao, fg_color='orange', text="Compras/BDD",
                                            command=cadastrar_produto)
    botaoCadastroBDD.place(x=340, y=320)

    botaoVendasBDD = customtkinter.CTkButton(janelaTransacao, fg_color='orange', text="Vendas/BDD",
                                            command=cadastrar_vendas)
    botaoVendasBDD.place(x=500, y=320)'''

    janelaTransacao.mainloop()


# --------------------FUNÇÃO JANELA INFORMAÇÕES ESTOQUE (ESTOQUE/HISTÓRICO DE TRANSAÇÕES)----------------------------


def criaJanelaEstoque():
    # ------------------------------FUNÇÃO PESQUISA DE PRODUTOS----------------------------------------
    def auxiliar():
        def pesquisaProduto():
            pesquisaProdutoNome = entradaNomeProduto.get()
            if pesquisaProdutoNome in dicionarioEstoque:
                produtoResultadoNome["text"] = "Nome:", pesquisaProdutoNome
                produtoResultadoQuantidade["text"] = "Quantidade em estoque:", dicionarioEstoque[pesquisaProdutoNome]
                # janelaPesquisaProduto.geometry("415x140+525+270")
            else:
                produtoResultadoNome["text"] = pesquisaProdutoNome, f"Não temos {pesquisaProdutoNome} em estoque!"
                produtoResultadoQuantidade["text"] = ""

    # -------------------------LAYOUT DA JANELA PRODUTO PESQUISADO----------------------------------
        pesquisado = Toplevel(janelaDados)
        pesquisado.title('PRODUTO PESQUISADO')

        largura = 600
        altura = 500

        largura_tela = pesquisado.winfo_screenwidth()
        altura_tela = pesquisado.winfo_screenheight()
        posX = largura_tela / 2 - largura / 2
        posY = altura_tela / 2 - altura / 2
        pesquisado.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))

        pesquisado.title("Produto Pesquisado")
        pesquisado["bg"] = '#efe1e1'
        pesquisado.resizable(width=False, height=False)

        nomeProduto = tk.Label(pesquisado, text="Nome do produto:")
        nomeProduto.place(x=10, y=15)
        nomeProduto["bg"] = "#efe1e1"

        entradaNomeProduto = customtkinter.CTkEntry(
            pesquisado, fg_color="white", text_color='black')
        entradaNomeProduto.place(x=130, y=10.5)

        produtoResultadoNome = tk.Label(pesquisado, text="", font='Arial 12' )
        produtoResultadoNome.place(x=10, y=50)
        produtoResultadoNome["bg"] = "#efe1e1"

        produtoResultadoQuantidade = tk.Label(pesquisado, text="")
        produtoResultadoQuantidade.place(x=10, y=70)
        produtoResultadoQuantidade["bg"] = "#efe1e1"

        botaoProcurar = customtkinter.CTkButton(
            pesquisado, fg_color='green',hover_color='#292929', text="Pesquisar", command=pesquisaProduto)
        botaoProcurar.place(x=280, y=10.5)

 

    # --------------------CRIA JANELA INFORMAÇÕES DE ESTOQUE (ESTOQUE/HISTÓRICO DE TRANSAÇÕES)--------------------------
    janelaDados = tk.Tk()

    largura = 600
    altura = 500

    largura_tela = janelaDados.winfo_screenwidth()
    altura_tela = janelaDados.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura / 2
    janelaDados.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
    janelaDados.title("Informações de Estoque")
    # janelaHistorico.geometry("400x400+525+0")
    janelaDados["bg"] = '#efe1e1'
    janelaDados.resizable(width=False, height=False)

    # -----------------------------Criação de um Notebook(elemento ttk, para adição de abas)--------------------------------
    hist = ttk.Notebook(janelaDados)
    hist.place(x=0, y=0, width=600, height=500)

    # ---------------------------------------criando aba Compras-----------------------------------------
    tb1 = tk.Frame(hist)
    hist.add(tb1, text='Compras')
    tb1["bg"] = "#efe1e1"

    # ---------------------------------------criando aba Vendas------------------------------------------
    tb2 = tk.Frame(hist)
    hist.add(tb2, text='Vendas')
    tb2["bg"] = "#efe1e1"

    # ---------------------------------------criando aba Estoque-----------------------------------------
    tb3 = tk.Frame(hist)
    hist.add(tb3, text='Estoque')
    tb3["bg"] = "#efe1e1"
    tree = ttk.Treeview(tb1)
    tree.place(relx=.35, rely=.5, anchor='center', height=450, width=400)
    tree['columns'] = ('Quantidade', 'Preço')
    tree.column('#0', width=120, minwidth=120, anchor='w')
    tree.column('Quantidade', width=120, minwidth=120, anchor='w')
    tree.column('Preço', width=120, minwidth=120, anchor='w')
    tree.heading('#0', text='Produto', anchor='w')  # PRODUTO
    tree.heading('Quantidade', text='Quantidade', anchor='w')  # QUANDIDADE
    tree.heading('Preço', text='Preço', anchor='w')  # PREÇO

    for produto, compras in dicionarioCompra.items():
        for dadosc in compras:
            tree.insert('', 'end', text=produto, values=(dadosc[0], dadosc[1]))


    tree = ttk.Treeview(tb2)
    tree.place(relx=.35, rely=.5, anchor='center', height=450, width=400)
    tree['columns'] = ('Quantidade', 'Preço')
    tree.column('#0', width=120, minwidth=120, anchor='w')
    tree.column('Quantidade', width=120, minwidth=120, anchor='w')
    tree.column('Preço', width=120, minwidth=120, anchor='w')
    tree.heading('#0', text='Produto', anchor='w')
    tree.heading('Quantidade', text='Quantidade', anchor='w')
    tree.heading('Preço', text='Preço', anchor='w')

    for produto, vendas in dicionarioVenda.items():
        for dadosv in vendas:
            tree.insert('', 'end', text=produto, values=(dadosv[0], dadosv[1]))

 
    # -----------------------------------------------------------------------------------------------------------------------------
    tree = ttk.Treeview(tb3)
    tree.place(relx=.35, rely=.5, anchor='center', height=450, width=400)
    tree['columns'] = ('Quantidade',)
    # ----'#0' identificador padrão para a primeira coluna
    tree.column('#0', width=90, minwidth=0, anchor='w')
    tree.column('Quantidade', width=90, minwidth=0, anchor='w')
    tree.heading('#0', text='Produto', anchor='w')
    tree.heading('Quantidade', text='Quantidade', anchor='w')

    for produto, estocagem in dicionarioEstoque.items():
        tree.insert('', 'end', text=produto, values=(estocagem,))

   
# -------------------------------------------------------------------

    # ---------------------------------------------------Bloco de Botões--------------------------------------------------------
    # ---cancela procedimento
    botaoCancela = customtkinter.CTkButton(
        janelaDados, fg_color='#595959',hover_color='#292929' , text="Voltar", command=janelaDados.destroy)
    botaoCancela.place(x=450, y=450)
    # botaoCancela["bg"] = "#FFE4B5"

    # ---pesquisa especifica
    botaoProcurar = customtkinter.CTkButton(
        janelaDados, fg_color='green', text="Pesquisar Produto",hover_color='#292929', command=auxiliar)
    botaoProcurar.place(x=450, y=40)



def criaJanelaGerenciamento():
    # ---------------------------FUNCIONAMENTO GERENCIAMENTO DE USUARIO -----------------------------
    def gerenciaUsuario():
        chaveNome = entradaNomeUsuario.get()
        cpf = entradaCpf.get()
        telefone = entradaTelefone.get()
        senha = entradaSenha.get()
        nivel = entradaNivel.get()
        # (chaveNome,cpf,telefone,senha,nivel)
        tuplaUsuario = (chaveNome, senha, cpf, telefone, nivel)

        if chaveNome in dicionarioUsuario:
            # ---------------------->>> ESCREVER NO ARQUIVO
            dicionarioUsuario[chaveNome] = tuplaUsuario
        else:
            listaUsuario = []
            listaUsuario.append(tuplaUsuario)
            dicionarioUsuario[chaveNome] = listaUsuario
        print(dicionarioUsuario)



    # ---------------------------   FUNÇÃO DE CADASTRAR USUÁRIO NO BANCO DE DADOS SQLITE ----------------------------------#
    def cadastrar_usuario():
            conexao = sqlite3.connect('usuarios.db')
            c = conexao.cursor()
            c.execute(" INSERT INTO usuarios VALUES (:nome, :cpf, :telefone,:senha,:nivel)",
                  {
                    'nome': entradaNomeUsuario.get(),
                    'cpf': entradaCpf.get(),
                    'telefone': entradaTelefone.get(),
                    'senha': entradaSenha.get(),
                    'nivel': entradaNivel.get(),
                  }
                  )
            conexao.commit()
            conexao.close()


    # ---------------------------------FUNCIONAMENTO PESQUISA DE USUARIO----------------------------

    def pesquisaUsuario():
        pesquisaNome = pesquisaEntrada.get()
        if pesquisaNome in dicionarioUsuario:
            resultadoNome["text"] = "Nome:", pesquisaNome
            resultadoCpf["text"] = "CPF:", dicionarioUsuario[pesquisaNome][0][3]
            resultadoTelefone["text"] = "Telefone:", dicionarioUsuario[pesquisaNome][0][2]
            resultadoNivel["text"] = "Senha:", dicionarioUsuario[pesquisaNome][0][1]
        else:
            resultadoNome["text"] = ""
            resultadoCpf["text"] = "ERRO: Usuário não cadastrado no sistema"
            resultadoTelefone["text"] = ""
            resultadoNivel["text"] = ""

    # ------------------------------FUNCIONAMENTO BOTAO EXCLUIR----------------------------------------
    def excluirUsuario():
        excluiNome = pesquisaEntrada.get()
        if excluiNome in dicionarioUsuario:
            dicionarioUsuario.pop(excluiNome)
            print(dicionarioUsuario)
            resultadoNome["text"] = ""
            resultadoCpf["text"] = ""
            resultadoTelefone["text"] = ""
            resultadoNivel["text"] = ""
            resultadoExclusao["text"] = "USUÁRIO EXCLUÍDO COM SUCESSO!"
        else:
            resultadoNome["text"] = ""
            resultadoCpf["text"] = ""
            resultadoTelefone["text"] = ""
            resultadoNivel["text"] = ""
            resultadoExclusao["text"] = "IMPOSSÍVEL EXCLUIR"

    # ------------------------------------LAYOUT JANELA GERENCIAMENTO---------------------------------
    janelaGerenciamento = tk.Tk()

    largura = 530
    altura = 420

    largura_tela = janelaGerenciamento.winfo_screenwidth()
    altura_tela = janelaGerenciamento.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura / 2
    janelaGerenciamento.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
    janelaGerenciamento["bg"] = "#efe1e1"
    # janelaGerenciamento.geometry("530x420+525+0")
    janelaGerenciamento.title("Gerenciamento de Usuário")
    janelaGerenciamento.resizable(width=False, height=False)

    # ---------------------------------------BOTÕES ADICIONAR USUARIO--------------------------------------------------------
    nomeUsuario = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="Nome do usuário:")
    nomeUsuario.place(x=20, y=20)
    # nomeUsuario["bg"] = "#87CEFA"

    entradaNomeUsuario = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    entradaNomeUsuario.place(x=150, y=20)

    cpfUsuario = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="CPF do usuário:")
    cpfUsuario.place(x=20, y=50)
    # cpfUsuario["bg"] = "#87CEFA"

    entradaCpf = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    entradaCpf.place(x=150, y=50)

    telefoneUsuario = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="Telefone do usuário:")
    telefoneUsuario.place(x=20, y=80)
    # telefoneUsuario["bg"] = "#87CEFA"

    entradaTelefone = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    entradaTelefone.place(x=150, y=80)

    senhaUsuario = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="Senha do usuário:")
    senhaUsuario.place(x=20, y=110)
    # senhaUsuario["bg"] = "#87CEFA"

    entradaSenha = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    entradaSenha.place(x=150, y=110)

    nivelUsuario = customtkinter.CTkLabel(janelaGerenciamento, fg_color='#efe1e1', text_color='black',
                                          text="Digite o nível de acesso:\n\nNível 1:Acesso mínimo | Nível 2:Acesso intermediário | Nível 3: Acesso máximo")
    nivelUsuario.place(x=20, y=145)
    # nivelUsuario["bg"] = "#87CEFA"

    entradaNivel = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=50, height=20)
    entradaNivel.place(x=340, y=140)

    botaoAddUsuario = customtkinter.CTkButton(
        janelaGerenciamento, fg_color='#305bd5', text="Adicionar Usuário",hover_color='#292929' , command=lambda:[gerenciaUsuario(),cadastrar_usuario()])
    botaoAddUsuario.place(x=200, y=200)

    # -----------------------------------BOTÕES PESQUISAR USUARIO-----------------------------------
    nomePesquisa = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="Nome:")
    nomePesquisa.place(x=20, y=270)
    # nomePesquisa["bg"] = "#87CEFA"

    pesquisaEntrada = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    pesquisaEntrada.place(x=70, y=270)
    # pesquisaEntrada["bg"] = "#87CEFA"

    botaoPesquisar = customtkinter.CTkButton(
        janelaGerenciamento, fg_color='#0f9e41', text="Pesquisar",hover_color='#292929' , command=pesquisaUsuario)
    botaoPesquisar.place(x=370, y=267)

    # ----------------------------------RESULTADO DA PESQUISA---------------------------------------
    resultadoNome = tk.Label(janelaGerenciamento, text="")
    resultadoNome.place(x=70, y=300)
    resultadoNome["bg"] = "#efe1e1"

    resultadoCpf = tk.Label(janelaGerenciamento, text="")
    resultadoCpf.place(x=70, y=320)
    resultadoCpf["bg"] = "#efe1e1"

    resultadoTelefone = tk.Label(janelaGerenciamento, text="")
    resultadoTelefone.place(x=70, y=340)
    resultadoTelefone["bg"] = "#efe1e1"

    resultadoNivel = tk.Label(janelaGerenciamento, text="")
    resultadoNivel.place(x=70, y=360)
    resultadoNivel["bg"] = "#efe1e1"

    # ------------------------------BOTAO PARA EXCLUIR USUARIO---------------------------------------
    botaoExcluir = customtkinter.CTkButton(
        janelaGerenciamento, fg_color='#ec1e1e',hover_color='#292929' , text="Excluir\nUsuário", command=excluirUsuario)
    botaoExcluir.place(x=370, y=320)
    botaoVoltar = customtkinter.CTkButton(
        janelaGerenciamento, fg_color='#595959',hover_color='#292929' , text="Voltar", command=janelaGerenciamento.destroy)
    botaoVoltar.place(x=370, y=370)

    # -----------------------------RESULTADO DA AÇAO EXCLUIR---------------------------------------
    resultadoExclusao = tk.Label(janelaGerenciamento, text="")
    resultadoExclusao.place(x=160, y=400)
    resultadoExclusao["bg"] = "#efe1e1"




def telaMenu(x):
    # --------------------LAYOUT JANELA ADMIN----------------------
    x.destroy()
    janela = customtkinter.CTk(fg_color='#efe1e1')

    largura = 600  # 400 original
    altura = 400 # 350 original

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura / 2
    janela.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
    # janela.geometry("400x350") #400x350
    janela.title("Controle de Estoque - Unibra (Administrador)")
    janela.resizable(width=False, height=False)

    # ----------------------LAYOUT DOS BOTOES--------------------------
    botaoTransacao = customtkinter.CTkButton(
        janela, width=360,height=60,fg_color='#CD5C5C',hover_color='#292929' ,text="Registrar Transação", command=criaJanelaTransacao)
    botaoTransacao.place(x=120, y=20)
    # botaoTransacao["bg"] = "#B0E0E6"

    botaoCadastro = customtkinter.CTkButton(
        janela, text="Gerenciamento de Usuário", fg_color='#CD5C5C',hover_color='#292929' , width=360, height=60, command=criaJanelaGerenciamento)
    botaoCadastro.place(x=120, y=90)
   

    # RAZAO DO Y = 60
    botaoHistorico = customtkinter.CTkButton(
        janela, text="Informações de Estoque", fg_color='#CD5C5C',hover_color='#292929' , width=360, height=60, command=criaJanelaEstoque)
    botaoHistorico.place(x=120, y=160)
    # botaoHistorico["bg"] = "#B0E0E6"

    botaoHistoria = customtkinter.CTkButton(janela, text="Conheça nossos Produtos",
                                            fg_color='#CD5C5C',hover_color='#292929' , width=360, height=60, command=lambda: webbrowser.open('index.html'))
    botaoHistoria.place(x=120, y=230)
    # botaoHistoria["bg"] = "#FFC0CB"

    # DATA DE ACESSO
    data_acesso = date.today()
    data_str = data_acesso.strftime('%d/%m/%Y')

    logAcesso = customtkinter.CTkLabel(
        janela, text_color='black', text=f'\n Acessado em: \n{data_str} ', fg_color='#efe1e1' ,width=360, height=50)
    logAcesso.place(x=120, y=330)

    janela.mainloop()

# ----------------------------------FUNÇAO DE LOGIN---------------------------------


# ------------------- REGISTRO DE USUÁRIO ------------------------------------------#
"""
OBSERVAR QUE NA FUNÇÃO INICIAL DE REGISTRO DE USUÁRIO O {nomeChave} e {senha} será atribuidos a (tulplaUsuario}, 
e consequentemente direcionado ao {dicionarioUsuario}.
A função que traz o valor das duas funções não está rodando no código principal do login.

Obs1.: Relizar o percorrimento da tulpla/dicionário e trazer o valor de nomeChave e senha
Obs2.: Finalizar o projeto com usuario e password != "" e dar entrada com qualquer comando digitado.

Pontos a analisar com calma, evitar raiva e estresse.
"""


def acesso(key1, key2, erro, inicio):

    usuario = key1.get()
    password = key2.get()
    aviso = erro

    if usuario != "" and password != "":
        telaMenu(inicio)
    elif usuario == "cadastro" and password == "cadastro":
        criaJanelaGerenciamento()
    else:
        aviso["text"] = "Usuário ou senha incorretos"
