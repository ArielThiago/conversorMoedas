#janela 500x500
#título
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com nomes das moedas

#importar a biblioteca
import customtkinter

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("400x600")
janela.title("Conversor de moedas")
janela.iconbitmap("icon.ico")

#criar botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=("",25))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de testino")

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD","BRL","ARS","SEK","RUB","EUR","JPY","GBP","AUD","CHF","CAD","CNY","TRY","BTC","DOGE","SHIB","ETH"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD","BRL","ARS","SEK","RUB","EUR","JPY","GBP","AUD","CHF","CAD","CNY","TRY","BTC","DOGE","SHIB","ETH"])

def converter_moeda():
    print("Converter moeda")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moeda1 = customtkinter.CTkLabel(lista_moedas, text="USD: Dólar americano")
moeda2 = customtkinter.CTkLabel(lista_moedas, text="BRL: Real brasileiro")
moeda3 = customtkinter.CTkLabel(lista_moedas, text="ARS: Peso argentino")
moeda4 = customtkinter.CTkLabel(lista_moedas, text="SEK: Coroa sueca")
moeda5 = customtkinter.CTkLabel(lista_moedas, text="RUB: Rublo russo")
moeda6 = customtkinter.CTkLabel(lista_moedas, text="EUR: Euro")
moeda7 = customtkinter.CTkLabel(lista_moedas, text="JPY: Iene japones")
moeda8 = customtkinter.CTkLabel(lista_moedas, text="GBP: Libra Esterlina")
moeda9 = customtkinter.CTkLabel(lista_moedas, text="AUD: Dólar australiano")
moeda10 = customtkinter.CTkLabel(lista_moedas, text="CHF: Franco suíço")
moeda11 = customtkinter.CTkLabel(lista_moedas, text="CAD: Dólar canadense")
moeda12 = customtkinter.CTkLabel(lista_moedas, text="CNY: Yuan chinês")
moeda13 = customtkinter.CTkLabel(lista_moedas, text="TRY: Lira turca")
moeda14 = customtkinter.CTkLabel(lista_moedas, text="BTC: Bitcoin")
moeda15 = customtkinter.CTkLabel(lista_moedas, text="DOGE: Dogecoin")
moeda16 = customtkinter.CTkLabel(lista_moedas, text="SHIB: Shiba Inu coin")
moeda17 = customtkinter.CTkLabel(lista_moedas, text="ETH: Ether")

moeda1.pack()
moeda2.pack()
moeda3.pack()
moeda4.pack()
moeda5.pack()
moeda6.pack()
moeda7.pack()
moeda8.pack()
moeda9.pack()
moeda10.pack()
moeda11.pack()
moeda12.pack()
moeda13.pack()
moeda14.pack()
moeda15.pack()
moeda16.pack()
moeda17.pack()

#colocar os elementos criados na tela
titulo.pack(padx=10, pady=20)
texto_moeda_origem.pack(padx=5, pady=5)
campo_moeda_origem.pack(padx=5, pady=5)
texto_moeda_destino.pack(padx=5, pady=5)
campo_moeda_destino.pack(padx=5, pady=5)
botao_converter.pack(padx=10, pady=40)
lista_moedas.pack(padx=5, pady=5)

#rodar a janela
janela.mainloop()