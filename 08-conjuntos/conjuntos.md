# Conjuntos (Sets) em Python

Para entender os sets, imagine um conjunto de figurinhas repetidas: você guarda apenas uma de cada e descarta as cópias. Os conjuntos em Python funcionam da mesma forma, eliminando duplicatas automaticamente e ignorando a ordem dos elementos. Outra analogia é um grupo de alunos inscritos em uma atividade: não importa a ordem das inscrições, apenas quem está no grupo.

## O que são conjuntos?

Conjuntos são coleções não ordenadas, mutáveis e que não permitem valores duplicados. Eles são ideais quando a unicidade dos elementos importa.

## Como criar um conjunto

```py
meu_set = {1, 2, 2, 3}
print(meu_set)  # {1, 2, 3}
```

## Métodos principais dos conjuntos

Conjuntos funcionam como um grupo de figurinhas sem repetição: duplicatas desaparecem e a ordem não importa.

### add(item)

Adiciona um novo item ao conjunto.

```py
s = {1, 2}
s.add(5)
```

Use quando desejar inserir elementos únicos.

### remove(item)

Remove um item específico e gera um erro (`KeyError`) se ele não existir.

```py
s = {1, 2, 3}
s.remove(2)
```

Use quando tiver certeza de que o item está presente.

### discard(item)

Remove o item, mas não gera erro se ele não existir.

```py
s = {1, 2, 3}
s.discard(4)  # Seguro mesmo se o elemento não existir
```

### pop()

Remove e retorna um item aleatório (como sets não têm ordem, você não controla qual sai).

```py
s = {10, 20, 30}
removido = s.pop()
```

### clear()

Remove todos os elementos do conjunto.

```py
s = {1, 2, 3}
s.clear()
print(s)  # set()
```

### union(outro_set)

Retorna um novo conjunto com todos os elementos presentes em qualquer um dos conjuntos.

```py
A = {1, 2}
B = {2, 3}
print(A.union(B))  # {1, 2, 3}
```

### intersection(outro_set)

Retorna apenas os elementos em comum.

```py
A = {1, 2, 3}
B = {2, 3, 4}
print(A.intersection(B))  # {2, 3}
```

### difference(outro_set)

Retorna os itens que estão em um conjunto e não estão no outro.

```py
A = {1, 2, 3}
B = {2, 4}
print(A.difference(B))  # {1, 3}
```

### symmetric_difference(outro_set)

Retorna os elementos exclusivos de cada conjunto (fora da interseção).

```py
A = {1, 2, 3}
B = {3, 4}
print(A.symmetric_difference(B))  # {1, 2, 4}
```

### issubset(outro_set)

Verifica se todos os elementos de um conjunto estão em outro.

```py
A = {1, 2}
B = {1, 2, 3}
print(A.issubset(B))  # True
```

### issuperset(outro_set)

Verifica se um conjunto contém todos os elementos de outro.

```py
A = {1, 2, 3}
B = {1, 2}
print(A.issuperset(B))  # True
```

### isdisjoint(outro_set)

Verifica se dois conjuntos não possuem elementos em comum.

```py
A = {1, 2, 3}
B = {4, 5}
print(A.isdisjoint(B))  # True
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

## Diferença entre conjuntos

A operação de diferença responde à pergunta: quais elementos estão em um conjunto, mas não no outro? Imagine dois grupos de alunos: um participou da aula de Python e outro da aula de Java. A diferença revela quem participou apenas da aula de Python.

```py
a = {1, 2, 3, 4}
b = {3, 4, 5}

resultado = a.difference(b)
print(resultado)  # {1, 2}

resultado = a - b
print(resultado)  # {1, 2}
```

## Diferença simétrica

A diferença simétrica retorna todos os elementos que estão em um conjunto ou no outro, mas não nos dois. É útil para descobrir quem participou apenas de uma das aulas.

```py
a = {1, 2, 3}
b = {3, 4, 5}

resultado = a.symmetric_difference(b)
print(resultado)  # {1, 2, 4, 5}

resultado = a ^ b
print(resultado)  # {1, 2, 4, 5}
```

## Testando subconjuntos

Um conjunto é subconjunto de outro quando todos os seus elementos também estão presentes no outro conjunto. Pense em um álbum de figurinhas: se você tem as figurinhas `{1, 2}` e o álbum completo possui `{1, 2, 3, 4}`, o seu conjunto é subconjunto do álbum.

```py
aluno_basico = {1, 2}
aluno_avancado = {1, 2, 3, 4}

print(aluno_basico.issubset(aluno_avancado))  # True
```

## Testando superconjuntos

O oposto também vale: um conjunto é superconjunto quando contém todos os elementos de outro.

```py
aluno_avancado = {1, 2, 3, 4}
aluno_basico = {1, 2}

print(aluno_avancado.issuperset(aluno_basico))  # True
```

## Conjuntos disjuntos

Dois conjuntos são disjuntos quando não possuem nenhum elemento em comum. Imagine duas sacolas de brinquedos sem nenhum item repetido.

```py
brinquedos1 = {"bola", "carrinho"}
brinquedos2 = {"boneca", "quebra-cabeca"}

print(brinquedos1.isdisjoint(brinquedos2))  # True
```

## Convertendo outros tipos para conjuntos

Conjuntos podem ser criados a partir de listas, tuplas e até strings, o que é muito útil para remover elementos duplicados.

```py
lista = [1, 2, 2, 3, 3, 3]
unico = set(lista)
print(unico)  # {1, 2, 3}
```

## Iterando sobre conjuntos

Assim como listas e tuplas, podemos percorrer um conjunto com `for`. Lembre-se de que a ordem pode mudar a cada execução.

```py
frutas = {"maca", "banana", "uva"}

for fruta in frutas:
    print(fruta)
```

## Removendo elementos de um conjunto

Sets não possuem índices, então removemos itens pelo valor.

```python
frutas = {"maca", "banana", "uva"}
frutas.remove("banana")
print(frutas)  # {'maca', 'uva'}

frutas.discard("laranja")  # Seguro se o item não existir
print(frutas)

numeros = {10, 20, 30}
removido = numeros.pop()
print("Removi:", removido)
print(numeros)
```

## Operações matemáticas com conjuntos

Conjuntos foram inspirados na matemática, então podemos realizar união, interseção, diferença e diferença simétrica. Pense em duas caixas com objetos únicos.

```python
a = {1, 2, 3}
b = {3, 4, 5}

# União
print(a | b)                 # {1, 2, 3, 4, 5}
print(a.union(b))            # {1, 2, 3, 4, 5}

# Interseção
print(a & b)                 # {3}
print(a.intersection(b))     # {3}

# Diferença
print(a - b)                 # {1, 2}
print(a.difference(b))       # {1, 2}

# Diferença simétrica
print(a ^ b)                 # {1, 2, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
```

## Métodos de comparação

Use estes métodos para entender como dois conjuntos se relacionam.

```python
a = {1, 2, 3}
b = {4, 5}
print(a.isdisjoint(b))  # True

a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))    # True

print(b.issuperset(a))  # True
```

## Operadores `in` e `not in`

Conjuntos são a estrutura mais rápida do Python para verificar presença de elementos.

```python
nomes = {"Ana", "Lucas", "Joao"}

print("Ana" in nomes)        # True
print("Carlos" not in nomes) # True
```

Use sets para verificar valores rapidamente, evitar duplicatas e comparar grupos de informações.
