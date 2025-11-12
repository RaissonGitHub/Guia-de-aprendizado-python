# **Estruturas de repetição**
Se as estruturas condicionais (`if`, `else` e `elif`) são como os desvios no seu trajeto para o mercado, as estruturas de repetição, ou também conhecidos como Laços de Repetição, ou loops, são como aquele seu vizinho que lava o carro todo santo sábado: uma ação que se repete várias e várias vezes até que algo mude.

Na programação, muitas vezes precisamos executar o mesmo bloco de código inúmeras vezes. Imagina ter que escrever `print('Bem vindo!')` cem vezes. Iria dar um grande trabalho para escrever e o código ficaria gigantesco!

Os laços de repetição existem para nos salvar disso. Eles nos permitem dizer ao Python: "Execute este conjunto de comandos enquanto esta condição for verdadeira" (usando o `while`) ou "Execute este conjunto de comandos para cada item desta lista" (usando o `for`).

Então, a estrutura de repetição serve para executar uma quantidade determinada ou indeterminada de vezes o mesmo bloco de comandos. 

## **While**
O `while` é o mais simples e direto: ele executa um bloco de código enquanto uma determinada condição for verdadeira (`True`). Assim que a condição se torna falsa (`False`), o loop para. O `while` é considerado um laço de repetição não contado, pois necessita de uma condição para finalizar. O bloco de comandos será executado enquanto a condição for atendida.

Estrutura do comando `while`:
```py
while(condição):
	#Instruções a serem executadas 
#Instruções a serem executadas após o fim do loop
```

Pense no `while` como um bebê pedindo comida: "Enquanto eu estiver com fome, eu vou chorar!"

Em Python, precisamos ter certeza de que essa condição de parada (o bebê ficar satisfeito) vai acontecer em algum momento, senão o loop roda para sempre, travando seu programa (e isso se chama Loop Infinito... um pesadelo!).

Para que o `while` funcione como esperado, principalmente, para que ele não rode para sempre (olha o Loop Infinito aí!), você precisa de três passos:

1. **Inicialização**: Você deve começar definindo o seu parâmetro de controle (sua variável) antes do `while` começar. Pense nisso como dar o pontapé inicial na contagem!
2. **Teste**: O Python vai checar essa variável na condição do `while` a cada nova rodada. Se for `True`, ele entra; se for `False`, ele para.
3. **Manipulação (ou Alteração)**: Dentro do bloco de código do `while`, você precisa fazer alguma coisa que mude o valor da sua variável de controle. Isso garante que, em algum momento, o teste lá em cima se torne Falso e o loop possa terminar.

Vamos ver um exemplo simples, contando de 1 até 5:

```py
# Inicializamos a nossa variável de controle
contador = 1

# Enquanto o contador for menor ou igual a 5, execute:
while contador <= 5:
    print(f'Contagem atual: {contador}')
    contador = contador + 1	   # Sem esta linha, o loop seria infinito!

print('Fim da contagem!')
```

**Atenção Redobrada**: No `while`, você é o responsável por garantir que a condição mude para `False`. Sempre preste atenção na sua variável de controle (o contador no exemplo anterior) e certifique-se de que ela está sendo modificada dentro do loop.

## **For**
O `for` é geralmente usado quando você já sabe quantas vezes quer repetir, ou quando quer passar por todos os itens de uma sequência, um iterável (como uma lista, uma string ou um range de números).

Estrutura do comando `for`:

```py
for <variável> in <iterável>:
#Instruções a serem executadas
#Instruções a serem executadas após o fim do loop
```

Pense no `for` como um carteiro. Ele tem uma lista de casas para entregar cartas e, para cada casa na lista, ele executa a mesma ação: entregar a correspondência.

```py
lista_casas = ['casa azul', 'casa vermelha', 'casa rosa', 'casa verde']

for casa in lista_casas:
	print(f'Entreguei as cartas na {casa}'}

print('Todas as entregas feitas')
```

Também é muito utilizada a função range, uma função embutida na linguagem Python, nos laços de repetição `for`.

A função range possui três parâmetros: 
range(inicio, fim, passo)

Mas o parâmetro obrigatório é o valor de parada(fim). Logo, quando a função range estiver com um único parâmetro, refere-se ao valor de parada. 

Por padrão, o início é determinado como 0, e o passo é determinado como 1. Isso mudará apenas quando você alterar estes valores. Além de que o parâmetro de fim é exclusivo, logo, ele não é executado dentro da sequência.

**Exemplo:**

* ```range(10)``` Será uma sequência de 0 a 9.

* ```range(1,10,2)``` Será uma sequência: 1, 3, 5, 7, 9


## Comandos especiais dentro das estruturas de repetição

### **Break**
O `break` é como um botão de emergência. Quando o Python encontrar um `break` dentro de um `while` ou `for`, ele interrompe imediatamente o loop, não importa quantas repetições ainda faltariam, e segue para o próximo comando que está depois da estrutura de repetição.

**Uso Comum**: Sabe quando você está buscando algo em uma lista e, assim que encontra, não precisa mais procurar? É o momento do `break`!

**Exemplo**:
```py
lista_de_livros = ['A', 'B', 'O Livro Certo', 'D', 'E']

for livro in lista_de_livros:
if livro == 'O Livro Certo':
print('Achei o livro!')
break  # Interrompe o for AGORA!
print(f'Ainda procurando o livro: {livro}')

print('Próxima tarefa.') # Este é o próximo comando após a interrupção.
```

**Resumo**: o comando `break` força a saída do fluxo do programa de dentro do laço de repetição.

### **Continue**

O `continue` é como se falasse “pula e vai para o próximo”. Ao ser encontrado, ele interrompe apenas a repetição atual e faz o Python pular imediatamente para o próximo ciclo do loop.

**Uso Comum**: Imagine que você está processando uma lista de 100 usuários, mas percebe que o usuário número 50 está incompleto. Você não quer parar o processo todo, apenas ignorar o usuário incompleto e ir para o próximo.

**Exemplo**:
```py
for numero in range(1, 6): # Itera de 1 a 5
if numero == 3:
print('Número 3 detectado. Vou PULAR este e ir para o próximo.')
continue # Pula o 'print' abaixo e vai para o número 4
print(f'Estou processando o número: {numero}')
```

**A saída deste programa seria**:

```
Estou processando o número: 1
Estou processando o número: 2
Número 3 detectado. Vou PULAR este e ir para o próximo.
Estou processando o número: 4
Estou processando o número: 5
```

### **Else no `while` ou `for`**

Você pode usar um else com o `for` e com o `while`! Mas ele tem um significado um pouco diferente do que no if.

O bloco else em um loop será executado somente se o loop terminar normalmente, ou seja:
* **No `for`**: se ele percorreu todos os itens da sequência.
* **No `while`**: se a condição se tornou `False` (e não porque um `break` o interrompeu).

**Exemplo**:
```py
lista_de_presentes = ['Boneca', 'Carrinho', 'Bola']
item_buscado = 'Bola'
encontrado = False

for presente in lista_de_presentes:
if presente == item_buscado:
encontrado = True
# O else é executado se o for terminar sem ser interrompido por um `break`!
else:
if encontrado:
print(f'Sucesso! Encontrei o {item_buscado} e percorri toda a lista.')
else:
print('Ops! Não encontrei o item na lista.')
```
