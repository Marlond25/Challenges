def ScaleBalancing(strArr):
    balance = strArr[0][0] - strArr[0][1]
    a = strArr[1]
    c = []

    if balance == 0:
        return "The scale is balanced"

    elif balance != 0:

        # pick sides
        if balance < 0:
            side = "left"
        else:
            side = "right"

        # does a single item balance the scale?
        for i in range(len(strArr[1])):
            if abs(balance) - abs(strArr[1][i]) == 0:
                return "Add " + str(strArr[1][i]) + " to the " + side

        # find all permutations
        for i in a:
            z = 0
            for j in a:
                c.append([i, a[z]])
                z += 1

        # does the sum of any items balance the scale?
        for i in range(len(c)-1):
            if abs(balance) - abs(c[i][0] + c[i+1][1]) == 0:
                return "Add (" + str(abs(c[i][0])) + " + " + str(abs(c[i+1][1])) + ") to the " + side

        # does a permutation balance the scale?
        for i in range(len(c)-1):
            if abs(c[i][0] - c[i+1][1]) == abs(balance):
                if (c[i][0] > c[i+1][1]) and (strArr[0][0] > strArr[0][1]):
                    return "Add " + str(c[i+1][1]) + " to the left, " + str(c[i][0]) +" to the right"
                else:
                    return "Add " + str(c[i][0]) + " to the left, " + str(c[i+1][1]) +" to the right"

    return "not possible"

left = 152222
right = 15
scale = [left, right]
weights = [12, 2, 6, 7, 10, 152206, 3, 1] # len(weights) > 0
print(ScaleBalancing([scale, weights]))
