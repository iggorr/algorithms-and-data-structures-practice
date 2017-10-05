def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)


    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(5,3,5,6,Igor=335,Agne=515,Russell=222))
