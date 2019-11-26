def parseList(strExpression):
    exprList = list(strExpression)
    count = -1
    for index in exprList:
        count += 1
        if index != "+" and index != "-" and index != "*" and index != "/" and index != "(" and index != ")":
            while count < len(exprList)-1:
                while count < len(exprList)-1 and exprList[count+1] != "+" and exprList[count+1] != "-" \
                      and exprList[count+1] != "*" and exprList[count+1] != "/" and exprList[count+1] != "(" and exprList[count+1] !=")" \
                      and exprList[count] != "+" and exprList[count] != "-" \
                      and exprList[count] != "*" and exprList[count] != "/" and exprList[count] != "(" and exprList[count] !=")":
                    num = exprList[count]
                    num += exprList[count+1]
                    num = "".join(num)
                    exprList[count] = num
                    del exprList[count+1]
                if exprList[count] == "(" or exprList[count] == ")" or exprList[count] == "+" or exprList[count] == "-" \
                      or exprList[count] == "*" or exprList[count] == "/" or exprList[count] == "(" or exprList[count] ==")":
                   count += 1
                else:
                   count += 2

    return exprList

def lenInBr(firstIndex, expressionList):
    count = firstIndex
    openBrCount = 1
    while openBrCount != 0:
        if expressionList[count+1] == "(":
            openBrCount += 1
        if expressionList[count+1] == ")":
            openBrCount -= 1
        count += 1

    length = len(expressionList[firstIndex+1:count])+1
    return length

def lenInClBr(lastIndex, expressionList):
    count = lastIndex
    closedBrCount = 1
    while closedBrCount != 0:
        if expressionList[count-1] == ")":
            closedBrCount += 1
        if expressionList[count-1] == "(":
            closedBrCount -= 1
        count -= 1

    length = len(expressionList[count+1:lastIndex])
    return length

def inClBr(lastIndex, expressionList):
    count = lastIndex
    closedBrCount = 1
    while closedBrCount != 0:
        if expressionList[count-1] == ")":
            closedBrCount += 1
        if expressionList[count-1] == "(":
            closedBrCount -= 1
        count -= 1

    newList = expressionList[count+1:lastIndex]
    return newList

def inBr(firstIndex, expressionList):
    count = firstIndex
    openBrCount = 1
    while openBrCount != 0:
        if expressionList[count+1] == "(":
            openBrCount += 1
        if expressionList[count+1] == ")":
            openBrCount -= 1
        count += 1

    newList = expressionList[firstIndex+1:count]
    return newList

def getNum(expressionList, countLocal):
    num1 = expressionList[count-1]
    if  num1 == ")":
        length = lenInClBr(countLocal-1, expressionList)
        num1 = evaluate(inClBr(countLocal-1, expressionList))
        num1 = str(num1)
        num1 = list(num1)
        num1.remove("[")
        num1.remove("]")
        num1 = "".join(num1)
        expressionList[countLocal-1] = num1
        for x in range(length+1):
            del(expressionList[countLocal-2])
            countLocal -= 1
    num2 = expressionList[count+1]
    if num2 == "(":
        length = lenInBr(countLocal+1, expressionList)
        num2 = evaluate(inBr(countLocal+1, expressionList))
        num2 = str(num2)
        num2 = list(num2)
        num2.remove("[")
        num2.remove("]")
        num2 = "".join(num2)
        expressionList[countLocal+1] = num2
        for x in range(length):
            del(exprList[countLocal+2])
    
    return num1, num2, expressionList, countLocal

def evaluate(expression):
    exprList = parseList(expression)
    count = -1
    while count < len(exprList)-2:
        count += 1
        if exprList[count] == "*":
            num1, num2, exprList, count = getNum(exprList, count)
            exprList[count-1] = float(num1) * float(num2)
            del(exprList[count])
            del(exprList[count])
            count -= 1
        elif exprList[count] == "/":
            num1, num2, exprList, count = getNum(exprList, count)
            exprList[count-1] = float(num1) / float(num2)
            del(exprList[count])
            del(exprList[count])
            count -= 1

    count = -1
    while count < len(exprList)-2:
        count += 1
        if exprList[count] == "+":
            num1, num2, exprList, count = getNum(exprList, count)
            exprList[count-1] = float(num1) + float(num2)
            del(exprList[count])
            del(exprList[count])
            count -= 1
        elif exprList[count] == "-":
            num1, num2, exprList, count = getNum(exprList, count)
            exprList[count-1] = float(num1) - float(num2)
            del(exprList[count])
            del(exprList[count])
            count -= 1

    return exprList


#MAIN PROGRAM

num = input("Enter an expressions (no errors please): ")
print(*evaluate(num))