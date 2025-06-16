
def eh_primo(n, divisor = 2):
    if n < 2:
        return False
    if divisor > n // 2:
        return True
    if n % divisor == 0:
        return False
    
    return eh_primo(n, divisor + 1)

def primos_recursivo(n, atual = 2, primos = None):
    if primos is None:
        primos = []
    if atual > n:
        return primos
    if eh_primo(atual):
        primos.append(atual)

    return primos_recursivo(n, atual + 1, primos)

def primos_linear(n):
    if n <= 1:
        raise ValueError("O número deve ser maior que 1.")
    
    primos = []
    for num in range(2, n + 1):
        eh_primo = True
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                eh_primo = False
                break

        if eh_primo:
            primos.append(num)
    return primos

def main():
    while True:
        try:
            n = int(input("Digite um número inteiro (n > 1): "))
            if n <= 1:
                raise ValueError("N deve ser maior que 1.")
            
            print(f"\nPrimos até {n} (Recursivo): {primos_recursivo(n)}")
            print(f"\nPrimos até {n} (Linear): {primos_linear(n)}")

            # coloquei esta opção de resposta para facilitar novas verificações, 
            # assim o usuário não terá que compilar o programa de novo 
            # caso queira verificar um novo número.
            while True:
                resp = input("\nDeseja verificar mais um número (S/N)?").strip().upper()
                if resp in ("S", "N"):
                    break
                print("Resposta inválida. Digite apenas 'S' ou 'N'.")

            if resp == "N":
                print("Encerrando programa...")
                break

        except ValueError as e:
            print("Erro: ", e)


if __name__ == "__main__":
    main()       