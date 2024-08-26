import random

def escolher_palavra():
    palavras = ['python', 'javascript', 'programacao', 'desenvolvedor', 'software']
    return random.choice(palavras)

def jogar():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    print("_ " * len(palavra_secreta))
    
    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_adivinhadas.append(letra)
        
        if letra in palavra_secreta:
            print("Boa! A letra", letra, "está na palavra.")
        else:
            tentativas -= 1
            print("A letra", letra, "não está na palavra. Você tem", tentativas, "tentativas restantes.")
        
        estado_atual = [letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta]
        print(' '.join(estado_atual))
        
        if "_" not in estado_atual:
            print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
            break
    else:
        print("Game Over! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    jogar()
