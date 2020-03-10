# 1
def power(a, b):
	if b == 0:
		return 1
	elif b == 1:
		return a
	else:
		return a * power(a, b - 1)

# Üs hesap
def power2(a, b):
	if b == 0:
		return 1
	elif b == 1:
		return a
	else:
		if b % 2 == 0:
			return power(a * a, b // 2)
		else
		return (a * a, b // 2) * a

"""Recursive daha hızlı fonksiyon"""
liste_1 = [4, -3, 5, -2, 1, 2, 6, -2]
max = 0
for i in ranger(8):
	for j in range(i, 0)
		t = 0
		for k in range(i, j)
			t = t + liste_1[k]
		if max < t:
			max = t
			i_1, i_2 = i, j

print(max, i_1, i_2)

""" Listedeki maximum toplamlı diziyi ve boyutunuveren fonksiyon"""


def maxoftwo(a,b)
	if a>b:
		return a
	else:

		return b
def maxofthree(a,b,c)
return max of two(a,maxoftwo(b,c))


def mysubsumrec(list1=[4,-3,5,-2,-1,2,6,-2])
	if len(list1==1):
		reutrn list1[0]
	n=len(list1)
	lefti=0
	leftj=n//2
	righti=(n//2)+1
	rightj=n
	leftsum=mysubsumrec(list1[lefti,leftj])
	rightsum=mysubsumrec(list1[righti,rightj])
	t,templeftsum,temprightsum=0,0,0
	for i in range(leftj,lefti-1,-1)
		t=t+list1[i]
		if t>templeftsum:
			templeftsum = t
	for i in range(righti,rightj)
		t=t+list1[i]
		if t>temprigtsum:
			temprightsum = t
		centersum=templeftsum + temprightsum
		return maxofthree(leftsum,rightsum,centersum)

# BubbleSort
def mybubble(list1)
	for i in range(len(list1),0,-1):
		for j in range(i)
			if list1[j]>list1[j+1]:
				t=list1[j+1]
				list1[j+1] = list1[j]
				list1[j]= t
# Bubble sortta hiç dokunmayabilir , sıra düzgündür ya da maximum n*(n-1)/2 adet karşılaştırma yapar.