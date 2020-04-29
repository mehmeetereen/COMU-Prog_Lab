#!/usr/bin/env python
# coding: utf-8

# In[3]:


def min_heapify(array,i):#Diziyi min heap dizilimine göre heapify eder.
    left = 2*i+1
    right = 2*i+2
    lenght=len(array)-1
    smallest = i
    if(left<= lenght and array[i] > array[left]):
        smallest=left
    if right<= lenght and array[i]>array[right]:
        smallest=right
    if smallest != i:
        array[i],array[smallest] =array[smallest], array[i]
        min_heapify(array,smallest)
        
def build_min_heap(array): #Dizideki tum elemanlar için çağırdık.Tersten başlayacak şekilde dizi oluşturur ve çağırır
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)
        
"""--------------------------------------------------------------------------------------------------------------------------"""
def insertItemToHeap(myheap_1,item):#Başta tek elemanlı ve heap,eklediğimiz eleman heapliği bozmadan eklenir.
    myheap_1.append(item)
    index = len(myheap_1)-1
    if index<=0:
        return    
    parent = (index-1)//2
    while parent>=0 and myheap_1[parent] > myheap_1[index]:
        myheap_1[parent],myheap_1[index] = myheap_1[index],myheap_1[parent]            
        index = parent
        parent = (index-1)//2
    
def removeItemFromHeap(myheap_1):#Heap yapısından sondaki elemanı siler.
    index = len(myheap_1)
    if index<=0:
        print("Heap'te eleman yok.")
        return
    myheap_1.pop()
"""--------------------------------------------------------------------------------------------------------------------------"""
def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array

my_array_1 = [8,5,11,4,13,15,1,2,16]
build_min_heap(my_array_1)
print(my_array_1 )
insertItemToHeap(my_array_1,9)
insertItemToHeap(my_array_1,1)
removeItemFromHeap(my_array_1)
print(my_array_1 )
print(sorted(my_array_1))


# In[ ]:




