from HashTable import HashTable

def read_txt_to_matrix(path : str) -> list:
    """
    Função de leitura de um arquivo-texto, que salva
    sua informação em uma matriz (lista de listas).
    """
    
    return_matrix = list()  # O(1)
    with open(path, 'r') as f:
        for line in f.readlines():  # O(l)
            return_matrix.append(list(map(int, line.split(' '))))  # O(c), onde c é o número de colunas
    return return_matrix  # O(1)
    # O(1) + O(l)*O(c) + O(1) => O(l)*O(c) => O(n)


def print_matrix(matrix : list) -> None:
    """
    Função para imprimir uma matriz na tela
    """
    line_len = len(matrix[0])  # O(1) ou O(n) (depende da implementação da função len() e da classe list do Python)
    for line in matrix:  # O(l)
        print('[', end='')  # O(1)

        for idx, num in enumerate(line):  # O(c)
            if idx == line_len - 1:  # O(1)
                print(f'{num}', end='')  # O(1)
            else:  # O(1)
                print(f'{num}, ', end='')  # O(1)
        
        print(']')  # O(1)
    
    # O(n) + O(l)*O(c)*O(1) + O(1) => O(n)


def find_duplicate_on_matrix(matrix : list, hash_table_size : int = 53) -> bool:
    """
    Função para achar um item duplicado em uma matriz
    """
    ht = HashTable(hash_table_size)  # O(1) em relação ao tamanho da lista
    # Nota: utilizei um número primo, pois pela minha função de disperção, esses números são preferíveis
    # O tamanho do vetor base pode variar para melhor acomodar o custo do algoritmo
    
    for line in matrix:  # O(l)
        for element in line:  # O(c)
            if ht.has(element):  # O(1) no caso médio
                return True  # O(1)
            ht.add(element)  # O(1) no caso médio
    
    return False  # O(1)
    # O(l)*O(c)*O(1) + O(1) => O(n) no caso médio

