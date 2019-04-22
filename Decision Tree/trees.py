# code source: 机器学习实战-Cha3-决策树
# author: iblackholmes
# date: 4/20/2019

from math import log
import operator


# create demo dataset
def createDataset():
    dataset = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ]
    labels = ['no surfacing', 'flippers']
    return dataset, labels

# calculate entropy
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    lableCounts = {}

    # dictionary for all classification
    for featVec in dataSet:
        currentLable = featVec[-1]
        if currentLable not in lableCounts.keys():
            lableCounts[currentLable] = 0
        lableCounts[currentLable] += 1

    # calculate log value with base 2
    shannonEnt = 0.0
    for key in lableCounts:
        prob = float(lableCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)

    return shannonEnt

# split data set
def splitDataSet(dataSet, axis, value):
    # new list storing split data set
    retDataSet = []

    # split out data
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)

    return retDataSet

# choose the best feature to spilt
def chooseBestFeatureToSplit(dataSet):
    numFeatures     = len(dataSet[0]) - 1               # ignore the column of label
    baseEntropy     = calcShannonEnt(dataSet)           # calculate the base Entropy of original data set
    bestInfoGain    = 0.0
    bestFeature     = -1

    # loop for comparing information gain of each split
    for i in range(numFeatures):
        # create unique feature list
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0

        # calculat Entropy of ecah split
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)

        # calculate the best information gain 
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    
    return bestFeature

# return the classcification which occurs in most times
def majorityCnt(classList):
    classCount = {}
    for key in classList:
        if key not in classCount.keys():
            classCount[key] = 0
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(i), reverse = True)
    return sortedClassCount[0][0]

# create a tree and return it in dictionary form
def createTree(dataSet, lables):
    classList = [example[-1] for example in dataSet]

    # stop spliting if classifications are same
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    # return the feature with most count when finish traversing
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    bestFeatIdx = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = lables[bestFeatIdx]
    
    # obtain all faatures
    tree = {bestFeatLabel:{}}
    del(lables[bestFeatIdx])
    featValues = [example[bestFeatIdx] for example in dataSet]
    uniqueVals = set(featValues)

    # generate tree
    for value in uniqueVals:
        subLabels = lables[:]
        tree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeatIdx, value), subLabels)

    return tree

# main method
if __name__ == "__main__":
    dataset, labels = createDataset()

    # without newe data following, the value of shannonEnt is 0.9709505944546686
    # while with new data, the value of shannonEnt raise at 1.3709505944546687
    # dataset[0][-1] = 'maybe'
    print(dataset)
    print(dataset[0])

    tree = createTree(dataset, labels)
    print(tree)