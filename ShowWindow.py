from tkinter import *
from tkinter import ttk, font, messagebox
from ttkthemes import ThemedTk


class ShowWindow:
    def __init__(self, title, size):
        self.game_scroll = None
        self.root = ThemedTk()
        self.root.title(title)
        self.root.resizable(False, False)
        self.root.minsize(size[0], size[1])
        self.root.maxsize(size[0], size[1])

    def showdata(self, data, col1, col2):
        self.game_scroll = Scrollbar(self.root, orient='vertical')
        self.game_scroll.pack(side=RIGHT, fill=Y)
        my_game = ttk.Treeview(self.root, yscrollcommand=self.game_scroll.set, height=500)
        my_game['columns'] = ('doc_id', 'Found')
        my_game.column("#0", width=0, stretch=NO)
        my_game.column("doc_id", anchor=CENTER, stretch=YES, width=280)
        my_game.column("Found", anchor=CENTER, stretch=YES)
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("doc_id", text=col1, anchor=CENTER)
        my_game.heading("Found", text=col2, anchor=CENTER)
        for keys, values in data.items():
            my_game.insert(parent='', index='end', iid=keys, text='', values=(keys, values))
        my_game.pack()

    def style(self, style):
        ttk.Style(self.root).theme_use(style)
        ttk.Style(self.game_scroll).theme_use(style)

    def header(self, title):
        header = Label(self.root, text=title)
        header.pack()

    def run(self):
        self.root.mainloop()
