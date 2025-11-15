# Dicionários
Em Python, o dicionário (dict) é uma estrutura de dados fundamental, ideal para armazenar coleções de dados de maneira organizada. Os dicionários usam nomes (chaves) para identificar e recuperar seus valores.

| Característica | Descrição | 
| --- | --- | 
| Representação | São delimitados por chaves ( { } ). | 
| Estrutura | Cada item é um par chave:valor. A chave é o "nome" que você usa para acessar o valor. |
| Tipo de Chaves | As chaves devem ser imutáveis, ou seja, podem ser do tipo strings, inteiros ou floats, mas não podem ser listas ou outros  |dicionários.
| Mutabilidade | Dicionários são mutáveis. Você pode adicionar, remover ou alterar pares chave:valor a qualquer momento. |
| Organização | Dicionários não possuem uma noção fixa de posições (como 0, 1, 2,..). |


## Criando um Dicionário
Você cria um dicionário listando pares de chave e valor separados por dois pontos (:) dentro das chaves:
```py
# Sintaxe: nome_do_dicionario = {chave: valor}
contatos = {'Yan': '1234-5678', 'Ana': '9999-0000'}
```

## Acessando Itens
Para obter um valor, você usa o nome da chave dentro de colchetes:
```py
contatos = {'Ana': '9999-0000'}
# Acessa o valor associado à chave 'Ana'
print(contatos['Ana'])
# Saída: 9999-0000
```

## Inserindo ou Alterando Valores
Se a chave não existe, um novo par é inserido. Se a chave já existe, o valor é alterado (sobrescrito).
```py
contatos = {'Ana': '9999-0000'}
# Inserindo um novo contato
contatos['João'] = '8887-7778'
# contatos agora é: {'Ana': '9999-0000', 'João': '8887-7778'}
```

## Removendo Valores:
Use a palavra-chave del seguida do nome do dicionário e a chave que deseja remover:
```py
contatos = {'Yan': '1234-5678', 'Ana': '9999-0000'}
# Remove o par chave:valor com a chave 'Yan'
del contatos['Yan']
# contatos agora é: {'Ana': '9999-0000'}
```

## Verificando a Existência de Itens
Você pode usar o operador in para verificar a presença de uma chave ou valor.

* Verificar a Existência de uma Chave:

```py
alunos = {'Amelia': 7.8, 'Bruno': 7.0}
# Verifica se a chave 'Mariana' existe no dicionário alunos
print('Mariana' in alunos)
# Saída: False
```
* Verificar a Existência de um Valor:

```py
turmaB = {'Amelia': 7.8, 'Bruno': 7.0}
# Verifica se o valor 7.8 existe entre os valores do dicionário turmaB
print(7.8 in turmaB.values())
# Saída: True
```

## Métodos para os dicionários

| Método |   Descrição   | Exemplo |   Exemplo de saída | 
| --- | --- | --- | --- |  
| `keys()`  | Retorna uma visualização de todas as chaves do dicionário.  | `turmaB.keys()`  | `{'Amelia', 'Bruno', 'Lucia', 'Mirela'}` | 
| `values()`| Retorna uma visualização de todos os valores do dicionário.| ` turmaB.values()`| ` {7.8, 7.0, 0.7, 6.4}` | 
| `items()` | Retorna uma visualização de todos os pares (chave, valor) como tuplas. | `turmaB.items()` | `{('Amelia', 7.8), ('Bruno', 7.0)}` |


**Exemplos de uso**:

**`keys()`**
```py
print("Lista de Alunos:")
for nome in turmaB.keys():
    print(nome)

# Saída:
# Lista de Alunos:
# Amelia
# Bruno
# Lucia
# Mirela
```

**`values()`**
```py
# Calculando a média das notas
notas = turmaB.values()
media = sum(notas) / len(notas)

print(f"A média da turma é: {media:.2f}")

# Saída (aprox.):
# A média da turma é: 5.48
```

**`items()`**
```py
# Imprimindo a chave e o valor de forma formatada
print("Notas Detalhadas:")
for aluno, nota in turmaB.items():
    print(f"O aluno {aluno} tirou a nota {nota}")

# Saída:
# Notas Detalhadas:
# O aluno Amelia tirou a nota 7.8
# O aluno Bruno tirou a nota 7.0
# O aluno Lucia tirou a nota 0.7
# O aluno Mirela tirou a nota 6.4
```
