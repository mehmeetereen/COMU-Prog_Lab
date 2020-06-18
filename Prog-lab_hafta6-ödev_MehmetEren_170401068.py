#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Programlama Labaratuarı dersi hafta 6 ödev
Mehmet Eren
170401068
"""


# In[ ]:


"""Bu ödev tarafımca ders videoları ve değerli öğretmeniz Sayın İsmail Kahraman tarafından Tavsiye edilmiş
kaynak kullanılarak hazırlanmıştır.Büyük ihtimalle çalışmayan kısımları olacaktır lakin elimden verilen sürede gelen budur
ve Ödevi açıklamasında da belirteceğim nedenden dolayı çalışmayan kısımları bulunamamıştır çünkü elimde olmayan sebeplerden
dolayı bilgisayarım herhangi python idle çalıştığında donup reset atmaktadır ve bu kısa zamanda buna çözüm bulamadım."""


# In[2]:


import random


# In[ ]:


def mybubble(list1):
    for i in range(len(list1),0,-1):
        for j in range(i)
            if list1[j]>list1[j+1]:
                t=list1[j+1]
                list1[j+1] = list1[j]
                list1[j]= t
                
    return list1


# In[ ]:


def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 


# In[ ]:


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getfirst(self):
        return self.first
    def getlast(self):
        return self.last
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.first)        + ', ' + str(self.last) + '>'
        return result


# In[ ]:


def bigTest(numItems):
    items = buildManyItems(numItems, maxpage)
    val, taken = maxVal(items, 40)
    for item in taken:
        print(item)
        print('Total value of items taken =', val)


# In[4]:


def buildManyItems(numItems, maxpage):
    first = random.randit(1,maxpage)
    last = random.randit(1,maxpage)
    if(first>last):
        temp=last
        last=first
        first=temp
    items = []
    for i in range(numItems):
        items.append(Item(str(i),first,last))
    return items


# In[10]:


#Bilinen ilk ve son sayfaların dizide arasını doldurur 
def pages(items):
    list1=[]
    for i in range(getfirst(items(i)),getlast(items(i),1):
        list1.append(i)
    return list1


# In[ ]:


#en çok okunan sayfa
def mostread(list1):
    list = pages(items)
    mrepeat = most_frequent(list)
    return mrepeat


# In[ ]:


#okunan tüm sayfaları verir.
def unique(list1):
    ulist=list1
    ulist = list(set(ulist))

    return ulist


# In[ ]:


#brute force yanlış hatırlamıyorsam istediğimiz eleman sayısı na kadar sahip olduğu alt kumelerdir

