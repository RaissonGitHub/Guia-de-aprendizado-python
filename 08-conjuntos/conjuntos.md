# Conjuntos (Sets) em Python

Para entender os sets, imagine um conjunto de figurinhas repetidas: você guarda apenas uma de cada e descarta as cópias. Os conjuntos em Python funcionam da mesma forma, eliminando duplicatas automaticamente e ignorando a ordem dos elementos. Outra analogia é um grupo de alunos inscritos em uma atividade: não importa a ordem das inscrições, apenas quem está no grupo.

## O que são conjuntos?

Sets são coleções **não ordenadas**, **mutáveis** e que não** permitem valores duplicados**.

Isso os torna ideais para situações onde a unicidade dos elementos importa.

## Como criar um conjunto
**Exemplo:**
```py
meu_set = {1, 2, 2, 3}
print(meu_set)  # {1, 2, 3}
```

## Adicionando itens a um conjunto

Sets funcionam como um grupo de figurinhas sem repetição: não importa a ordem, e duplicatas não existem.

### add(item)

Adiciona um novo item ao conjunto.

**Exemplo:**
```py
s = {1, 2}
s.add(5)
```
## Removendo elementos de um conjunto (set)
Assim como acontecia com listas, também é possível remover elementos de um conjunto.

Porém, **é muito importante lembrar que sets não possuem índices**, então você sempre remove itens pelo valor, nunca pela posição.

A seguir estão os principais métodos de remoção e quando usá-los:

### remove(item)
Remove um item específico do conjunto.
* Se o item não existir, ocorre um erro (KeyError).
* Use quando você tem certeza de que o item está no conjunto.

**Exemplo:**
```py
frutas = {"maçã", "banana", "uva"}
frutas.remove("banana")
print(frutas)  
# {'maçã', 'uva'}
```

### discard(item)
Também remove um item específico, mas **NÃO gera erro se o item não existir**.
* Sempre seguro de usar.
* Mais recomendado quando não temos certeza da presença do elemento.
  
**Exemplo:**
```py
frutas = {"maçã", "banana", "uva"}
frutas.discard("laranja")  # não existe, mas não gera erro
print(frutas)  
```
### pop()
Remove e retorna **um elemento aleatório** do `set`.
* Lembre que `sets` não são ordenados.
* Útil quando você só quer "pegar e remover qualquer elemento".
  
**Exemplo:**
```py
numeros = {10, 20, 30}
removido = numeros.pop()
print("Removi:", removido)
print(numeros) 
```
### clear()
Remove **todos os elementos**, deixando o set vazio.

**Exemplo:**
```py
s = {1, 2, 3}
s.clear()
print(s)  # set()
```

## Exemplo: removendo duplicatas e ordenando nomes

```py
entrada = "Ana, Ana, Bruno, Carla"
nomes = [nome.strip() for nome in entrada.split(",")]

# Passo 1: remover duplicatas
nomes_unicos = set(nomes)

# Passo 2: voltar para lista
nomes_unicos = list(nomes_unicos)

# Passo 3: ordenar
nomes_unicos.sort()

print("Nomes únicos e ordenados:")
print(nomes_unicos)
```

- `split()` separa a entrada em partes.
- `strip()` remove espaços antes e depois de cada nome.
- `set()` elimina duplicatas.
- `sort()` coloca em ordem alfabética.


## Convertendo outros tipos para conjuntos

Conjuntos podem ser criados a partir de listas, tuplas e até strings, o que é muito útil para remover elementos duplicados.

**Exemplo:**
```py
lista = [1, 2, 2, 3, 3, 3]
unico = set(lista)
print(unico)  # {1, 2, 3}
```

## Iterando sobre conjuntos

Assim como listas e tuplas, podemos percorrer um conjunto com `for`. Lembre-se de que a ordem pode mudar a cada execução.

**Exemplo:**
```py
frutas = {"maca", "banana", "uva"}

for fruta in frutas:
    print(fruta)
```

## Operações matemáticas com conjuntos

Os conjuntos foram inspirados em conjuntos da matemática. Assim, é possível realizar operações como:
* União
* Interseção
* Diferença
* Diferença simétrica
Vamos explicar cada uma com bastante calma e analogias.

Imagine conjuntos como **duas caixas com objetos dentro**, onde cada objeto só pode aparecer uma vez em cada caixa.

Use estes métodos para entender como dois conjuntos se relacionam.

### União — set1 | set2 ou set1.union(set2)

Pense assim: é como juntar os objetos de duas caixas, **sem repetir itens**.

**Exemplo:**
```py
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}
```
### Interseção — set1 & set2 ou set1.intersection(set2)
É o que existe **nas duas caixas ao mesmo tempo**.
```py
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # {2, 3}
```
### Diferença — set1 - set2 ou set1.difference(set2)
Imagine retirar da primeira caixa todos os itens que também estão na segunda.

**Exemplo:**
```py
a = {1, 2, 3}
b = {3, 4}
print(a - b)  # {1, 2}
```

### Diferença simétrica — set1 ^ set2 ou set1.symmetric_difference(set2)
É como pegar tudo o que existe em **apenas uma das caixas**, excluindo o que é comum.

**Exemplo:**
```py
a = {1, 2, 3}
b = {3, 4}
print(a ^ b)  # {1, 2, 4}
```
## Métodos de comparação entre conjuntos
Estes métodos servem para saber como dois conjuntos se relacionam.
Pense em **uma caixa menor dentro de outra**, ou **duas caixas sem nada em comum**.

### isdisjoint() — verifica se os conjuntos NÃO têm elementos em comum

Imagine duas caixas completamente diferentes.
Se nada se repete, retorna `True`.

**Exemplo:**
```py
a = {1, 2, 3}
b = {4, 5}
print(a.isdisjoint(b))  # True
```

### issubset() — verifica se um conjunto está contido em outro

É como perguntar:
**“Todos os itens da caixa A cabem dentro da caixa B?”**

**Exemplo:**
```py
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))  # True
```

### issuperset() — verifica se o conjunto é maior e contém outro dentro dele

É o contrário de `issubset()`.
**“A caixa B contém todos os itens da caixa A?”**

**Exemplo:**
```py
b = {1, 2, 3, 4}
a = {1, 2}
print(b.issuperset(a))  # True
```

## Operadores `in` e `not in`

Os `sets` são a estrutura mais rápida do Python para verificar se algo está presente.
* `in` → verifica se algo existe
* `not in` → verifica se algo não existe

**Exemplo:**
```python
nomes = {"Ana", "Lucas", "Joao"}
print("Ana" in nomes)        # True
print("Carlos" not in nomes) # True
```

Por isso, sets são muito usados para:
- verificar presença de valores rapidamente
- evitar duplicatas
- comparar grupos de informações

