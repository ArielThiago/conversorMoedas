#janela 500x500
#título
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com nomes das moedas

#importar a biblioteca
import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("400x600")
janela.title("Conversor de moedas")
janela.iconbitmap("icon.ico")

dic_conversoes_disponiveis = conversoes_disponiveis()

#criar botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=("",25))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de testino")

def carregar_moedas_destino(moeda_selecionada):
    lista_moeda_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values = lista_moeda_destino)
    campo_moeda_destino.set(lista_moeda_destino[0])


campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
   nome_moeda =  moedas_disponiveis[codigo_moeda]
   texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
   texto_moeda.pack()   

#colocar os elementos criados na tela
titulo.pack(padx=10, pady=20)
texto_moeda_origem.pack(padx=5, pady=5)
campo_moeda_origem.pack(padx=5, pady=5)
texto_moeda_destino.pack(padx=5, pady=5)
campo_moeda_destino.pack(padx=5, pady=5)
botao_converter.pack(padx=10, pady=40)
texto_cotacao_moeda.pack(padx=5, pady=5)
lista_moedas.pack(padx=5, pady=5)


#rodar a janela
janela.mainloop()