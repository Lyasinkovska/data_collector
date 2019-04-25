'''def maxMultiple(divisor, bound):
    return bound//divisor*divisor

print(maxMultiple(3, 10))


def circle_of_numbers(n, firstNumber):
    if firstNumber < n/2:
        return (2*firstNumber+n)//2
    else:
        return (2*firstNumber - n)//2

print(circle_of_numbers(13, 2))

def lateRide(n):
    return n//60//10+n//60%10+n%60//10+n%60%10

print(lateRide(808))

def phoneCall(min1, min2_10, min11, s):
    if s - min1 <=0:
        return 1
    elif (s-min1)-min2_10*9<=0:
        print(1+(s-min1)//9)
    else:
        print(1+min2_10*9+(s-min1-min2_10*9)//min11)

print(phoneCall(2,2,1,24))

def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 > maxW and weight2 > maxW:
        return 0
    elif weight1+weight2 <= maxW:
        return value1+value2
    elif value1>value2:
        if weight1<maxW:
            return value1
        else:
            if weight2<maxW:
                return value2
            else:
                return 0
    else:
        if weight2<maxW:
            return value2
        elif weight1<maxW:
            return value1
        else:
            return 0


def isInfiniteProcess(a, b):
    if a>b:
        return True
    elif (b-a)%2==0:
        return False
    else:
        return True


import re

def timedReading(maxLength, text):

    count = 0
    x = re.findall("[a-zA-Z]+", text)
    for item in x:
        if len(item) <= maxLength:
            count += 1

    return count


print(timedReading(4, "The Fox asked the stork, 'How is the soup?'"))

def adjacentElementsProduct(inputArray):

    result = list()
    for n in range(len(inputArray)-1):
        i = inputArray[n]
        s = i * inputArray[n + 1]
        i = inputArray[n+1]
        result.append(s)

    return max(result)


print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))

print(adjacentElementsProduct([-23, 4, -3, 8, -12]))

def shapeArea(n):
    list_n = list()
    for i in range(n):
        result = i*4
        list_n.append(result)
    return(sum(list_n)+1)

print(shapeArea(3))
print(shapeArea(4))

def shapeArea(n):
    rerurn (for i in range(n)



def tennisSet(score1, score2):
    score = [score1, score2]
    return max(score) == 6 and min(score) < 5 or (max(score) == 7 and (4 < min(score) and min(score) < 7))
print(tennisSet(3,6))

#  return (max === 6 and min<5) or (max===7 and (4 < min and min < 7));

from datetime import datetime as dt

def metroCard(lastNumberOfDays):
    x = dt
    return x.month
[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(metroCard(30))


def killKthBit(n, k):
    if bin(n)[k+2] == 1:
        bin(n)[k + 2]=0
    return bin(n)[k+2]

print(killKthBit(37,3))

def matrixElementsSum(matrix):

    index= set()
    results = list()
    for elem in matrix:
        for i in range(len(elem)):
            if elem[i]==0:
                index.add(i)
            else:
                if i not in index:
                    results.append(elem[i])

    return sum(results)

print(matrixElementsSum([[1, 1, 1, 0],
                         [0, 5, 0, 1],
                         [2, 1, 3, 10]]))

def allLongestStrings(inputArray):
    result = list()
    for i in range(len(inputArray)):
        if len(inputArray[i])==len(sorted(inputArray, key=len)[-1]):
            result.append(inputArray[i])
    return result


print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))

def commonCharacterCount(s1, s2):
    result = dict()
    for letter in s1:
        for letter in s2:
            if letter in s1:
                if s1.count(letter)<s2.count(letter):
                    result.update({letter: s1.count(letter)})
                else:
                    result.update({letter: s2.count(letter)})
    return sum(result.values())

print(commonCharacterCount("aabcc", "adcaa"))
print(commonCharacterCount("zzzz", "zzzzzzz"))

def isLucky(n):
    n = str(n)
    numbers = list()
    for i in range(len(n)):
        numbers.append(int(n[i]))
    return sum(numbers[0:int(len(numbers) / 2)])==sum(numbers[int(len(numbers) / 2):])

print(isLucky("1239")

def sortByHeight(a):
    temp = list()
    newlist = list()
    for elem in a:
        if elem!=-1:
            temp.append(elem)
    t = sorted(temp)
    i=0
    for el in a:
        if el == -1:
            newlist.append(-1)
        else:
            newlist.append(t[i])
            i+=1

    return newlistzbazabazb


print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
'''
def reverseInParentheses(inputString):
    if "(" in inputString:
        parenthesis = [inputString.find('('), inputString.find(')')]
    else:
        parenthesis = []
    if parenthesis == []:
        inputString = ''.join(reversed(inputString))
    else:
        r = inputString[parenthesis[0]+1:parenthesis[1]]
        r2 = r[::-1]
        inputString.replace(r, r2)
    return parenthesis, inputString


print(reverseInParentheses('bar'))
print(reverseInParentheses('bar(baz)blim'))
#print(reverseInParentheses('foo(bar(baz))blim'))














