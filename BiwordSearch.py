from Preprocessing import Preprocessing
import fnmatch

dic = {}


class BiwordSearch:
    def __init__(self):
        BiwordSearch.getdata()

    def search(self, query, checkbox):
        index = query.index("*")
        # print(index)
        query2 = query.split("*")
        if checkbox[3]:
            query2 = Preprocessing.Lemmatize(query2)
            # print(f"lem {queryToken}")

        if checkbox[2]:
            query2 = Preprocessing.Stemming(query2)
        # print(query2)
        keys = list(dic.keys())
        resultkey = []
        if index == 0:
            for indx in range(len(keys)):
                if keys[indx].endswith(query2[1]):
                    resultkey.append(keys[indx])
        elif index == len(query) - 1:
            for indx in range(len(keys)):
                if keys[indx].startswith(query2[0]):
                    resultkey.append(keys[indx])
        else:
            for indx in range(len(keys)):
                if keys[indx].startswith(query2[0]) and keys[indx].endswith(query2[1]):
                    resultkey.append(keys[indx])
        print(resultkey)
        if len(resultkey) >0:
            result = dic[resultkey[0]]
        for indx in range(1, len(resultkey)):
            # print(dic[resultkey[indx]])
            result = BiwordSearch.OrOp(result, dic[resultkey[indx]])

        return result


    @staticmethod
    def getdata():
        file = open("index\BiwordIndex.txt", "r")
        rows = file.read().split('\n')
        global docnum
        docnum = int(rows.pop(len(rows) - 1))
        for row in rows:
            term_post = row.split(':')
            dic[term_post[0]] = []
            for post in term_post[1].split(','):
                if len(post) > 0:
                    dic[term_post[0]].append(int(post))
        # dic[term_post[0]].pop(len(dic[term_post[0]]) - 1)
        return dic

    @staticmethod
    def OrOp(operand1=[], operand2=[]):
        # result = operand1 + operand2
        # result.sort()
        # return result
        result = []
        i = 0
        j = 0
        while i < len(operand1) and j < len(operand2):
            if operand1[i] == operand2[j]:
                result.append(operand1[i])
                i += 1
                j += 1
            elif operand1[i] < operand2[j]:
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
    def print(data):
        result = {}
        for index in range(len(data)):
            result[index + 1] = data[index]
        return result

# obj = BiwordSearch()
# print(obj.search("present st*"))