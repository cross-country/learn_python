import openpyxl

def create_list(file_txt):
    file = file_txt
    with open(file, 'r') as text:
        my_str = text.read()
    my_str = my_str.lower()
    my_str = my_str.title()
    my_list = my_str.split('\n')
    return my_list
def create_excel(txt_file, excel_file):
    my_list = create_list(txt_file)
    book = openpyxl.Workbook()
    sheet = book.active
    row = 1
    for i in my_list:
        sheet.cell(row=row, column=2).value = my_list[row - 1]
        row += 1
    book.save(excel_file)
    book.close()

create_excel('ch14.txt', 'ch14.xlsx')