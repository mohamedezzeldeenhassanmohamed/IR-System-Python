# Libs
from tkinter import *
from tkinter import ttk, font, messagebox
from ttkthemes import ThemedTk

from BiwordSearch import BiwordSearch
from IncidenceIndexing import IncidenceIndexing
from IncidenceSearch import IncidenceSearch
from Indexing import Indexing
from InvertedIndexing import InvertedIndexing
from InvertedSearch import InvertedSearch
from Searching import Searching
from ShowWindow import ShowWindow
from luceneIndexing import luceneIndexing
from luceneSearch import luceneSearch
from PositionalIndex import PositionalIndex
from BiwordIndex import BiwordIndex
from PositionalSearch import PositionalSearch


# windows setting
root = ThemedTk()
root.title("IR")
root.resizable(False, False)
root.minsize(500, 500)
root.maxsize(500, 500)

# indexing
indexes = ['lucene', 'Term-document', 'Inverted Index', 'Positional Index', 'Bi-word Index']

# themes
themes = ['breeze', 'plastik', 'blue', 'alt', 'kroc', 'aquativo', 'scidblue', 'yaru', 'adapta', 'equilux', 'scidmint',
          'scidpink', 'classic', 'winnative', 'scidsand', 'arc', 'vista', 'elegance', 'scidgreen', 'xpnative',
          'radiance',
          'scidgrey', 'itft1', 'clearlooks', 'winxpblue', 'ubuntu', 'scidpurple', 'black', 'default', 'clam', 'smog',
          'keramik']

# fonts
fnt_header = font.Font(family="Helvetica", size=25, weight="bold")
fnt_wnd = font.Font(family="Arial", size=20, weight="bold")

# header windows
header = Label(root, text="IR Project 2023", font=fnt_header)
header.pack()

# tabs windows
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Indexing')
tabControl.add(tab2, text='Searching')
tabControl.pack(fill="both", expand=1)

# tab1 content Indexing
index = Indexing(tab1)
btn_index = ttk.Button(tab1, text="Indexing")
btn_index.grid(pady=(100, 0), columnspan=2)
# tab2 content Searching
search = Searching(tab2)
btn_search = ttk.Button(tab2, text="Searching")
btn_search.pack(pady=(100, 0))


# funcs
def indexing():
    try:
        if index.combo_box() == indexes[0]:
            luceneIndexing().indexing()

        elif index.combo_box() == indexes[1]:
            IncidenceIndexing(index.checks())

        elif index.combo_box() == indexes[2]:
            InvertedIndexing(index.checks())

        elif index.combo_box() == indexes[3]:
            PositionalIndex(index.checks())

        elif index.combo_box() == indexes[4]:
            BiwordIndex(index.checks())

        messagebox.showinfo(title="Info", message="Success")
    except EXCEPTION as e:
        print(e)
        messagebox.showinfo(title="Info", message="Failed")


def searching():
    title = ""
    try:
        if search.combo_box() == indexes[0]:
            sr = luceneSearch()
            re = sr.search(search.search_words())
            title = "Lucene"

        elif search.combo_box() == indexes[1]:
            sr = IncidenceSearch()
            re = sr.search(search.search_words(), search.checks())
            title = "Term Matrix"

        elif search.combo_box() == indexes[2]:
            sr = InvertedSearch()
            re = sr.search(search.search_words(), search.checks())
            title = "Inverted Search"

        elif search.combo_box() == indexes[3]:
            sr = PositionalSearch()
            re = sr.search(search.search_words(), search.checks())
            title = "Positional Search"

        elif search.combo_box() == indexes[4]:
            sr = BiwordSearch()
            re = sr.search(search.search_words(), search.checks())
            title = "Bi-word Search"

        s = ShowWindow(title, (500, 500))
        s.style("ubuntu")
        s.header(search.search_words())
        s.showdata(sr.print(re), "Num", "Docs")
        s.run()
    except EXCEPTION as e:
        print(e)
        messagebox.showinfo(title="Info", message="Failed")


# actions
btn_index.configure(command=indexing)
btn_search.configure(command=searching)

# style
ttk.Style(root).theme_use("ubuntu")

# run windows
root.mainloop()
