"""List & Hash - -------------------------------
| _ > insert |->insert
| _ > search - ----------------------- |->update / delete
| _ > update / delete |->  search
"""
"""stack
l
______ ^
| ______ |
"""
List1.append(100)  # hash yapısı olsa idi hash[key]=100
list1 = [0, 5, 25, 100, 5, 5, 0, 100]
0: 1, 4: 3
25: 1
100: 2


def myh(list1)
    # a=10-------------------|
    mydictionary = dict()  # {}	#			 |----> hata verir
    for i in list1  # for i in a-------------|
        if i in mydictionary:
            mydictionary[i] = mydictionary[i] + 1
        else:
            mydictionary[i] = 1

    return mydictionary


print(myh(List1))

"""KODUN
ÇALIŞMASI

myd -->{}
i = a[0:1]
i = 5
s: 1 /\2 /\3
25: 1
100: 1 /\2
"""

def lookup(d, v):
    for k in d:
        if d[k] == v:
            return k


known = {0: 0, 1: 1}


def fibonaccirec(n):
    if n < 2:
        return n
    else:
        return fibonaccirec(n - 1) + fibonaccirec(n - 2)
"""""  if n in known:
            return know[n]
        else:
    	    result=fibonaccirec(n-1)+fibonaccirec(n-2)
            known[n]=result
     	    return result
""""

from sympy import FiniteSet

s = FiniteSet(1, 15
iFraction(1, 5)
for member in s:
    print(member)
t = FiniteSet(Fraction(1, 5), 1.5, 1, 1)
if s == t:
    print("True")
s.intersect(t)
s.unson(t)
p = s ** 2
p1 = s ** 3
A = FiniteSet(1, 10, 20)
B = FiniteSet(5, 8)
if A == B:
    var = A.intersect(B).union
A ** 2,


list1 = [1, 4, 7, 84, 3, 62, 23]
myd = dict()
# myd1={}
myd = {1: 'bir', 2: 2, '3': 'three'}
print(myd)
for key in myd.keys():
    print(key, myd[key])
var = 1 in myd
if -41 not in myd:
    myd[-40] = 50
print(myd)


def myh(list1):
    myd = {}
    for item in list1:
        if item not in myd:
            myd[item] = 1
        else:
            myd[item] = item + 1
    return myd


print(myh([2, 3, 4, 6, 2, 5, 6, 6, 6, 6, 6, 6, 6, 2]))



def lookup(d, v):
    for key in d:
        if [key] == v:
            return key
        else:
            return -1



def myh(list1):
    myd = {}
    for item in list1:
        if item not in myd:
            myd[item] = 1
        else:
            myd[item] = item + 1
    return myd


def lookup(d, v):
    for key in d:
        if [key] == v:
            return key
        else:
            return -1


list1 = {2, 4, 6, 2, 1, 1, 4, 5, 78, 87, 8, 6, 2, 3}
print(lookup(myh(list1), 4))