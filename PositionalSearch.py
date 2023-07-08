from Preprocessing import Preprocessing
dic = {}

class PositionalSearch:
    def __init__(self):
        PositionalSearch.getdata()


    def search(self, query, checkbox):
        if checkbox[1]:
            query = Preprocessing.normalization(query)

        queryToken = Preprocessing.tokenize(query)
        # print(queryToken)
        if checkbox[3]:
            queryToken = Preprocessing.Lemmatize(queryToken)

        if checkbox[2]:
            queryToken = Preprocessing.Stemming(queryToken)

        if checkbox[4]:
            queryToken = Preprocessing.StopWord(queryToken)

        result = []
        if dic.get(queryToken[0]):
            result = dic[queryToken[0]]
        if len(result) > 0:
            for index in range(1, len(queryToken)):
                if len(result) == 0 or dic.get(queryToken[index]) is None:
                    break
                result = self.CheckFound(result, dic[queryToken[index]])

        return result

    def CheckFound(self, operand1, operand2):
        result = {}
        i = 0
        j = 0
        key1 = list(operand1.keys())
        key2 = list(operand2.keys())
        while i < len(operand1) and j < len(operand2):
            if key1[i] < key2[j]:
                i += 1
            elif key1[i] > key2[j]:
                j += 1
            else:
                post1 = 0
                post2 = 0
                while post1 < len(operand1[key1[i]]) and post2 < len(operand2[key2[j]]):
                    if operand1[key1[i]][post1] == operand2[key2[j]][post2] -1:
                        if result.get(key2[j]) is None:
                            result[key2[j]] = []
                        result[key2[j]].append(operand2[key2[j]][post2])
                        post1 += 1
                        post2 += 1
                    elif operand1[key1[i]][post1] < operand2[key2[j]][post2]:
                        post1 += 1
                    else:
                        post2 += 1
                i += 1
                j += 1
        return result


    @staticmethod
    def getdata():
        file = open("index\positionalIndex.txt", "r")
        rows = file.read().split('\n')
        global docnum
        docnum = int(rows.pop(len(rows) - 1))
        for row in rows:
            term_post = row.split()
            dic[term_post[0]] = {}
            for post in term_post[1].split(';'):
                if len(post) == 0:
                    continue
                document = post.split(':')
                dic[term_post[0]][int(document[0])] = []
                for position in document[1].split(','):
                    if len(position) > 0:
                        dic[term_post[0]][int(document[0])].append(int(position))
        return dic

    @staticmethod
    def print(data={}):
        if len(data) > 0:
            data = list(data.keys())
        result = {}
        for index in range(len(data)):
            result[index + 1] = data[index]
        return result

