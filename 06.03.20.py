FiniteSet || Symbol
x=5 'x'
a=100 'a'
z=(x+y)**3-2xy
FiniteSet(1,2,3)
intersect
union
**
t=Finiteset(1,2,3)
t==s
t.union(s)
t.intersect(s)
t**2



def probability(space,event):
    return len(event)/len(space)  #Olay/Tüm Olaylar




def checkprime(number):
    if number!=1:
        for factor in range (2,number):
            if number%factor==0:
                return False
        else:
            return False
        return True





space=FiniteSet(*range(1,21))
primes=[]
for num in spaces:
    if checkprime(num): # asallık kontrol
        primes.append(num)
event=FiniteSet(*primes)
p=probability(space,event) # olasılık
print(p)



from sympy import FiniteSet
content=file1.readlines()
def probability(space,event):
    return len(event)/len(space)  #Olay/Tüm Olayların Uzayı




def checkprime(number):
    if number!=1:
        for factor in range (2,number):
            if number%factor==0:
                return False
        else:
            return False
        return True



space=FiniteSet(*range(1,21))# * operatörü kendinden sonra gelen 2 sayı arasındaki tüm sayıları gönderir
primes=[]
for num in space:
    if checkprime(num):
        primes.append(num)
event=FiniteSet(*primes)
p=probability(space,event) # olasılık
print(p)


file1 = open("mtf.txt","r")
content=file1.readLines()
print(content)
for line in content:
    for item in line:
        print(item)     #print(line)
