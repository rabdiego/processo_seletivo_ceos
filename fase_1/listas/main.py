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


def simple_partition(l1: list, l2 : list, start, finish) -> None:
    x = l1[start]
    n = len(l1)
    i, j = start + 1, finish

    i_fix, j_fix = 0, 0
    l1_fix, l2_fix = list(), list()
    while i <= j:
        if i >= n:
            i_fix, j_fix = i - n, j - n
            l1_fix, l2_fix = l2, l2
        elif j >= n:
            i_fix, j_fix = i, j - n
            l1_fix, l2_fix = l1, l2
        else:
            i_fix, j_fix = i, j
            l1_fix, l2_fix = l1, l2
        
        if l1_fix[i_fix] > x and l2_fix[j_fix] < x:
            l1_fix[i_fix], l2_fix[j_fix] = l2_fix[j_fix], l1_fix[i_fix]
        
        if l1_fix[i_fix] < x: i += 1 
        if l2_fix[j_fix] > x: j -= 1 
    
    if j >= n:
        j_fix = j - n
        l1[start], l2[j_fix] = l2[j_fix], l1[start]
    else:
        l1[start], l2[j] = l2[j], l1[start]



l1 = [5, 1, 2, 3, 4]
l2 = [6, -1, 7, 8, 9]
simple_partition(l1, l2, 3, 6)
print(l1)
print(l2)