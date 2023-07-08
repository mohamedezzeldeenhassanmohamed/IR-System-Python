from Preprocessing import Preprocessing
dic = {}

class InvertedSearch:
    def __init__(self):
        InvertedSearch.getdata()

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
        # if there are many NOT operation in query delete them
        removelist1 = []
        for index in range(len(queryToken)):
            if queryToken[index] == "NOT":
                if index < len(queryToken) - 1 and queryToken[index + 1] == "NOT":
                    removelist1.append(index + 1)
        removelist1.reverse()
        for index in removelist1:
            queryToken.pop(index)
        try:
            if dic.get(queryToken[0]) != None:
                result = dic[queryToken[0]]
        except Exception as e:
            print(e)
        if len(queryToken) > 1:
            # finish NOT operation first
            removeList = []
            for index in range(len(queryToken)):
                if queryToken[index] == "NOT":
                    if index < len(queryToken) - 1:
                        if dic.get(queryToken[index + 1]) != None:
                            # print(index)
                            queryToken[index] = InvertedSearch.NotOp(dic[queryToken[index + 1]])
                            removeList.append(index + 1)
            # remove word after not from queryToken
            removeList.reverse()
            for index in removeList:
                queryToken.pop(index)
            # initiate the first value of the result
            try:
                if type(queryToken[0]) is list:
                    result = queryToken[0]
                else:
                    result = dic[(queryToken[0])]
            except:
                result = []
            # end
            # start loop for query
            for index in range(len(queryToken)):
                # print(index)
                if queryToken[index] == "AND":
                    if index > 0 and index < len(queryToken) - 1:
                        try:

                            if type(index + 1) is list:
                                result = InvertedSearch.AndOp(result, queryToken[index + 1])
                            elif dic.get(queryToken[index + 1]) is None:
                                result = []
                            else:
                                result = InvertedSearch.AndOp(result, dic[queryToken[index + 1]])
                        except:
                            continue
                elif queryToken[index] == "OR":
                    if index > 0 and index < len(queryToken) - 1:
                        # if dic.get(queryToken[index + 1]) != None:
                        try:
                            if type(queryToken[index + 1]) is list:
                                result = InvertedSearch.OrOp(result, queryToken[index + 1])
                            elif dic.get(queryToken[index + 1]) is None:
                                continue
                            else:
                                result = InvertedSearch.OrOp(result, dic[queryToken[index + 1]])
                        except:
                            continue
                elif queryToken[index] == "NOT":
                    if index < len(queryToken) - 1:
                        if dic.get(queryToken[index + 1]) != None:
                            # print(index)
                            result = InvertedSearch.NotOp(dic[queryToken[index + 1]])
        return result

    @staticmethod
    def getdata():
        file = open("index\invertedIndex.txt", "r")
        rows = file.read().split('\n')
        global docnum
        docnum = int(rows.pop(len(rows) - 1))
        for row in rows:
            term_post = row.split()
            dic[term_post[0]] = []
            for post in term_post[1].split(','):
                if len(post) > 0:
                    dic[term_post[0]].append(int(post))
        # dic[term_post[0]].pop(len(dic[term_post[0]]) - 1)
        return dic

    @staticmethod
    def AndOp(operand1, operand2):
        result = []
        i = 0
        j = 0
        while i < len(operand1) and j < len(operand2):
            if operand1[i] == operand2[j]:
                result.append(operand1[i])
                i += 1
                j += 1
            elif operand1[i] < operand2[j]:
                i += 1
            else:
                j += 1
        return result

    @staticmethod
    def OrOp(operand1=[], operand2=[]):
        # result = operand1 + operand2
        # result.sort()
        # return result
        result = []
        i = 0
        j = 0
        while i < len(operand1) and j < len(operand2):
            if int(operand1[i]) == int(operand2[j]):
                result.append(operand1[i])
                i += 1
                j += 1
            elif int(operand1[i]) < int(operand2[j]):
                result.append(operand1[i])
                i += 1
            else:
                result.append(operand2[j])
                j += 1
        while i < len(operand1):
            result.append(operand1[i])
            i += 1
        while j < len(operand2):
            result.append(operand2[j])
            j += 1
        return result

    @staticmethod
    def NotOp(operand):
        result = []
        i = 0
        for index in range(1, docnum + 1):
            if i >= len(operand) or index < operand[i]:
                result.append(index)
            else:
                i += 1
        return result

    @staticmethod
    def print(data):
        result = {}
        for index in range(len(data)):
            result[index + 1] = data[index]
        return result
