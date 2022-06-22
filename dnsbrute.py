import dns.resolver
from tkinter import *

def buscaDominio(dominio):

    resolver = dns.resolver.Resolver()
    wordlist = ["advanced", "shop", "dvwa", "mailz"]

    for subdominio in wordlist:
        try:
            subdominios = []
            sub_alvo = "{}.{}".format(subdominio, dominio)
            resultados = resolver.resolve(sub_alvo, "A")
            for resultado in resultados:
                    subdominios.append("{} -> {}".format(sub_alvo, resultado))

            encontrados = Label(janela, text= subdominios[0])
            encontrados.grid(column=1, padx=10, pady= 10)

        except Exception as error:
             pass


janela = Tk()
janela.title("DNS-BRUTE")
Texto = Label(janela, text="          DIGITE O DOMINIO PARA PROCURAR OS SUBDOMINIOS          ")
Texto.grid(column=1, row=0, padx=10, pady=10)
inputCaixa = Entry(janela)
inputCaixa.grid(column=1, row=1, padx=10, pady=10)
botao1 = Button(janela, text="Buscar", command=lambda: buscaDominio(inputCaixa.get()))
botao1.grid(column=1, row=2, padx=10, pady=10)

janela.mainloop()
