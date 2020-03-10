"""Bubble
Sort
List1 = {.....
    c-> swap
ıof
comparison = n2 - n / 2
of
swap - -->?
"""

"""SELECTİON
SORT

2
ye
ayrılır
1 - Sıralanmış
2 - Sıralanmamış
______""""
"""swap
I
sorted
I
ı
ı
I
selection(indis)
_I
(max)

3, 10, 2, 6, 5, 9
- --
sorted
- --
unsorted
10, 6
- -----
unsorted
6, 10...

- ---Maxindis(1)
10 - ------------>9

3, 10, 2, 6, 5, 9
3, 10, 2, 6, 5, 9
3, 2, 10, 6, 5, 9
2, 3, 10, 6, 5, 9
2, 3, 6, 10, 5, 9
2, 3, 6, 5, 10, 9
2, 3, 5, 6, 10, 9
2, 3, 5, 6, 9, 10
"""
"""Slection
sortta
sıralama
yaparken
swap
1
olduğunda
başa
döner
ve
tekrar
kontrol
eder

23, 10, 12, 36, 51, 98
10, 23, 12, 36, 51, 98
- --> swap
1
başa
dön
10, 12, 23, 36, 51, 98
- ---> swap
1
10, 12, 23, 36, 51, 98
swap
0
çık

23, 10, 11, 6, 5, 18, 1
10, 23, 11, 6, 5, 18, 1
10, 11, 12, 6, 5, 18, 1
    .....
    Selection
sort
burada
gereksiz
yere
çok
karşılaştırma
yapar
"""

"""SHELLSORT

2, 3, 5, 6, 9, 10
'u tersten yazmak için
10
'u başa almak için n
9
u
sonraya
atmaya
n - 1
    .
    .
    .
    swap
gerekliyken
shell
algoritmasıyla
daha
aza
indirilir
How:
Diziyi
ikiye
bölüyor
2, 3, 5, 6
9, 10, 15, 20
9 -->2
3 -->10
5 -->15
6 - -->20
gap
aralığı
sayılar
kendi
arasında
sıralıdır
diye
düşünülür
9, 10, 15, 20, 2, 3, 5, 6
ya
dönüştü
15, 20, 9, 10, 5, 6, 2, 3
20, 15, 10, 9, 6, 5, 3, 2
n = 1
#'e düşene kadar devam et
"""
#İnsertion Sort Code
def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[i + 1] = arr[j]
            j = j - 1
            #  .......,61,.........,130,60-----> 60 61 yerine gider ve diğer sayılar sağa doğru kayar.


#Shell Sort Code
def shellsort(arr):
    n = len(arr)
    gap = n / 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap > temp]:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap //= 2