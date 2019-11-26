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
    count = -1
    openBrCount = 0
    closedBrCount = 0
    for x in expressionList:
        count += 1
        if x == "(":
            openBrCount += 1
        elif x == ")":
            closedBrCount += 1
            if closedBrCount == openBrCount:
                break
    length = len(expressionList[firstIndex+1:count])+1
    return length

def lenInClBr(lastIndex, expressionList):
    count = -1
    openBrCount = 0
    closedBrCount = 0
    for x in expressionList:
        count += 1
        if x == ")":
            closedBrCount += 1
            if count == lastIndex:
                break
    count = -1
    for y in expressionList:
        count += 1
        if y == "(":
            openBrCount += 1
            if openBrCount == closedBrCount:
                break

    length = len(expressionList[count+1:lastIndex-1])+1
    return length

def lenInClBr(lastIndex, expressionList):
    done = False
    count = lastIndex
    while done == False:
        if expressionList[count-1] == "(":
            done = True
        count -= 1
    return length

def inClBr(lastIndex, expressionList):
    count = -1
    openBrCount = 0
    closedBrCount = 0
    for x in expressionList:
        count += 1
        if x == ")":
            closedBrCount += 1
            if count == lastIndex:
                break
    count = -1
    for y in expressionList:
        count += 1
        if y == "(":
            openBrCount += 1
            if openBrCount == closedBrCount:
                break

    newList = expressionList[count+1:lastIndex]
    return newList

def inBr(firstIndex, expressionList):
    count = -1
    openBrCount = 0
    closedBrCount = 0
    for x in expressionList:
        count += 1
        if x == "(":
            openBrCount += 1
        elif x == ")":
            closedBrCount += 1
            if closedBrCount == openBrCount:
                break
    newList = expressionList[firstIndex+1:count]
    return newList

def evaluate(expression):
    exprList = parseList(expression)
    count = -1
    while count < len(exprList)-2:
        count += 1
        if exprList[count] == "*":
            num1 = exprList[count-1]
            if  num1 == ")":
                length = lenInClBr(count-1, exprList)
                num1 = evaluate(inClBr(count-1, exprList))
                num1 = str(num2)
                num1 = list(num2)
                num1.remove("[")
                num1.remove("]")
                num1 = "".join(num1)
                exprList[count-1] = num1
                for x in range(length+1):
                    del(exprList[count-2])
                    count -= 1
            num2 = exprList[count+1]
            if num2 == "(":
                length = lenInBr(count+1, exprList)
                num2 = evaluate(inBr(count+1, exprList))
                num2 = str(num2)
                num2 = list(num2)
                num2.remove("[")
                num2.remove("]")
                num2 = "".join(num2)
                exprList[count+1] = num2
                for x in range(length):
                    del(exprList[count+2])
            exprList[count-1] = float(num1) * float(num2)
            del(exprList[count])
            del(exprList[count])
            count -= 1
        elif exprList[count] == "/":
            num1 = exprList[count-1]
            if  num1 == ")":
                length = lenInClBr(count-1, exprList)
                num1 = evaluate(inClBr(count-1, exprList))
                num1 = str(num1)
                num1 = list(num1)
                num1.remove("[")
                num1.remove("]")
                num1 = "".join(num1)
                exprList[count-1] = num1
                for x in range(length+1):
                    del(exprList[count-2])
                    count -= 1
            num2 = exprList[count+1]
            if num2 == "(":
                length = lenInBr(count+1, exprList)
                num2 = evaluate(inBr(count+1, exprList))
                num2 = str(num2)
                num2 = list(num2)
                num2.remove("[")
                num2.remove("]")
                num2 = "".join(num2)
                exprList[count+1] = num2
                for x in range(length):
                    del(exprList[count+2])
            exprList[count-1] = float(num1) / float(num2)
            del(exprList[count])
            del(exprList[count])
            count -= 1

    count = -1
    while count < len(exprList)-2:
        count += 1
        if exprList[count] == "+":
            num1 = exprList[count-1]
            if  num1 == ")":
                length = lenInClBr(count-1, exprList)
                num1 = evaluate(inClBr(count-1, exprList))
                num1 = str(num1)
                num1 = list(num1)
                num1.remove("[")
                num1.remove("]")
                num1 = "".join(num1)
                exprList[count-1] = num1
                for x in range(length+1):
                    del(exprList[count-2])
                    count -= 1
            num2 = exprList[count+1]
            if num2 == "(":
                length = lenInBr(count+1, exprList)
                num2 = evaluate(inBr(count+1, exprList))
                num2 = str(num2)
                num2 = list(num2)
                num2.remove("[")
                num2.remove("]")
                num2 = "".join(num2)
                exprList[count+1] = num2
                for x in range(length):
                    del(exprList[count+2])
            exprList[count-1] = float(num1) + float(num2)
            del(exprList[count])
            del(exprList[count])
            count -= 1
        elif exprList[count] == "-":
            num1 = exprList[count-1]
            if  num1 == ")":
                length = lenInClBr(count-1, exprList)
                num1 = evaluate(inClBr(count-1, exprList))
                num1 = str(num1)
                num1 = list(num1)
                num1.remove("[")
                num1.remove("]")
                num1 = "".join(num1)
                exprList[count-1] = num1
                for x in range(length+1):
                    del(exprList[count-2])
                    count -= 1
            num2 = exprList[count+1]
            if num2 == "(":
                length = lenInBr(count+1, exprList)
                num2 = evaluate(inBr(count+1, exprList))
                num2 = str(num2)
                num2 = list(num2)
                num2.remove("[")
                num2.remove("]")
                num2 = "".join(num2)
                exprList[count+1] = num2
                for x in range(length):
                    del(exprList[count+2])
            exprList[count-1] = float(num1) - float(num2)
            del(exprList[count])
            del(exprList[count])
            count -= 1

    return exprList


num = input("Enter an expressions (no errors please): ")

print(*evaluate(num))
