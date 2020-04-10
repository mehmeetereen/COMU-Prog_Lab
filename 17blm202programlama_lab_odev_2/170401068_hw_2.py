import os
import sys
def hist(document):
    histogram = []
    data = []
    for i in document:
        check = False
        data.append(int(i.split(";")[3].split("-")[1]))
        for k in range(len(histogram)):
            if int(i.split(";")[3].split("-")[1]) == histogram[k][0]:
                histogram[k][1] += 1
                check = True
        if check == False:
            histogram.append([int(i.split(";")[3].split("-")[1]), 1])
    return histogram,data

with open(sys.argv[1]+"input_hw_2.csv") as document:
    histogram = hist(document)
    months = histogram[1]
    histogram = histogram[0]
    documentprt(sys.argv[2])
    print("Histogram : ",histogram)

def documentprt(adress):
    prt = open(adress+"170401068_hw_2_output.txt","w+",encoding="UTF-8")
    prt.write(f"Median : {median(months)}")
    prt.write(f"Average : {avg(months)}")
    prt.close()

def median(list):
    list=bubbleSort(list)
    if len(list)%2==1:
        mid = int(len(list)/2)+1
        return list[mid-1]
    else:
        mid1,mid2=list[int(len(list)/2)],list[int(len(list)/2)-1]
        return (mid1+mid2)/2

def avg(list):
    sum=0
    for i in list:
        sum+=i
    return sum/len(list)

def bubbleSort(list):
    for i in range(len(list)-1,-1,-1):
        for j in range(0,i):
            if not list[j]<list[j+1]:
                temp=list[j]
                list[j],list[j+1]=list[j+1],temp
    return list

def median(list):
    list=bubbleSort(list)
    if len(list)%2==1:
        mid = int(len(list)/2)+1
        return list[mid-1]
    else:
        mid1,mid2=list[int(len(list)/2)],list[int(len(list)/2)-1]
        return (mid1+mid2)/2

