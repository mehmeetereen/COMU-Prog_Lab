# Rastgele sayi olusturma.
import random

random.random()
s = random.randint(1, 100)
print(s)

# İstenildiği kadar istenilen aralıkta dizi üreten fonk.
def get_n_random_numbers(n=10, min_=-5, max_=5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_, max_))
    return numbers

print(get_n_random_numbers())

my_list = get_n_random_numbers(15, -4, 4)
sorted(my_list)  # daha rahat görülmesi açısından sıralama


# iki farklı fonk. ile histogram

def my_frequency_with_dict(list):
    frequency_dict = {}  # dict()={}
    for item in list:
        if (item in frequency_dict):
            frequency_dict[item] = frequency_dict[item] + 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

print(my_frequency_with_dict(my_list))


def my_frequency_with_list_of_tuples(list_1):
    frequency_list = []
    for i in range(len(list_1)):
        s = False
        for j in range(len(frequency_list)):
            if (list_1[i] == frequency_list[j][0]):
                frequency_list[j][1] = frequency_list[j[1] + 1
                s = True
                if (s == False):
                    frequency_list.append([list_1[i], 1])
    return frequency_list


my_list = [2, 3, 2, 5, 8, 2, 4, 3, 3, 2, 8, 5, 2, 4, 4, 4, 4, 4]
result_1 = my_frequency_with_dict(my_list)
result_2 = my_frequency_with_list_of_tuples(my_list)
print(result_1, result_2)

# Histogram ile beraber bir listenin modu
my_list_1 = get_n_random_numbers(10)
my_hist_d = my_frequency_with_dict(my_list_1)
print(my_hist_d)
my_hist_1 = my_frequency_with_list_of_tuples(my_list_1)
print(my_hist_1)

frequency_max = -1
mode = -1
for key in my_hist_d.keys():
    print(key, my_hist_d[key])
    if my_hist_d[key] > frequency_max:
        frequency_max = my_hist_d[key]
        mode = key

print(frequency_max, mode)


def my_mode_with_dict(my_hist_d):
    frequency_max = -1
    mode = -1
    for key in my_hist_d.keys():
        # print(key,my_hist_d[key])
        if my_hist_d[key] > frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return mode, frequency_max

print(my_mode_with_dict(my_hist_d))



my_list_100 = get_n_random_numbers(10, -4, 4)
my_hist_1 = my_frequency_dict(my_list_100)
print(my_mode_with_dict(my_hist_1))
print(my_list_100)

my_list_1 = get_n_random_numbers(10)
my_hist_list = my_frequency_with_list_of_tuples(my_list_1)
print(my_hist_list)

frequency_max = -1
mode = -1
for item, frequency in my_hist_list:
    print(item, frequency)
    if frequency > frequency_max:
        frequency_max = frequency
        mode = item

print(mode, frequency_max)


def my_mode_with_list(my_hist_list):
    frequency_max = -1
    mode = -1
    for item, frequency in my_hist_list:
        print(item, frequency)
        if frequency_max=frequency
        mode = item
    return mode, frequency_max


my_list_100 = get_n_random_numbers(20, -4, 4)
my_hist_1 = my_frequency_with_list_of_tuples(my_list_100)
print(my_mode_with_list(my_hist_1))
print(my_list_100)


# bir listede linear arama
def my_search(my_list, item_search):
    found = (-1, -1)
    for indis in my_list:
        if my_list[indis] == item_search:
            found = (my_list[indis], indis)
    return found

my_list=get_n_random_numbers(10,-5,5)
print(my_list)

print(my_search(my_list, 3))


# listenin ortalaması
my_list=get_n_random_numbers(10,-50,50)
print(my_list)
s, t = 0, 0
for item in my_list:
    s = s + 1
    t = t + item
mean_ = t / s
print(mean_)

def my_mean(my_list):
    s, t = 0, 0
    for item in my_list:
        s = s + 1
        t = t + item
    mean_= t / s
    return mean_

my_list=get_n_random_numbers(10,-50,50)
print(my_list)
print(my_mean(my_list))


# Listenin sıralanması
print(my_list)
n=len(my_list)
print(my_list)
for i in range(n - 1, -1, -1):
    for j in range(0, i):
        if not (my_list[j] < my_list[j + 1]):
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp
print(my_list)



def my_bubble_sort(my_list):
    n = len(my_list)
    print(my_list)
    for i in range(n - 1, -1, -1):
        for j in range(0, i):
            if not (my_list[j] < my_list[j + 1]):
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

my_list = get_n_random_numbers(4,-5,5)
print(my_list)
print(my_bubble_sort(my_list))


# ikili arama
def my_binary_search(my_list, item_search):
    found = (-1, -1)
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if my_list[mid] == item_search:
            return my_list[mid], mid
        elif my_list[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1
    return found        #None

my_list_1 = get_n_random_numbers(10)
print("liste",my_list)
my_list_2 = my_bubble_sort(my_list_1)
print("sirali liste",my_list_2)
my my_binary_search(my_list_2,3)


# median bulma
size = input("dizinin boyutunu giriniz")
size = int(size)
my_list_1 = get_n_random_numbers(size)

print("liste", my_list_1)


def my_median(my_list):
    my_list_2 = bubble_sort(my_list)
    #print(my_list_2)
    n = len(my_list_2)
    if n % 2 == 1:
        middle = int(n / 2) + 1
        median = my_list_2[middle-1]
        #print(median)
    else:
        middle_1 = int(n / 2)-1
        middle_2 = middle_1 + 1
        median = (my_list_2[middle_1]+my_list_2[middle_2])/2
        #print(median)
    return median

my_list_2=get_n_random_numbers(4,-100,100)
print(my_median(my_list_2),my_list_2)
print(my_list_2)

