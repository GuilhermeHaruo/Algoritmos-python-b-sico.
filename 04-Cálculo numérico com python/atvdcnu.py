import numpy as np

def jacobi(A, b, x0, epsilon, max_iter):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_novo = np.zeros_like(x)
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_novo[i] = (b[i] - soma) / A[i][i]
        erro = np.linalg.norm(x_novo - x, np.inf) / np.linalg.norm(x_novo, np.inf)
        if erro <= epsilon:
            return x_novo, k + 1, erro
        x = x_novo
    return x, max_iter, erro


def gauss_seidel(A, b, x0, epsilon, max_iter):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_ant = x.copy()
        for i in range(n):
            soma1 = sum(A[i][j] * x[j] for j in range(i))
            soma2 = sum(A[i][j] * x_ant[j] for j in range(i + 1, n))
            x[i] = (b[i] - soma1 - soma2) / A[i][i]
        erro = np.linalg.norm(x - x_ant, np.inf) / np.linalg.norm(x, np.inf)
        if erro <= epsilon:
            return x, k + 1, erro
    return x, max_iter, erro


# ==========================
# Programa principal
# ==========================

print("=== Método Iterativo ===")
N = int(input("Digite a ordem da matriz (N): "))

A = np.zeros((N, N))
b = np.zeros(N)

print("\nDigite os elementos da matriz A:")
for i in range(N):
    for j in range(N):
        A[i][j] = float(input(f"A[{i+1},{j+1}] = "))

print("\nDigite os elementos do vetor b:")
for i in range(N):
    b[i] = float(input(f"b[{i+1}] = "))

x0 = np.zeros(N)
epsilon = float(input("\nDigite a tolerância (ex: 1e-5): "))
max_iter = int(input("Digite o número máximo de iterações: "))

print("\nEscolha o método:")
print("1 - Jacobi (Algoritmo 2.9)")
print("2 - Gauss-Seidel (Algoritmo 2.10)")
opcao = int(input("Opção: "))

if opcao == 1:
    x, k, erro = jacobi(A, b, x0, epsilon, max_iter)
    metodo = "Jacobi"
elif opcao == 2:
    x, k, erro = gauss_seidel(A, b, x0, epsilon, max_iter)
    metodo = "Gauss-Seidel"
else:
    print("Opção inválida!")
    exit()

print("\n=== Resultado ===")
print(f"Método: {metodo}")
print(f"Solução aproximada x = {x}")
print(f"Iterações realizadas: {k}")
print(f"Erro final: {erro:.6e}")
