def myf1():
    n = len(list1)
    maxsum = 0
    for i in range(n):
        for j in range(i, n):

            for k in range(i.j):
                t = t + list1[k]
                if (t > maxsum):
                    maxsum = t
    print(maxsum)
    return maxsum


list1 = [4, -3, 5, -2, -1, 2, 6, -2]
x = myf1(list1)
print(x)


def myf2(list1=[4, -3, 5, -2, -1, 2, 6, -2]):
    n = len(list1)
    maxsum = 0
    for i in range(n):
        t = 0
        for j in range(i, n):
            t = t + list1[j]
            if (t > maxsum):
                maxsum = t
    return maxsum


list1 = [4, -3, 5, -2, -1, 2, 6, -2]
x = myf2(list1)
print(x)
#Supreme


def maxoftwo(a, b):
    if a > b:
        return a
    else:

        return b


def maxofthree(a, b, c):
    return maxoftwo(a, maxoftwo(b, c))


def myf3(list1=[4, -3, 5, -2, -1, 2, 6, -2]):
    n = len(list1)
    if (n == 1):
        return list1[0]
    lefti = 0
    leftj = n // 2
    righti = (n // 2) + 1
    rightj = n
    leftsum = myf3(list1[lefti:leftj])
    rightsum = myf3(list1[righti:rightj])  # diziden bir blok alırken iki nokta ( : )
    templeftsum = 0
    t = 0
    for i in range(leftj - 1, lefti - 1, -1):
        t = t + list1[i]
        if (t > templeftsum):
            templeftsum = t
    temprightsum = 0
    for i in range(righti, rightj):
        t = t + list1[i]
        if (t > temprightsum):
            temprightsum = t
    midsum = templeftsum + temprightsum
    return maxofthree(leftsum, rightsum, midsum)


list1 = [4, -3, 5, -2, -1, 2, 6, -2]
x = myf3(list1)
print(x)
