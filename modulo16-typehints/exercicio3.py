from typing import List, Dict

def media(numeros: List[float]) -> float:
    return sum(numeros) / len(numeros)

#print(media([10.0, 20.0, 30.0]))

def contar_palavras(texto:str) -> Dict[str, int]:
    palavras = texto.split()
    contagem: Dict[str, int] = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

print(contar_palavras("python e python e code"))
