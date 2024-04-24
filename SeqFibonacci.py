def fibonacci(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        seq = [0, 1]
        while seq[-1] < n:
            seq.append(seq[-1] + seq[-2])
        return seq

def verifica_na_sequencia(n, seq):
    if n in seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

n = int(input("Informe um número: "))
seq = fibonacci(n)
mensagem = verifica_na_sequencia(n, seq)
print(mensagem)
