def transformar_vetor(A):
    B = []
    for numero in A:
        if numero % 2 == 0:  # Verifica se o número é par
            B.append(numero * 5)
        else:  # Se o número é ímpar
            B.append(numero + 3)
    return B

def main():
    A = []
    print("Digite 10 números inteiros:")
    for i in range(10):
        numero = int(input(f"Digite o número {i+1}: "))
        A.append(numero)
    
    B = transformar_vetor(A)
    
    print("Vetor A:", A)
    print("Vetor B:", B)

if __name__ == "__main__":
    main()