### ficha de cadastro com python ###
import tkinter as tk
from tkinter import ttk  
import datetime as dt

lista_tipos= ["Galão", "Caixa", "saco", "Unidade"]
listas_codigos= []
janela = tk.Tk()

## Criação da função 

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quantidade.get()
    data_criacao =  dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(listas_codigos)+1
    codigo_str = "COD-{}".format(codigo)
    listas_codigos.append((codigo_str,descricao,tipo,quant,data_criacao))
 


#título da Janela 
janela.title("Ferramenta de Cadastro de materiais")

label_descricao = tk.Label(text="Descrição do material ")
label_descricao.grid(column=0, row=1, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(column=0, row=2, padx=10, pady=10, sticky='nswe', columnspan=4 )

label_tipo_unidade = tk.Label(text="Tipo da unidade do material")
label_tipo_unidade.grid(column=0, row=3, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quantidade = tk.Label(text="Quantidade na unidade de material")
label_quantidade.grid(column=0, row=4, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(column=2, row=4, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text="Criar código", command=inserir_codigo)
botao_criar_codigo.grid(column=0, row=5, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()

print(listas_codigos)