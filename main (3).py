class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self, elemento):
        self.pilha.append(elemento)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.pilha.pop()

    def esta_vazia(self):
        return len(self.pilha) == 0

def inverter_palavras(texto):
    pilha = Pilha()
    resultado = ""
    for caractere in texto:
        if caractere != " " and caractere != ".":
            pilha.empilhar(caractere)
        else:
            while not pilha.esta_vazia():
                resultado += pilha.desempilhar()
            resultado += caractere
    return resultado

sentenca = input().strip()  # Lê a sentença de entrada
resultado = inverter_palavras(sentenca)

print(resultado.replace(".", ""))
