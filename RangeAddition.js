def getRange():
    xrange = int(input())
    return xrange


def sumCurrentPrev(xrange):
    prev = 0
    for i in range(xrange):
        sum = i + prev
        print(sum)
        prev = i

xrange = getRange()
sumCurrentPrev(xrange)
