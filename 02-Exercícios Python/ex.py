def encontrar_maior(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

def encontrar_menor(numeros):
    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    return menor

def main():
    numeros = []
    for i in range(5):
        numero = float(input(f"Digite o número {i+1}: "))
        numeros.append(numero)
    
    maior = encontrar_maior(numeros)
    menor = encontrar_menor(numeros)
    
    print(f"O maior número digitado é: {maior}")
    print(f"O menor número digitado é: {menor}")

if __name__ == "__main__":
    main()