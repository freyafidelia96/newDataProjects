try:
    a = list(eval(input("Enter as many values as you can separated by commas:")))
    print(f"List A = {a}")
    b = list(eval(input("Enter as many values as you can separated by commas:")))        
    print(f"List B = {b}")
    c = []

    def toBin(sum):
        x = ""
        while sum > 0:
            a = sum % 2
            x = x + str(a)
            sum = sum // 2
        return int(x[::-1])


    def toDec(x):
        x = str(x)
        x = x[::-1]
        decNum = 0
        for i in range(len(x)):
            decNum = decNum + (int(x[i]) * 2**i)
        return decNum


    def addBin(i, j):
        sum = i + j
        if i + j == 2:
            sum = 10
        elif i + j > 2:
            #Converts both i and j to decimal
            x = toDec(i) + toDec(j)
            sum = toBin(x)
        return sum

    for i, j in zip(a, b):
        c.append(addBin(i, j))

    print(f"Addition of A and B, List C = {c}")

except TypeError:
    print(f"Length of each list should be the same and greater than one")

    



