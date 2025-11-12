# Fundamentos de Programação

Python é uma linguagem extremamente poderosa, mas, antes de chegar nas partes mais avançadas (módulos, pacotes e organização profissional de código), precisamos entender os **fundamentos da programação** — os blocos de construção usados em qualquer programa, independente do tamanho.

Aprender esses fundamentos é como aprender a dirigir: ninguém começa pilotando um caminhão; primeiro você entende o volante, os pedais e os sinais... depois vai praticando até conseguir coordenar tudo.

## Variáveis

Uma variável pode ser entendida como uma "caixa com rótulo onde armazenamos um valor para usar depois." Em Python, criamos variáveis assim:

```py
nome = "Carlos"
idade = 19
nota = 8.5
```

Nesse momento:

- `nome` guarda o texto "Carlos"
- `idade` guarda o número inteiro `19`
- `nota` guarda o número decimal `8.5`

Imagine que você está arrumando seu quarto e decide organizar tudo em caixas com etiquetas:

- Caixa “Documentos"
- Caixa “Fios"
- Caixa “Ferramentas"
- Caixa “Lembranças"

Cada caixa guarda um conteúdo diferente, e você sempre sabe o que tem dentro porque existe um nome na frente. Uma variável funciona exatamente assim.

### Por que isso é tão importante?

Porque um programa precisa armazenar:

- dados digitados pelo usuário
- valores de cálculos
- estados do sistema
- nomes, preços, quantidades
- mensagens
- resultados intermediários

Sem variáveis, seria impossível montar qualquer aplicação.

## Constantes

Python não obriga o uso de constantes, mas a comunidade usa nomes em MAIÚSCULAS para indicar valores que não deveriam mudar. Exemplo:

```py
PI = 3.14159
TAMANHO_MAXIMO = 100
COR_PADRAO = "AZUL"
```

Constantes são como aqueles objetos da casa que você não troca de lugar — tecnicamente podem ser alteradas, mas não deveriam.

## Tipos Primitivos

Em Python, os tipos básicos são como categorias de objetos dentro da sua "caixa" (variável). Cada tipo tem um propósito:

- **int** — números inteiros (ex.: `1`, `200`, `-3`)
- **float** — números decimais (ex.: `3.14`, `-0.5`, `10.0`)
- **bool** — valores lógicos (ex.: `True`, `False`)
- **str** — textos (ex.: `"Python"`, `"Olá"`)

Exemplos de uso:

- `int`: quantidade de pessoas na fila
- `float`: altura, preço, peso
- `bool`: interruptor (ligado/desligado)
- `str`: texto

## Entrada e Saída de Dados

- Saída — `print()`

```py
print("Bem-vindo ao Python!")
```

- Entrada — `input()`

```py
nome = input("Digite seu nome: ")
print("Olá,", nome)
```

**Importante:** `input()` sempre retorna texto (`str`). Se quiser transformar em número, use conversões:

```py
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
```

## Conversão de Tipos

Converter tipos é mudar o formato de um dado. Exemplos:

```py
int("10")    # vira inteiro 10
float("3.14")# vira 3.14
str(50)        # vira "50"
bool(0)        # vira False
```

## Operadores Aritméticos

Principais operadores:

- `+`  (adição): `5 + 2` -> `7`
- `-`  (subtração): `5 - 2` -> `3`
- `*`  (multiplicação): `5 * 2` -> `10`
- `/`  (divisão): `5 / 2` -> `2.5`
- `//` (divisão inteira): `5 // 2` -> `2`
- `%`  (resto): `5 % 2` -> `1`
- `**` (potência): `2 ** 3` -> `8`

Notas rápidas:

- `%`: o que sobra quando divide algo
- `//`: dividir itens igualmente (divisão inteira)
- `**`: potência (exponenciação)

## Operadores Relacionais

Usados para comparar valores:

- `==` (igual): `5 == 5`
- `!=` (diferente): `5 != 3`
- `>`  (maior que): `10 > 2`
- `<`  (menor que): `2 < 5`
- `>=` (maior ou igual): `7 >= 7`
- `<=` (menor ou igual): `3 <= 8`

Esses operadores funcionam como comparar preços ou tamanhos.

## Operadores Lógicos

Exemplo de uso com condicionais:

```py
if idade >= 18 and tem_carteira:
    print("Pode dirigir")
```

- `and`: todas as condições devem ser verdadeiras (duas chaves para abrir o cofre)
- `or`: basta uma das condições ser verdadeira
- `not`: inverte o estado lógico
