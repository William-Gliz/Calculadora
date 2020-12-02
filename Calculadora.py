from tkinter import *


# Criando a Aplicação
class Application(Frame):
    answer = '0'

    def __init__(self, master):
        super().__init__(master)
        # janela
        self.master = master
        self.master.title('Calculadora')
        self.master.geometry('300x200')
        self.option_add('*Font', 'calibri 12')
        self.pack(expand=YES, fill=BOTH)
        self.criar_interface()

    def criar_interface(self):

        # OBS: Para que os botões sejam ajustáveis ao tamanho da tela, é preciso definir:
        # configuração da linha e coluna com weight > 0
        # Os botões precisam ser definidos com sticky=N+S+W+E

        # 7 Colunas e 7 Linhas
        for x in range(5):
            self.columnconfigure(x, weight=1)
            self.rowconfigure(x, weight=1)

        # Display
        self.display = Entry(self, bd=5, bg='powder blue', relief=RIDGE)
        self.display.grid(row=0, columnspan=5, sticky=N+S+W+E)

        """ 5 colunas e 5 linhas
        [   Resultado   ]
        [7][8][9][DEL][C]
        [4][5][6][ X ][/]
        [1][2][3][ + ][-]
        [0][.][M][Ans][=]
        """

        # Números
        for i, c in enumerate(['789', '456', '123', '0.']):
            cont = 0
            for char in c:
                botao = Button(self, text=char, command=lambda s=self, y=char: s._append(y))
                botao.grid(row=(i + 1), column=cont, sticky=N+S+W+E, padx=2, pady=2)
                cont += 1

        # Operadores
        for i, c in enumerate(['*/', '+-']):
            cont = 0
            for char in c:
                botao = Button(self, text=char, command=lambda s=self, y=char: s._append(y))
                botao.grid(row=(i + 2), column=cont + 3, sticky=N+S+W+E, padx=2, pady=2)
                cont += 1

        # Comandos
        delete = Button(self, text='DEL', command=lambda s=self: s._del())
        delete.grid(row=1, column=3, sticky=N+S+W+E, padx=2, pady=2)

        clear = Button(self, text='C', command=lambda s=self: s._clear())
        clear.grid(row=1, column=4, sticky=N+S+W+E, padx=2, pady=2)

        ans = Button(self, text='Ans', command=lambda s=self: s._ans())
        ans.grid(row=4, column=2, sticky=N+S+W+E, padx=2, pady=2)

        res = Button(self, text='=', command=lambda s=self: s._eval())
        res.grid(row=4, column=3, columnspan=2, sticky=N+S+W+E, padx=2, pady=2)

    def _append(self, char):
        self.display.insert('end', char)

    def _del(self):
        tam = len(self.display.get())
        self.display.delete(tam - 1)  # Deleta o caracter peo seu index

    def _clear(self):
        self.display.delete('0', 'end')

    def _ans(self):
        self._append(self.answer)

    def _eval(self):
        valor = eval(self.display.get())
        self._clear()
        self._append(valor)
        self.answer = valor


root = Tk()
app = Application(master=root)
app.mainloop()

