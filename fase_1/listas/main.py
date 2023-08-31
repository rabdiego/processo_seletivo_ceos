from HashTable import HashTable

def third_biggest_element(l : list) -> int:
    """
    Função para retornar o terceiro maior elemento de uma lista
    """
    big, sec_big, third_big = float('-inf'), float('-inf'), float('-inf')  # O(1)
    for element in l:  # O(n)
        # Todas as operações abaixos são O(1)
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
    # O(1)*O(n) => O(n)


def partition_lists(l1 : list, l2 : list) -> None:
    """
    Função para particionar duas listas, da forma que todos os elementos
    da primeira sejam menores ou iguais que o menor elemento da segunda
    """
    def simple_partition(l1: list, l2 : list, start, finish) -> int:
        """
        Função de partição simples, porém aplicada para suportar manipulação em
        duas listas
        """
        n = len(l1)

        if start >= n:
            relative_start = start - n
            l_final = l2
        else:
            relative_start = start
            l_final = l1

        x = l_final[relative_start]
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
                l1_fix, l2_fix = l1, l1
            
            if l1_fix[i_fix] > x and l2_fix[j_fix] < x:
                l1_fix[i_fix], l2_fix[j_fix] = l2_fix[j_fix], l1_fix[i_fix]
            
            if l1_fix[i_fix] < x: i += 1 
            if l2_fix[j_fix] > x: j -= 1 
        
        if j >= n:
            j_fix = j - n
            l_final[relative_start], l2[j_fix] = l2[j_fix], l_final[relative_start]
        else:
            l_final[relative_start], l1[j] = l1[j], l_final[relative_start]
        
        return j

    n = len(l1)
    i, j = 0, 2*n - 1
    k, goal = 0, n

    while k != goal:
        k = simple_partition(l1, l2, i, j)
        if k > goal:
            i, j = 0, k
        else:
            i, j = k + 1, 2*n - 1


def are_lists_permutations(l1 : list, l2 : list) -> bool:
    """
    Função para checar se duas listas são permutações entre elas
    """
    ht = HashTable(53)

    for element in l1:
        ht.add(element)
    
    for element in l2:
        if ht.has(element):
            ht.delete(element)
        else:
            return False
    
    return True

