my_list = [3, 5, 9]

def sum_list(alist):
    if len(alist) == 1:
        return alist[0]
    return alist[0] + sum_list(alist[1:])

sum = sum_list(my_list)
print(sum)
