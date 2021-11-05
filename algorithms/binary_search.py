my_list = []
for i in range(51):
    my_list.append(i)

def binary_search(list, item):
    item = item
    list = list
    low = 0
    high = len(list) - 1
    q = 0
    while low <= high:
        q += 1
        print(q)
        guess = int((low + high) / 2)
        if list[guess] < item:
            low = guess + 1
        elif list[guess] > item:
            high = guess - 1
        else:
            return list[guess]
    return None

print(binary_search(my_list, 75))
