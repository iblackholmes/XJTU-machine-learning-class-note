# code source: 机器学习实战-Cha4-朴素贝叶斯
# author: iblackholmes
# date: 4/24/2019



# create deno data set
def loadDataSet():
    postingList = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ]

    # 1: 侮辱性文字
    # 0: 正常言论
    classVec = [0,1,0,1,0,1]

    return postingList, classVec


# create vocabulary form data set
def createVocabList(dataSet):
    # 创建一个空集
    vocabSet = set([])

    # 创建两个集合的并集
    for document in dataSet:
        vocabSet = vocabSet | set(document)

    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    # 创建一个其中所含元素都为0的向量
    returnVec = [0]*len(vocabList)
    
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList, index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec