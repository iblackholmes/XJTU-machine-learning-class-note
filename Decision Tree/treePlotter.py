# code source: 机器学习实战-Cha3-决策树
# author: iblackholmes
# date: 4/20/2019

import matplotlib.pyplot as plt

# customize textbox and arrow format
decisionNode    = dict(boxstyle = "sawtooth", fc="0.8")
leafNode        = dict(boxstyle="round4", fc="0.8")
arrow_args      = dict(arrowstyle="<-")


# generae a tree for test
def genTree(i):
    listOfTrees =  [
        {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
        {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
    ]
    return listOfTrees[i]

# draw notes with arrow
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(
        nodeTxt, 
        xy          = parentPt, 
        xycoords    = 'axes fraction',
        xytext      = centerPt,
        textcoords  = 'axes fraction',
        va          = 'center',
        ha          = 'center',
        bbox        = nodeType,
        arrowprops  = arrow_args)

# draw information between parent node and child node
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)

def plotTree(tree, parentPt, nodeTxt):
    # calculate depth and length of figure
    numLeafs = getNumLeafs(tree)
    depth = getTreeDepth(tree)
    firstStr = list(tree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)

    # sign attribution value of child node
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)

    # reduce y offset
    secondDict = tree[firstStr]
    plotNode.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

# get the number of leafs of a tree
def getNumLeafs(tree):
    numLeafs = 0
    firstStr = list(tree.keys())[0]
    secondDict = tree[firstStr]

    for key in secondDict.keys():
        # test whether the type of this data is a dictionary
        if type(secondDict[key]).__name__=='dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1

    return numLeafs

# get the depth of a tree
def getTreeDepth(tree):
    maxDepth = 0
    firstStr = list(tree.keys())[0]
    secondDict = tree[firstStr]

    for key in secondDict.keys():
        # test whether the type of this data is a dictionary
        if type(secondDict[key]).__name__=='dict':
            tmpDepth = 1 + getTreeDepth(secondDict[key])
        else:
            tmpDepth = 1
        if tmpDepth>maxDepth:
            maxDepth = tmpDepth

    return maxDepth

# generate figure
def createPlot(tree):
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon = False, **axprops)
    
    plotTree.totalW = float(getNumLeafs(tree))
    plotTree.totalD = float(getTreeDepth(tree))
    plotTree.xOff = -0.5/plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(tree, (0.5,1.0), '')

    plt.show()

# main method
if __name__ == "__main__":
    tree = genTree(1)
    # tree['no surfacing'][3]='maybe'
    createPlot(tree)