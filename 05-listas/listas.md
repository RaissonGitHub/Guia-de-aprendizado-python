# Listas em Python
## O que são listas?
Imagine uma **lista** como uma **fila de pessoas no supermercado**.

Cada pessoa ocupa uma posição específica na fila, e essa posição importa. Você pode adicionar novas pessoas ao final, pedir para alguém entrar em uma posição específica ou até remover alguém. Por serem mutáveis, as listas funcionam exatamente assim: uma sequência de elementos em ordem, que pode ser alterada a qualquer momento.

Listas são coleções **ordenadas**, **mutáveis** e que **aceitam valores duplicados**. Elas são uma das estruturas mais usadas na linguagem, pois permitem armazenar vários valores em uma única variável.

**Mutável** significa que é possível alterar seus elementos após a criação: adicionar, remover ou modificar.

## Como criar listas
``minha_lista = [1, 2, 3, "texto", True]``

Uma lista é sempre escrita usando colchetes ``[]``.

## Características principais
* Mantêm a ordem dos elementos
* Aceitam valores duplicados
* São mutáveis
* Podem armazenar qualquer tipo de dado


## Acessando elementos de uma lista
Assim como em muitas linguagens, o índice começa em 0.
```py
numeros = [10, 20, 30, 40]
print(numeros[0])  # 10
print(numeros[2])  # 30
```

## Modificando listas
```py
lista = [10, 20, 30]
lista[1] = 15
print(lista)  # [10, 15, 30]
```
## Métodos importantes das listas
Vamos ver cada método com explicações e exemplos.

`append(x)` — adiciona no finalda lista
```py
lista.append(40)
lista = [1, 2]
lista.append(3)
print(lista)  # [1, 2, 3]
```
---

`extend(iterável)` — adiciona vários elementos na lista
```py
lista = [1, 2]
lista.extend([3, 4])
print(lista)  # [1, 2, 3, 4]
```
---

`insert(posição, item)`
Insere um item em uma posição específica.
É como pedir que alguém entre no meio da fila.
```py
lista.insert(2, 50)
```
Use quando você precisa colocar algo em um local exato.

---

 ``remove(item)``
Remove a primeira ocorrência de um valor.
Imagine chamar uma pessoa pelo nome e retirá-la da fila.
```py
lista.remove(20)
```
Use quando você sabe o valor, mas não a posição.

---

`pop(índice)`
Remove e retorna o item do índice indicado. Sem índice, remove o último.
É como tirar alguém da fila e ainda receber o nome dessa pessoa.
```py
ultimo = lista.pop()
primeiro = lista.pop(0)
```
Use quando precisar do valor removido.

---

`clear()`
Remove todos os itens.
É como esvaziar completamente a fila.
```py
lista.clear()
```

---

`index(valor)`
Retorna o índice da primeira ocorrência do valor.
Procura em que posição da fila a pessoa está.
```py
pos = lista.index(30)
```

---

`count(valor)`
Conta quantas vezes o valor aparece.
Imagine contar quantas pessoas com o mesmo nome estão na fila.
```py
lista.count(10)
```

---

`sort()`
Ordena a lista em ordem crescente.
 Organiza a fila segundo algum critério.
```py
lista.sort()
```
Use quando quiser ordenar números ou palavras.

---

`reverse()`
Inverte a ordem dos elementos.
A fila vira do avesso.
```py
lista.reverse()
```

## Fatiamento (slicing) de listas
Fatiamento permite pegar partes da lista usando:
```py
lista[início:fim:passo]
```

Exemplos:
```py
lista = [10, 20, 30, 40, 50]
print(lista[1:4])   # [20, 30, 40]
print(lista[:3])    # [10, 20, 30]
print(lista[3:])    # [40, 50]
print(lista[::2])   # [10, 30, 50]
print(lista[::-1])  # [50, 40, 30, 20, 10]
```

## Listas aninhadas (listas dentro de listas)
Também chamadas de matrizes ou tabelas.
```py
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][2])  # 6
```

## Iterando sobre listas
```py
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)
```

## Operadores in e not in
Estes dois operadores lógicos verificam se uma variável está presente ou não dentro de uma lista. Ao o usar o operador `in`, espera-se que, caso tal variável esteja presente na lista, ele retorne `True`. O mesmo ocorre para o `not in`, que retorna verdadeiro caso a variável não esteja presente na lista.
```py
"banana" in frutas      # True
"laranja" not in frutas # True
```