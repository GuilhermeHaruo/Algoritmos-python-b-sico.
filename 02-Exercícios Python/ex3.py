
def criar_vetor():
    vetor = []

   
    print("Digite 10 números:")
    for i in range(10):
        num = float(input(f"Número {i+1}: "))
        vetor.append(num)

   
    for i in range(9, -1, -1):
        vetor.append(vetor[i])

    return vetor

def main():
    vetor_final = criar_vetor()
    print("Vetor final:")
    print(vetor_final)


if __name__ == "__main__":
    main()