# Número a ser adivinhado
numero_correto = 7
tentativas = 3

# Loop para as tentativas
for tentativa in range(tentativas):
    # Solicita que o jogador faça uma tentativa
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    
    # Verifica se o palpite está correto
    if palpite == numero_correto:
        print("Parabéns! Você acertou o número!")
        break
    else:
        print("Tente novamente.")
else:
    print("Você esgotou suas tentativas. O número correto era 7. Tente novamente na próxima vez!")
