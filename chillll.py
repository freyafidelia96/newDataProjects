def toBin(sum):
    x = ""
    while sum > 0:
        a = sum % 2
        x = x + str(a)
        sum = sum // 2
    return (x[::-1])


def toDec(binInt):
    binInt = binInt[::-1]
    decNum = 0
    for i in range(len(binInt)):
        decNum = decNum + (int(binInt[i]) * 2**i)
    return decNum


def main():
    binIntegerA = input("Enter a binary integer a of length n:")
    binIntegerB = input("Enter a binary integer b of length n:")
    
    listA = []
    listB = []
    listC = []

    for i, j in zip(binIntegerA, binIntegerB):
        listA.append(int(i))
        listB.append(int(j))

    print(f"List A = {listA}\nList B = {listB}")

    decSum = toDec(binIntegerA) + toDec(binIntegerB)
    binValue = toBin(decSum)
    for i in binValue:
        listC.append(int(i))

    print(f"The sum of the two binary integers give c:{binValue} and List C = {listC} ")

main()
