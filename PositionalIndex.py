from Preprocessing import Preprocessing

term_doc_matrix = {}

class PositionalIndex:

    def __init__(self, checkbox):
        self.indexing(checkbox)

    def positionalIndex_(self, checkbox):
        file = open('dataset\CISI - Copy.ALL', "r")
        text = file.read()
        global docnum
        docnum = 1
        docs = text.split('.I ')
        docs.pop(0)
        for doc in docs:
            indxStart = doc.index(".W")
            indxEnd = doc.index(".X")
            content = doc[indxStart + 3:indxEnd]
            if checkbox[1]:
                content = Preprocessing.normalization(content)

            # Split the content into term_doc_matrix
            tokens = Preprocessing.tokenize(content)
            if checkbox[3]:
                tokens = Preprocessing.Lemmatize(tokens)
            if checkbox[2]:
                tokens = Preprocessing.Stemming(tokens)
            if checkbox[4]:
                tokens = Preprocessing.StopWord(tokens)

            # Update the matrix for each term
            index = 0
            for token in tokens:
                index += 1
                if token not in term_doc_matrix:
                    term_doc_matrix[token] = {}
                if not term_doc_matrix[token].get(docnum):
                    term_doc_matrix[token][docnum] = []
                term_doc_matrix[token][docnum].append(index)

            docnum += 1

    def saveToFile(self, data={}):
        file = open("index\positionalIndex.txt", "w")
        for term in data:
            file.write(f'{term} ')
            for docnum in term_doc_matrix[term]:
                file.write(f"{docnum}:")
                for index in term_doc_matrix[term][docnum]:
                    file.write(f'{index},')
                file.write(';')
            file.write("\n")
        file.write(f'{docnum - 1}')
        file.close()
        term_doc_matrix.clear()

    def indexing(self, checkbox):
        self.positionalIndex_(checkbox)
        self.saveToFile(term_doc_matrix)
