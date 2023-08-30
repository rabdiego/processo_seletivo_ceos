def third_biggest_element(l : list) -> int:
    big, sec_big, third_big = float('-inf'), float('-inf'), float('-inf')
    for element in l:
        if element > big:
            third_big = sec_big
            sec_big = big
            big = element
        elif element > sec_big:
            third_big = sec_big
            sec_big = element
        elif element > third_big:
            third_big = element
    return third_big


print(third_biggest_element([1, 2, 3, 4, 5, 6, 7, 8, -3, -2, -1]))