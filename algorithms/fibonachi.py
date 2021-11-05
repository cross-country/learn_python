def fibonachi(items, start_digit = 1):
    items = items
    start = start_digit
    fib_list = [0, start]
    for i in range(2, items):
        fib = fib_list[len(fib_list) -2] + fib_list[len(fib_list) - 1]
        fib_list.append(fib)
    print(fib_list)

fibonachi(5)

