def imprimir_matriz(matriz : list) -> None:
    line_len = len(matriz[0])
    for line in matriz:
        print('[', end='')

        for idx, num in enumerate(line):
            if idx == line_len - 1:
                print(f'{num}', end='')
            else:
                print(f'{num}, ', end='')
        
        print(']')

