# Libs
from tkinter import *
from tkinter import ttk

indexes = ['lucene', 'Term-document', 'Inverted Index', 'Positional Index', 'Bi-word Index']
checkboxs_names = ['Tokenization', 'Normalization', 'Stemming', 'Lemmatization', 'Stop words']
checkboxs = []


class Indexing:
    co = ""

    def __init__(self, tab1):
        # left
        tab1_frame1 = ttk.Frame(tab1)
        tab1_frame1.grid(row=0, column=0, padx=(75, 20), pady=(100, 0))
        Label(tab1_frame1, text="Choose Index").pack()
        index = ttk.Combobox(tab1_frame1, values=indexes, state='readonly')
        index.set(indexes[0])
        index.pack()
        self.co = index
        # right
        tab1_frame2 = ttk.Frame(tab1)
        tab1_frame2.grid(row=0, column=1, padx=(30, 0), pady=(100, 0))
        Label(tab1_frame2, text="Pre-processing").pack()
        i = 0
        for chk in checkboxs_names:
            checkboxs.append(IntVar())
            checkboxs[i] = ttk.Checkbutton(tab1_frame2, text=chk)
            checkboxs[i].configure(width=15, padding=[0, 12, 0, 0])
            if i == 0:
                checkboxs[i].state(["selected", "disabled"])
            checkboxs[i].pack()
            i += 1

    def checks(self):
        chks = []
        for ch in checkboxs:
            if len(ch.state()) > 0 and ch.state()[0] == 'selected':
                chks.append(True)
            else:
                chks.append(False)
        chks[0] = True
        return chks

    def combo_box(self):
        return self.co.get()
