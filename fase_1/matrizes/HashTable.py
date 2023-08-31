class HashTable:
    """
    Classe de implementação da estrutura de dados Hash Table,
    que utiliza o encadeamento simples para lidar com colisões.
    
    Utilizada para verificar se há elementos repetidos em
    uma matriz em ordem média de O(n)
    """
    def __init__(self, vector_size : int) -> None:
        """Construtor"""
        self.base = [[] for i in range(vector_size)]  # O(1) (em relação ao número de elementos da matriz)
        self.n = vector_size  # O(1)
        # O(1) + O(1) => O(1)
    
    
    def hash_function(self, n : int) -> int:
        """Função de disperção"""
        return n % self.n  # O(1)
    
    
    def add(self, n : int) -> None:
        """Adicionando um elemento no vetor base"""
        idx = self.hash_function(n)  # O(1)
        self.base[idx].append(n)  #  O(n) no pior caso, O(1) no melhor caso e caso médio
    
    
    def find_on_list(self, l : list, n : int) -> int:
        """
        Função auxiliar para achar um elemento em uma lista.
        
        Alternativa ao método .find()
        """
        for idx, element in enumerate(l):  # O(c), onde c é o número de colunas da matriz
            if element == n:  # O(1)
                return idx  # O(1)
        
        return -1  # O(1)
        # O(1)*O(1)*O(c) + O(1) => O(c)

    
    def _get_index_on_list(self, n : int) -> int:
        idx = self.hash_function(n)  # O(1)
        found = self.find_on_list(self.base[idx], n)
        return (idx, found)
    
    
    def has(self, n : int) -> bool:
        """Checando se um elemento está presente na tabela"""
        _, found = self._get_index_on_list(n)
        if found >= 0:
            return True
        return False
        """
        Em teoria, a operação custaria na ordem de O(c), porém
        na aplicação de uma Hash Table com números aleatórios e uma
        boa função de disperção, temos um caso médio de O(1).
        """


    def delete(self, idx_base : int, idx_list : int) -> None:
        """Deletando um elemento presente no HashTable"""
        self.base[idx_base].pop(idx_list)
        # O(1)
