# Libs
from tkinter import *
from tkinter import ttk, font

indexes = ['lucene', 'Term-document', 'Inverted Index', 'Positional Index', 'Bi-word Index']
checkboxs_names = ['Tokenization', 'Normalization', 'Stemming', 'Lemmatization', 'Stop words']
checkboxs = []


class Searching:
    en = ""
    co = ""

    def __init__(self, tab2):
        # top
        tab1_frame1 = ttk.Frame(tab2)
        tab1_frame1.pack(pady=(12, 0))
        entry = Entry(tab1_frame1, width=35, font=font.Font(size=12), borderwidth=2)
        entry.grid(row=0, column=0, padx=(0, 12), ipady=10, rowspan=2)
        self.en = entry
        Label(tab1_frame1, text="Choose Index").grid(row=0, column=1)
        index = ttk.Combobox(tab1_frame1, values=indexes, state='readonly')
        index.set(indexes[0])
        index.grid(row=1, column=1)
        self.co = index
        # bottom
        tab1_frame2 = ttk.Frame(tab2)
        tab1_frame2.pack()
        Label(tab1_frame2, text="Pre-processing").grid(row=0, column=0)
        i = 0
        for chk in checkboxs_names:
            checkboxs.append(IntVar())
            checkboxs[i] = ttk.Checkbutton(tab1_frame2, text=chk)
            checkboxs[i].configure(width=15, padding=[0, 12, 0, 0])
            if i == 0:
                checkboxs[i].state(["selected", "disabled"])
            checkboxs[i].grid(row=i + 1, column=0)
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

    def search_words(self):
        return self.en.get()
