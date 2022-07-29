
my_str = ''
my_list = []
my_dict = {}
with open('scanned.txt', 'r') as file:
    my_str = file.read()
my_list = my_str.split('\n')
my_str = ''.join(my_list)
my_list = my_str.split(' ')

k = 0
while k < len(my_list):
    my_dict[my_list[k]] = '{} {} {}'.format(my_list[k+1], my_list[k+2], my_list[k+3])
    k += 4
    if k >= len(my_list) - 1:
        break

print(my_dict)