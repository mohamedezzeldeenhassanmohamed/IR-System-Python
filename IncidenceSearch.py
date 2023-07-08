from Preprocessing import Preprocessing

dic = {}


class IncidenceSearch:

    def __init__(self):
        IncidenceSearch.getdata()

    @staticmethod
    def is_binary(s):
        for c in s:
            if c not in ['0', '1']:
                return False
        return True

    def search(self, query, checkbox):
        # print(queryToken)
        if checkbox[1]:
            query = Preprocessing.normalization(query)

        queryToken = Preprocessing.tokenize(query)

        if checkbox[3]:
            queryToken = Preprocessing.Lemmatize(queryToken)
            # print(f"lem {queryToken}")

        if checkbox[2]:
            queryToken = Preprocessing.Stemming(queryToken)
            # print(f"stem {queryToken}")

        if checkbox[4]:
            queryToken = Preprocessing.StopWord(queryToken)
            # print(f"stop {queryToken}")

        # print(queryToken)
        result = ""
        # if there are many NOT operation in query delete them
        removelist1 = []
        for index in range(len(queryToken)):
            if queryToken[index] == "NOT":
                if index < len(queryToken) - 1 and queryToken[index + 1] == "NOT":
                    removelist1.append(index + 1)
        removelist1.reverse()
        for index in removelist1:
            queryToken.pop(index)

        # print(queryToken)
        try:
            if dic.get(queryToken[0]) != None:
                result = dic[queryToken[0]]
        except Exception as e:
            result = "0" * docnum
            print(e)
        if len(queryToken) > 1:
            # finish NOT operation first
            removeList = []
            for index in range(len(queryToken)):
                if queryToken[index] == "NOT":
                    if index < len(queryToken) - 1:
                        if dic.get(queryToken[index + 1]) != None:
                            # print(index)
                            queryToken[index] = IncidenceSearch.NotOp(dic[queryToken[index + 1]])
                            removeList.append(index + 1)
            # remove word after not from queryToken
            removeList.reverse()
            for index in removeList:
                queryToken.pop(index)
            # print(queryToken)
            # initiate the first value of the result
            if dic.get(queryToken[0]) != None:
                result = dic[queryToken[0]]
            elif IncidenceSearch.is_binary(queryToken[0]):
                result = queryToken[0]
            # end
            # start loop for query
            for index in range(len(queryToken)):
                # print(index)
                if queryToken[index] == "AND":
                    if index > 0 and index < len(queryToken) - 1:
                        if dic.get(queryToken[index + 1]) != None:
                            try:
                                if dic.get(queryToken[index + 1]) is None:
                                    result = IncidenceSearch.AndOp(result, queryToken[index + 1])
                                else:
                                    result = IncidenceSearch.AndOp(result, dic[queryToken[index + 1]])
                            except:
                                result = "0" * docnum
                elif queryToken[index] == "OR":
                    if index > 0 and index < len(queryToken) - 1:
                        if result == "":
                            result = "0" * docnum
                        try:
                            if dic.get(queryToken[index + 1]) is not None:
                                result = IncidenceSearch.OrOp(result, dic[queryToken[index + 1]])
                            else:
                                result = IncidenceSearch.OrOp(result, queryToken[index + 1])
                        except:
                            continue
                elif queryToken[index] == "NOT":
                    if index < len(queryToken) - 1:
                        if dic.get(queryToken[index + 1]) != None:
                            # print(index)
                            result = IncidenceSearch.NotOp(dic[queryToken[index + 1]])
        return result

    @staticmethod
    def getdata():
        file = open("index\indexIncidence.txt", "r")
        rows = file.read().split('\n')
        rows.pop(len(rows) - 1)
        global docnum
        docnum = len(rows[0].split()[1])
        for row in rows:
            term_post = row.split()
            dic[term_post[0]] = term_post[1]
        return dic

    @staticmethod
    def AndOp(operand1="", operand2=""):
        result = ""
        for i in range(len(operand1)):
            result += str(int(operand1[i]) & int(operand2[i]))
        return result

    @staticmethod
    def OrOp(operand1="", operand2=""):
        result = ""
        for i in range(len(operand1)):
            result += str(int(operand1[i]) | int(operand2[i]))
        return result

    @staticmethod
    def NotOp(operand=""):
        result = ""
        for op in operand:
            if op == "0":
                result += "1"
            else:
                result += "0"
        return result

    @staticmethod
    def print(data):
        result = {}
        for index in range(len(data)):
            result[index + 1] = data[index]
        return result
