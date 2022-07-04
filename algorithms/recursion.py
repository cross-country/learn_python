my_list = [5, 6, 0, 3, 45]



#Summing all items in a list using recursion
def sum_func(lists):
    if len(lists) == 0:
        return 0
    return lists[0] + sum_func(lists[1:])
print(sum_func(my_list))


    #Summing all items in a list using recursion
def sum_func2(lists, x = 0):
    if x == len(lists):
        return 0
    return lists[x] + sum_func2(lists, x + 1)
print(sum_func2(my_list))


    #Counting all items in a list using recursion
def count_elements(lists, x = 0):
    if x == len(lists):
        return 0
    return 1 + count_elements(lists, x + 1)
print(count_elements(my_list))


    #Finding the biggest number using recursion
def biggest_num(lists, x = 0):
    if x == len(lists):
        return lists[len(lists) - 1]
    j = biggest_num(lists, x + 1)
    if j < lists[x]:
        j = lists[x]
    return j
print(biggest_num(my_list))


    #Binary search using recursion
new_list = []
for i in range(1, 91):
    new_list.append(i)
def binary_search(lists, item):
    low = 0
    high = len(lists) - 1
    if high < low:
        return 'No number'
    guess = int((high + low) / 2)
    if lists[guess] < item:
        low = guess + 1
    elif lists[guess] > item:
        high = guess - 1
    else:
        return lists[guess]
    return binary_search(lists[low: high + 1], item)
print(binary_search(new_list, 656))

    #Array quick sort using recursion
my_list = [4, 7, 9, 2, 5, 3]
def quick_sort(alist):
    low_list = []
    high_list = []
    if len(alist) < 2:
        return alist
    elif len(alist) == 2:
        if alist[0] > alist[1]:
            alist[0], alist[1] = alist[1], alist[0]
        return alist
    base_element = alist[len(alist) - 1]
    for i in alist[:-1]:
        if i < base_element:
            low_list.append(i)
        else:
            high_list.append(i)
    return quick_sort(low_list) + [base_element] + quick_sort(high_list)
print(quick_sort(my_list))