
'''
my_list = [5, 9, 7, 8, 9, 2, 4, 1]
for i in range(0, len(my_list) - 1):
    a = 0
    b = 1
    for j in range(0, len(my_list) - 1):
        if my_list[a] > my_list[b]:
            my_list[a], my_list[b] = my_list[b], my_list[a]
        a += 1
        b += 1
    print(my_list)
'''



'''
my_list = [5, 9, 7, 8, 9, 2, 4, 1]
for i in range(0, len(my_list) - 1):
    for j in range(i, len(my_list) - 1):
        if my_list[i] > my_list[j+1]:
            my_list[i], my_list[j+1] = my_list[j+1], my_list[i]
print(my_list)
'''


'''
my_list = [5, 9, 7, 8, 9, 2, 4, 1]
for i in range(0, len(my_list)):
    print(my_list)
    for j in range(0, i):
        if my_list[i] < my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)
'''

