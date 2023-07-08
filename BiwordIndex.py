from Preprocessing import Preprocessing

term_doc_matrix = {}

class BiwordIndex:

    def __init__(self, checkbox):
        self.indexing(checkbox)

    def biwordIndex_(self, checkbox):
        file = open('dataset\CISI - Copy.ALL', "r")
        text = file.read()
        global docnum
        docnum = 1
        # Split file into documents
        docs = text.split('.I ')
        docs.pop(0)
        for doc in docs:
            # get content only from document
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
            for index in range(1, len(tokens)):
                biword = tokens[index-1]+' '+tokens[index]
                if biword not in term_doc_matrix:
                    term_doc_matrix[biword] = []

                if not term_doc_matrix[biword].__contains__(docnum):
                    term_doc_matrix[biword].append(docnum)
            docnum += 1

    def saveToFile(self, data={}):
        file = open("index\BiwordIndex.txt", "w")
        for term in data:
            file.write(f'{term}:')
            for index in term_doc_matrix[term]:
                file.write(f"{index},")
            file.write("\n")
        file.write(f'{docnum - 1}')

        file.close()

    def indexing(self, checkbox):
        self.biwordIndex_(checkbox)
        self.saveToFile(term_doc_matrix)
