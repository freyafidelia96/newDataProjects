#INSERTION SORT ALGORITHM

'''a = [5, 2, 4, 6, 1, 3]
n = len(a)

for i in range(1, n):
    temp = a[i]
    j = i - 1
    while j >= 0 and a[j] > temp:
        a[j+1] = a[j]
        j = j - 1
    a[j+1] = temp
print(a)

for i in range(1, n):
    temp = a[i]
    j = i - 1
    while a[j] < temp and j >= 0:
        a[j + 1] = a[j]
        i = i - 1
        j = j - 1
    a[j+1] = temp
print(a)'''

"""x = eval(input("Enter a number: "))

for i in range(0, n):
    if a[i] == x:
        print("Number:", x, "is found at index", i)
        break
    elif a[i] != x and i == n - 1:
        print("Nil")"""

#Sum in binary

a = list(eval(input("Enter as many values as you can separated by commas:")))
print(a)
b = list(eval(input("Enter as many values as you can separated by commas:")))
print(b)
c = []


def toBin(sum):
    x = ""
    while sum > 0:
        a = sum % 2
        x = x + str(a)
        sum = sum // 2
    return int(x[::-1])


for i, j in zip(a, b):
    sum = i + j
    x = toBin(sum)
    c.append(x)
        
print(f"The list is added and converted to binary which gives us: {c}")

