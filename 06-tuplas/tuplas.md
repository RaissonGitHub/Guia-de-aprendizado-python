# Tuplas em Python

Imagine uma tupla como um boleto já emitido ou um certificado de nascimento: depois que o documento é criado, você não pode mais alterar seu conteúdo. Ela é definitiva. Outra comparação útil é uma caixa lacrada: você pode olhar o que tem dentro (acessar valores), mas não consegue mudar nada lá dentro. Por isso, tuplas são ideais para dados que não devem ser modificados.

## O que são tuplas?

Tuplas são coleções ordenadas, imutáveis e que aceitam valores duplicados. Imutável significa que, depois de criada, você não pode modificar seus valores.

## Como criar tuplas

```py
minha_tupla = (1, 2, 3)
```

**Atenção com tuplas de um único elemento:**

```py
tupla_unica = (5,)  # Correto
nao_tupla = (5)     # Isso é apenas um número
```

## Acessando tuplas

```py
cores = ("azul", "verde", "vermelho")
print(cores[0])  # azul
```

## Fatiamento de tuplas

Funciona igual ao fatiamento de listas:

```py
tupla = (10, 20, 30, 40, 50)
print(tupla[1:4])   # (20, 30, 40)
print(tupla[::-1])  # (50, 40, 30, 20, 10)
```

## Métodos das tuplas

Tuplas são como uma caixa lacrada: você consegue ver o conteúdo, mas não pode mexer dentro. Por isso, não possuem métodos de modificação. Os métodos disponíveis são:

`count(valor)`: conta quantas vezes o valor aparece na tupla.

```py
t = (1, 2, 3, 3)
t.count(3)
```

`index(valor)`: retorna o índice da primeira ocorrência do valor.

```py
t = ("azul", "verde", "azul")
t.index("azul")
```

As tuplas também permitem fatiamento, igual às listas:

```py
tupla = (10, 20, 30, 40)
print(tupla[1:3])  # (20, 30)
```

Use tuplas quando os dados não devem ser alterados.

## Iterando sobre tuplas

A iteração acontece da mesma forma que em listas:

```py
for item in (1, 2, 3):
    print(item)
```
