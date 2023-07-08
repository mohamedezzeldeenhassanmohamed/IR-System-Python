from Preprocessing import Preprocessing

term_doc_matrix = {}


class IncidenceIndexing:
    def __init__(self, checkbox):
        self.indexing(checkbox)

    def saveToFile(self, data={}):
        file = open("index\indexIncidence.txt", "w")
        for term in data:
            file.write(f'{term} {data[term]}\n')
        file.close()

    def indexInsedanceMatrixs(self, checkbox):
        file = open('dataset\CISI - Copy.ALL', "r")
        text = file.read()
        docnum = 0
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
            # Split the content into term_doc_matrix
            # 'Stemming', 'Lemmatization', 'Stop words'
            # print(tokens)
            if checkbox[3]:
                tokens = Preprocessing.Lemmatize(tokens)
            if checkbox[2]:
                tokens = Preprocessing.Stemming(tokens)
            if checkbox[4]:
                tokens = Preprocessing.StopWord(tokens)

            # Update the matrix for each term
            for token in tokens:
                if token not in term_doc_matrix:
                    term_doc_matrix[token] = [0] * len(docs)

                # term frequency
                # if docnum not in term_doc_matrix[token]:
                #     term_doc_matrix[token][docnum] = 0
                # term_doc_matrix[token][docnum] += 1

                term_doc_matrix[token][docnum] = 1
            docnum += 1

    def indexing(self, checkbox):
        self.indexInsedanceMatrixs(checkbox)
        data = {}
        for term in term_doc_matrix:
            posting = ""
            for post in term_doc_matrix[term]:
                posting += str(post)
            data[term] = posting
        self.saveToFile(data)
