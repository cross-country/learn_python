import math
class Dictionary:
    """
    #strings of documentation
    """
    def __init__(self, adict):
        self.dict = adict

    def sort(self, reverse=False, sort='key'):
        """
        #dict_sort(reverse=False(True), sort='key(value)'
        #method sorts dictionary object by key or by value
        #method sorts only integers and strings
        """
        if sort == "value":
            item = 1
        elif sort == "key":
            item = 0
        my_dict = self.dict.copy()
        sorted_dict = {}
        while len(my_dict) > 0:
            key_delete = ""
            biggest = math.inf
            smallest = -math.inf
            biggest_letter = 'я'
            smallest_letter = 'A'
            reverse_str_var = False
            int_var = False
            for i in my_dict.items():
                if reverse is True:
                    if type(i[item]) is str:
                        reverse_str_var = True
                        if i[item] > smallest_letter:
                            smallest_letter = i[item]
                            key_delete = i[0]
                            temp_dictionary = {i[0]: i[1]}
                    elif type(i[item]) is int and not reverse_str_var:
                        if i[item] > smallest:
                            smallest = i[item]
                            key_delete = i[0]
                            temp_dictionary = {i[0]: i[1]}
                    else:
                        if type(i[item]) is not int and type(i[item]) is not str:
                            print('Only strings and integers can be sorted!!!')
                            return self.dict

                else:
                    if type(i[item]) is str and not int_var:
                        if i[item] < biggest_letter:
                            biggest_letter = i[item]
                            key_delete = i[0]
                            temp_dictionary = {i[0]: i[1]}
                    elif type(i[item]) is int:
                        int_var = True
                        if i[item] < biggest:
                            biggest = i[item]
                            key_delete = i[0]
                            temp_dictionary = {i[0]: i[1]}
                    else:
                        if type(i[item]) is not int and type(i[item]) is not str:
                            print('Only strings and integers can be sorted!!!')
                            return self.dict
            my_dict.pop(key_delete)
            sorted_dict.update(temp_dictionary)
            self.dict = sorted_dict
        return self.dict

    def tableview(self, numbered=True):
        number = 1
        table = ""
        for i in self.dict.items():
            if numbered:
                table += "{} - {} - {} \n".format(str(number), str(i[0]), str(i[1]))
            else:
                table += "{} - {} \n".format(str(i[0]), str(i[1]))
            number += 1
        return table
    def add_to_file(self, name='temporary'):
        f = open(name+'.txt', 'a')
        f.write(self.tableview())
        f.close()

asd = {'white': 300, 5: 30, 6: 'come', 'друг': 200, 'вокруг': 600, 2: 'begin'}
p = Dictionary(asd)
p.sort(sort="value", reverse=False)
print(p.tableview())