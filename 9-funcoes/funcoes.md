# **Introdução a funções e como declará-las**
Você já deve ter encontrado o termo "funções" ao estudar programação e talvez tenha se perguntado o que isso significava. De forma simplificada, uma função é um segmento de código que pode ser reaproveitado e só é executado quando invocado.

Para elucidar essa ideia, considere sua máquina de lavar. Se você tivesse que especificar cada etapa que ela deveria seguir para lavar suas roupas (encher com água, adicionar sabão, centrifugar, etc.), seria tedioso e repetitivo, certo? É nesse ponto que as funções se tornam úteis. Em vez de escrever essas etapas várias vezes, você pode defini-las uma única vez e simplesmente reutilizá-las. É exatamente isso que a máquina de lavar faz quando você a liga: ela executa funções predefinidas para lavar suas roupas, sem que você precise fornecer instruções detalhadas a cada uso.

Retornando ao código, em Python, declaramos uma função utilizando a palavra-chave `def`. Para nomear a função, você atribui um nome a ela, seguido por dois parênteses () (que serão explicados posteriormente) e dois pontos :.

Aqui um exemplo:

```py
def minha_funcao():
       print("Olá, mundo!")
```

Agora que você viu como declarar uma função, a próxima etapa é aprender como executá-la. Uma função só é útil se `for` 'chamada', se você apenas criar e nunca chamá-la, sua função acaba nunca executando, nesse caso nós não iríamos conseguir  imprimir o nosso querido “Olá, mundo!”. Para chamar uma função em Python, basta escrever o nome dela seguido por parênteses, dessa forma:

```py
def minha_funcao():
      print("Olá, mundo!")

minha_funcao()
```

## **Argumentos posicionais e nomeados**

Interessante, não é? Mas podemos ir além. E se, em vez de um simples "Olá, mundo!", eu quisesse cumprimentar pessoas diferentes? Seria preciso criar uma função nova para cada nome? Não! É aí que entram os **parâmetros de funções**.  Parâmetros são valores que uma função pode receber, são espaços reservados para as informações que ela precisa para realizar suas tarefas. Ao chamar uma função, você passa os **argumentos**, que são os valores de verdade a serem usados. No próximo exemplo vamos criar uma função saudacao que recebe um nome como argumento e na exucução imprime a saudação com o nome recebido.

```py
def saudacao(nome):
      print(f"Olá, {nome}!")

saudacao(“Fulano” )
```

Podemos então passar argumentos para as funções. Mas e se quisermos passar mais de um argumento? Não se preocupe, é possível passar quantos argumentos forem necessários, basta separá-los por vírgula. Vamos ver um exemplo de uma função que recebe dois números e imprime a soma deles.

```py
def soma(a, b):
    print(a+b)

soma(25,30)
```

No exemplo acima, passamos os argumentos 25 e 30 para a função soma. Esses são **argumentos posicionais**, o que significa que a ordem em que você os passa é importante. O primeiro valor (25) é atribuído ao primeiro parâmetro (a), e o segundo valor (30) ao segundo parâmetro (b).

Além dos argumentos posicionais, o Python também permite o uso de **argumentos nomeados**. Com eles, você especifica o nome do parâmetro ao qual o valor está sendo atribuído. Isso torna o código mais legível e flexível, especialmente quando a função tem muitos parâmetros ou se a ordem não é tão intuitiva.

Veja o exemplo da função soma novamente, mas agora com argumentos nomeados:

```py
def soma(a, b):
    print(a + b)

soma(b=30, a=25)
```

Nesse caso, a ordem em que a e b são passados não importa, pois estamos explicitamente dizendo a qual parâmetro cada valor pertence. O resultado será o mesmo.

Agora que você já sabe da existência deles, pode estar se perguntando: "Tá, mas quando eu uso um e quando eu uso o outro?". É uma ótima pergunta! A resposta é que depende um pouco do contexto e de quão legível e claro você quer que seu código fique.

### **Argumentos Posicionais: Para que servem?**

Pense nos argumentos posicionais como a forma mais "direta" de passar informações. Eles são ótimos quando:

* **A função tem poucos parâmetros e a ordem é super clara**: Se você tem uma função dividir(num1, num2) e sabe que num1 é sempre o dividendo e num2 é o divisor, não há mistério. dividir(10, 2) é fácil de entender.
* **Você está usando uma função muito comum e conhecida**: Para funções built-in do Python ou aquelas que todo mundo no seu time já sabe como funcionam, a ordem posicional é suficiente.
* **A concisão é importante**: Se você quer um código mais compacto e rápido de escrever, e a clareza não será prejudicada, os posicionais são seus amigos.

### Argumentos Nomeados: Quando brilham?
Já os argumentos nomeados são como ter etiquetas nas suas informações. Eles são a melhor escolha quando:

* **A função tem muitos parâmetros**: Imagine uma função com 5, 6, 7 parâmetros. Tentar lembrar a ordem de cada um é pode ser complicado! Com argumentos nomeados, você não precisa se preocupar com isso, é só nomear e pronto.
* **A ordem dos parâmetros não é óbvia ou intuitiva**: Às vezes, a função pode ter parâmetros com nomes genéricos ou que não têm uma ordem "natural". Usar nomes deixa claro o que cada valor representa.
* **Você quer melhorar a legibilidade do código**: Quando outra pessoa (ou você mesmo no futuro!) `for` ler seu código, os argumentos nomeados tornam a intenção da função muito mais clara, sem precisar ficar consultando a definição da função.
* **A função tem valores padrão**: Se você só quer passar alguns argumentos e deixar outros com os valores padrão, os argumentos nomeados te permitem especificar apenas os que você quer mudar, em qualquer ordem. (Não se preocupe, veremos valores padrão em breve)

## **Retorno de funções**

Certo, mas talvez você tenha reparado que essas funções até agora não "retornaram" nada de verdade, não é mesmo? Elas apenas imprimiram algo na tela. Mas e se quiséssemos que uma função nos desse um valor de volta para que pudéssemos usá-lo em outro lugar do nosso código? É aí que entra o **retorno de valores**! Pense nisso como uma função te entregando um presente depois de fazer o trabalho dela.

Em Python, usamos a palavra-chave `return` para que uma função possa enviar um valor de volta. Quando o Python encontra `return` dentro de uma função, ele imediatamente sai da função e entrega o valor especificado de volta para o local onde a função foi chamada.
Vamos pegar nosso exemplo da função soma novamente. Em vez de apenas imprimir a soma, vamos fazer com que ela **retorne** o resultado:
```py
def soma(a, b):
    return a + b
```
Agora, quando chamamos ```soma(25, 30)```, a função não imprime nada diretamente. Em vez disso, ela nos **devolve** o valor 55. Podemos então armazenar esse valor em uma variável ou usá-lo em outras operações: 
```py
resultado_da_soma = soma(25, 30)
print(resultado_da_soma)  # Isso imprimirá 55
```

Percebe a diferença? Com `print()`, a função apenas exibe algo na tela; com `return`, ela produz um valor que pode ser usado. Isso é super importante para construir programas mais complexos, onde o resultado de uma função precisa ser a entrada para outra.
Múltiplos Retornos

Uma função pode ter múltiplos `return` statements, mas apenas um será executado por chamada. O `return` encerra a execução da função. Por exemplo:

```py
def verificar_numero(numero):

    if numero > 0:

        return "Positivo"

    elif numero < 0:

        return "Negativo"

    else:

        return "Zero"

print(verificar_numero(10))   # Saída: Positivo

print(verificar_numero(-5))   # Saída: Negativo

print(verificar_numero(0))    # Saída: Zero
```
Nesse exemplo, a função retorna uma string diferente dependendo da condição que é satisfeita.

## **Retornando Múltiplos Valores (Tuplas)**

O Python tem uma característica muito legal: uma função pode, na verdade, retornar múltiplos valores de uma vez! Ele faz isso "empacotando" os valores em uma tupla (uma coleção ordenada e imutável de itens).

```py
def operacoes_basicas(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    return soma, subtracao, multiplicacao, divisao
resultados = operacoes_basicas(10, 2)
print(resultados)

# Saída: (12, 8, 20, 5.0)
# Você também pode desempacotar os valores diretamente em variáveis:
s, sub, m, d = operacoes_basicas(10, 2)

print(f"Soma: {s}, Subtração: {sub}, Multiplicação: {m}, Divisão: {d}")

# Saída: Soma: 12, Subtração: 8, Multiplicação: 20, Divisão: 5.0
```

Isso é extremamente útil quando você quer que uma única função calcule e forneça vários dados relacionados.

Com o conceito de retorno de valores, suas funções se tornam muito mais poderosas e versáteis, permitindo que você construa lógicas complexas e modulares em seus programas.

## **Valores Padrão em Argumentos de Funções**
Até agora, vimos que quando definimos parâmetros para uma função, somos obrigados a passar os argumentos correspondentes quando chamamos a função. Mas e se quiséssemos que um parâmetro tivesse um valor "predefinido" caso o usuário não forneça um argumento para ele? É aí que entram os **valores padrão**.

Argumentos com valores padrão são aqueles que recebem um valor inicial na própria definição da função. Isso significa que você pode chamar a função sem fornecer um argumento para esse parâmetro específico, e ele automaticamente usará o valor padrão. Se você fornecer um valor, ele substituirá o padrão.

Veja o exemplo da nossa função `saudacao`, mas agora com um valor padrão para o nome:
```py
def saudacao(nome="Mundo"):

    print(f"Olá, {nome}!")

saudacao()           # Saída: Olá, Mundo!
saudacao("Python")   # Saída: Olá, Python!
```

No primeiro caso, não passamos nenhum argumento para saudacao(), então a função utilizou o valor padrão "Mundo" para o parâmetro nome. No segundo caso, passamos "Python", que sobrescreveu o valor padrão.

### Por que usar valores padrão?

* **Flexibilidade**: Permite que a função seja chamada de maneiras mais simples quando a maioria dos casos de uso envolve o valor padrão, mas ainda oferece a opção de personalização.
* **Redução** de código: Evita a necessidade de criar múltiplas funções ou usar lógica condicional complexa para lidar com a ausência de argumentos.
* **Legibilidade**: Deixa claro quais parâmetros são opcionais e qual é o seu comportamento padrão.

### Regras importantes:

Ao definir parâmetros com valores padrão, há uma regra de sintaxe crucial no Python: **todos os parâmetros com valores padrão devem vir DEPOIS dos parâmetros sem valores padrão.** 
```py
# Correto:
def exemplo_correto(param1, param_padrao="default"):
    print(f"Param1: {param1}, Param_padrao: {param_padrao}")

exemplo_correto("obrigatório")
exemplo_correto("obrigatório", "personalizado")
```
```py
# Incorreto:
def exemplo_incorreto(param_padrao="default", param1):
    pass

# Isso resultaria em um SyntaxError: non-default argument follows default argument
```
Essa regra garante que o interpretador Python saiba qual argumento corresponde a qual parâmetro quando a função é chamada, especialmente em chamadas com argumentos posicionais.

## **\`*args` e \*\*kwargs**

Para esse tópico vamos começar com uma analogia para uma experiência que temos no nosso dia a dia. Imagine que você está preparando uma receita. Algumas receitas são muito específicas sobre a quantidade de cada ingrediente, como "adicione 2 xícaras de farinha e 1 xícara de açúcar". Outras receitas são mais flexíveis, permitindo que você adicione quantos ingredientes quiser, como "adicione legumes a gosto".

Pense na receita de um café. Para um café simples, você pode precisar de "2 colheres de pó de café, 1 xícara de água e açúcar a gosto". Aqui, o pó de café e a água têm quantidades fixas, mas o açúcar é flexível. E se você quiser fazer um café gourmet com diferentes tipos de xaropes, cremes e especiarias? A receita pode precisar de uma forma de adicionar "uma pitada de canela", "um fio de caramelo" ou "uma dose de chantilly", sem ter que especificar cada um deles de antemão.

Em programação, as funções são como essas receitas. Às vezes, você sabe exatamente quantos argumentos (ingredientes) uma função precisa. Outras vezes, você quer que uma função seja capaz de receber um número variável de argumentos. É aí que `*args` e `**kwargs` entram em jogo.

`*args` e `**kwargs` permitem que você defina funções que podem receber um número arbitrário de argumentos. Eles são especialmente úteis quando você não sabe quantos argumentos serão passados para a sua função, ou quando você quer tornar sua função mais flexível.

Vamos explorar cada um deles em detalhes.

### O que é `*args`?
O `*args` (o asterisco é fundamental!) permite que uma função aceite um número variável de argumentos posicionais. A palavra "args" é uma convenção (abreviação de "arguments"), mas você poderia usar qualquer outro nome depois do asterisco, como `*numeros` ou `*itens`. O Python empacotará todos esses argumentos em uma **tupla** dentro da função.

**Exemplo Prático**:

Imagine que você quer uma função que some vários números, mas nem sempre sabe quantos números serão.
```py
def somar_todos(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(somar_todos(1, 2))              # Saída: 3
print(somar_todos(1, 2, 3, 4, 5))     # Saída: 15
print(somar_todos(10, 20, 30, 40))    # Saída: 100
```
Neste exemplo:

* `*numeros` captura todos os argumentos posicionais passados para a função.
* Dentro da função, numeros é uma tupla (1, 2), (1, 2, 3, 4, 5) ou (10, 20, 30, 40), dependendo da chamada.
* A função itera sobre essa tupla para calcular a soma.

### O que é `**kwargs`?
Assim como `*args`, o `**kwargs` (dois asteriscos são fundamentais!) permite que uma função aceite um número variável de argumentos nomeados (keyword arguments). "kwargs" é uma convenção (abreviação de "keyword arguments"), mas novamente, você poderia usar qualquer outro nome depois dos dois asteriscos, como `**opcoes` ou `**dados`. O Python empacotará esses argumentos nomeados em um **dicionário** dentro da função.

**Exemplo Prático:**

Considere uma função que cria um perfil de usuário, mas nem todos os detalhes são obrigatórios ou fixos.
```py
def criar_perfil(nome, **detalhes):
    print(f"Criando perfil para: {nome}")
    for chave, valor in detalhes.items():
        print(f"{chave.capitalize()}: {valor}")

criar_perfil("Alice", idade=30, cidade="São Paulo")

# Saída:
    # Criando perfil para: Alice
    # Idade: 30
    # Cidade: São Paulo

print("-" * 20)
criar_perfil("Bob", profissao="Engenheiro", empresa="Tech Corp", status="Ativo")

# Saída:
    # Criando perfil para: Bob
    # Profissao: Engenheiro
    # Empresa: Tech Corp
    # Status: Ativo
```
Neste exemplo:

* `**detalhes` captura todos os argumentos nomeados (como idade=30, cidade="São Paulo", profissao="Engenheiro", etc.).
* Dentro da função, detalhes é um dicionário que mapeia os nomes dos parâmetros para seus valores.
* A função itera sobre os itens desse dicionário para imprimir os detalhes.
  
### Ordem dos Argumentos
Se você `for` usar argumentos posicionais normais, `*args` e `**kwargs` juntos em uma única função, a ordem em que eles devem aparecer na definição da função é crucial:
1. Parâmetros posicionais normais
2. Parâmetros com valores padrão
3. `*args`
4. `**kwargs`

**Exemplo**:
```py
def exemplo_completo(param_obrigatorio, param_padrao="padrao", *extras, **opcoes_adicionais):
    print(f"Obrigatório: {param_obrigatorio}")
    print(f"Padrão: {param_padrao}")
    print(f"Argumentos Extras (*extras): {extras}")
    print(f"Opções Adicionais (**opcoes_adicionais): {opcoes_adicionais}")

print("--- Chamada 1 ---")
exemplo_completo("valor_obrigatório")

# Saída:
    # Obrigatório: valor_obrigatório
    # Padrão: padrao
    # Argumentos Extras (*extras): ()
# Opções Adicionais (**opcoes_adicionais): {}

print("\n--- Chamada 2 ---")
exemplo_completo("valor_obrigatório", "novo_padrao", 1, 2, 3, chave='valor', teste=True)

# Saída:
    # Obrigatório: valor_obrigatório
    # Padrão: novo_padrao
    # Argumentos Extras (*extras): (1, 2, 3)
    # Opções Adicionais (**opcoes_adicionais): {'chave': 'valor', 'teste': True}
```

**Casos de Uso Comuns**:

* `*args`:
  - Quando você precisa de uma função que aceite um número indefinido de entradas (ex: somar, concatenar, média).
  - Ao criar funções "wrapper" que repassam argumentos para outras funções.
* `**kwargs`:
  - Para funções que configuram objetos ou aceitam diversas opções configuráveis (ex: funções de plotagem, construtores de classe).
  - Ao criar funções flexíveis onde você não quer predefinir todos os parâmetros possíveis.

Dominar `*args` e `**kwargs` é um passo importante para escrever código Python mais flexível, robusto e idiomático. Eles são ferramentas poderosas para lidar com a variabilidade na forma como as funções podem ser chamadas.

## **Escopo**

Vamos pensar no escopo de funções como o "alcance" ou a "visibilidade" de certas coisas em diferentes lugares. Para entender melhor, imagine a sua casa e a casa dos seus vizinhos.

Dentro da sua casa, você tem acesso a certas coisas: sua geladeira, seu sofá, seus talheres. Essas coisas são "suas", e ninguém de fora da sua casa (seus vizinhos, por exemplo) tem acesso direto a elas. Se o seu vizinho quiser um copo d'água, ele não pode simplesmente entrar na sua casa e pegar na sua geladeira, certo? Ele precisa pedir a você, e você (a função) pode entregar a água (o valor).

Da mesma forma, as coisas que estão dentro do seu quarto (sua cama, suas roupas no armário) são ainda mais "privadas". Seu colega de casa pode ter acesso à geladeira na cozinha, mas ele não vai simplesmente entrar no seu quarto e pegar suas roupas sem permissão. O quarto tem um escopo mais restrito que a casa.

Agora, e o que está lá fora, na rua? A rua, o parque público, o céu. Isso é algo que tanto você quanto seus vizinhos podem ver e acessar. Não pertence a ninguém em particular, mas está disponível para todos.

Em Python, o conceito de escopo funciona de maneira bem parecida.

* **Coisas dentro da sua função (seu quarto)**: Variáveis criadas dentro de uma função são como os objetos dentro do seu quarto. Elas são locais para aquela função e só podem ser acessadas lá dentro. Nenhuma outra parte do seu código pode "ver" ou usar essas variáveis diretamente.
  
* **Coisas na sua casa (mas fora do quarto, como a geladeira)**: Se você tem uma variável definida fora de qualquer função, mas dentro de um módulo (um arquivo `.py`), ela é como a geladeira na cozinha. Todas as funções dentro daquele módulo podem "ver" e usar essa variável.
  
* **Coisas na rua (global)**: Existem algumas coisas que são "globais", ou seja, acessíveis de qualquer lugar do seu programa, como funções `print()` ou `len()`. Elas são como a rua ou o céu, disponíveis para todos usarem.

Essa separação de escopos é fundamental para evitar que uma parte do seu código altere acidentalmente dados em outra parte, e para manter as funções independentes e reutilizáveis.

Agora, vamos levar essa analogia para o código Python:

### Escopo Local (Seu Quarto)
Quando você cria uma variável dentro de uma função, ela existe apenas enquanto a função está sendo executada. Assim que a função termina, a variável "desaparece" (é removida da memória).
```py
def minha_funcao():
    # 'x' é uma variável local, só existe dentro de minha_funcao
    x = 10 
    print(f"Dentro da função, x é: {x}")

minha_funcao()

# Tentar acessar 'x' aqui fora causaria um erro (NameError), 
# porque 'x' só existe dentro de minha_funcao.
# print(x) 
```
Nesse exemplo, a variável `x` é como seus objetos pessoais dentro do seu quarto. Ninguém de fora do quarto (`minha_funcao`) pode vê-los.

### Escopo Envolvente (Enclosing ou Nonlocal) - Quartos Dentro de uma Casa
Imagine que dentro do seu quarto, você tem uma caixa de brinquedos. E dentro dessa caixa, você guarda um boneco. O boneco está dentro da caixa, que está dentro do seu quarto.

Em Python, isso acontece quando você tem uma função definida dentro de outra função. A função interna pode acessar variáveis da função externa (envolvente).
```py
def minha_casa():
    cor_parede = "branca" # Variável da casa (função externa)
    def meu_quarto():
        # meu_quarto pode ver cor_parede porque ela está na casa
        print(f"A cor da parede do quarto é: {cor_parede}") 
        # cor_cobertor é local ao quarto
        cor_cobertor = "azul" 
        print(f"A cor do cobertor é: {cor_cobertor}")

    meu_quarto()
    # A casa não consegue ver a cor do cobertor, pois ela está dentro do quarto
    # print(cor_cobertor) 

minha_casa()
```

Nesse caso, `cor_parede` é como a geladeira na cozinha da casa. O quarto (`meu_quarto`) pode ver e usar a geladeira (`cor_parede`), mas o cobertor (`cor_cobertor`) é exclusivo do quarto e a "casa" não sabe qual a cor dele.

Para modificar uma variável do escopo envolvente dentro de uma função aninhada, usamos a palavra-chave `nonlocal`:
```py
def balcao_da_lanchonete():
    estoque_cafe = 10 # Estoque inicial do balcão
    def vender_cafe():
        nonlocal estoque_cafe # Declara que estamos usando a variável do escopo envolvente
        if estoque_cafe > 0:
            estoque_cafe -= 1
            print(f"Café vendido! Restam {estoque_cafe} cafés.")
        else:
            print("Acabou o café!")

    vender_cafe()
    vender_cafe()
    print(f"Estoque final no balcão: {estoque_cafe}")

balcao_da_lanchonete()
```

Aqui, `estoque_cafe` é como a quantidade de grãos de café que o barista (`vender_cafe`) pega do estoque geral do balcão (`balcao_da_lanchonete`). Se ele não disser `nonlocal`, ele pensaria que está pegando de um estoque próprio (local), não do estoque do balcão.

## Escopo Global (A Rua)

Variáveis definidas no nível principal do seu script (fora de qualquer função) são consideradas globais. Elas podem ser acessadas de qualquer lugar no seu código, incluindo dentro de funções.
```py
velocidade_maxima_rodovia = 110 # Variável global (a rua)

def meu_carro():
    print(f"Meu carro está na rodovia. A velocidade máxima permitida é: {velocidade_maxima_rodovia} km/h")

def bicicleta():
    print(f"Minha bicicleta não pode ir tão rápido, mas a rodovia ainda tem uma velocidade máxima de: {velocidade_maxima_rodovia} km/h")

meu_carro()
bicicleta()
```

Aqui, `velocidade_maxima_rodovia` é como a sinalização de velocidade na rodovia. Tanto o carro (`meu_carro`) quanto a bicicleta (`bicicleta`) podem "ver" e saber qual é a velocidade máxima.

Para modificar uma variável global dentro de uma função, você precisa explicitamente usar a palavra-chave `global`:
```py
saldo_conta_bancaria = 1000 # Saldo global na agência bancária

def sacar_dinheiro(valor):
    global saldo_conta_bancaria # Avisa que estamos mexendo no saldo global
    if saldo_conta_bancaria >= valor:
        saldo_conta_bancaria -= valor
        print(f"Saque de {valor} realizado. Novo saldo: {saldo_conta_bancaria}")
    else:
        print("Saldo insuficiente!")

print(f"Saldo inicial: {saldo_conta_bancaria}")
sacar_dinheiro(200)
sacar_dinheiro(900) # Isso não vai funcionar, saldo ficou 800
print(f"Saldo final: {saldo_conta_bancaria}")
```

Sem global, o Python criaria uma nova variável `saldo_conta_bancaria` local dentro da função `sacar_dinheiro`, sem afetar o saldo real da conta. Usar `global` é como ter uma permissão especial para mexer diretamente no cofre principal do banco.

## Escopo Built-in (O Universo)

Existem funções e tipos que vêm "embutidos" no Python e estão sempre disponíveis, como `print(), len(), str(), list()`, etc. Eles são como as leis da física no universo – estão sempre lá e podem ser usados por qualquer um, a qualquer momento, em qualquer lugar.

Esses quatro tipos de escopo (**Local, Envolvente, Global e Built-in**, ou **LEGB** na sigla em inglês) definem a ordem em que o Python procura por nomes (variáveis, funções, etc.) quando você os usa em seu código. Ele sempre começa no escopo mais restrito (Local) e vai expandindo até o mais amplo (Built-in).

Entender o escopo é crucial para escrever código limpo, sem bugs inesperados, e para organizar suas informações de forma eficiente em seus programas!

## **Funções Anônimas (Funções Lambda)**

Prepare-se para conhecer as funções "express", aquelas que são rapidinhas, sem muita formalidade e perfeitas para um uso pontual: as **funções anônimas**, também conhecidas como **funções `lambda`**.

Pense nelas como um bilhetinho pós-it que você cola na geladeira para uma tarefa rápida. Você não vai escrever uma carta formal, com cabeçalho, saudação e assinatura, para pedir para alguém comprar pão, certo? Um "Comprar pão, por favor!" é o suficiente. Funções `lambda` são assim: ideais para tarefas curtas e que não precisam ser reutilizadas em muitos lugares.

**Por que "Anônimas"?** <br />
Elas são chamadas de anônimas porque não recebem um `def` e um nome formal, como as funções que vimos até agora. Elas são definidas no momento em que são necessárias e geralmente são usadas imediatamente.

**Como elas são no Python?** <br />
No Python, uma função anônima é criada usando a palavra-chave `lambda`. A sintaxe é super concisa:

`lambda argumentos: expressão`

É como dizer: "ei, aqui está uma função que recebe estes argumentos e faz o que está na expressão". O resultado da expressão é o que a função retorna automaticamente.

**Exemplo Prático: Um "bilhetinho" de soma**

Se você quisesse uma função simples para somar dois números, sem ter que dar um nome a ela, faria assim:
```py
somar = lambda a, b: a + b
print(somar(5, 3))  # Saída: 8
```

Nesse caso:

* `lambda` a, b: define que a função recebe dois argumentos, a e b.
* : a + b é a expressão que será executada, e seu resultado (a + b) será retornado.

A variável `somar` está "apontando" para essa função `lambda`, mas ela não tem um nome formal de função.

## Quando as funções `lambda` brilham?

Elas são particularmente úteis em situações onde você precisa de uma pequena função para uma única operação, muitas vezes como argumento para outra função de ordem superior (funções que aceitam outras funções como argumentos, como `map()`, `filter()` ou `sorted()`).

### Exemplo com `sorted()`:

Imagine que você tem uma lista de tuplas, onde cada tupla representa uma pessoa ((nome, idade)), e você quer ordenar essa lista pela idade: 

```py
pessoas = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# Ordenar pela idade (segundo elemento da tupla)
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[1])
print(pessoas_ordenadas)
# Saída: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
```

Aqui, `lambda` pessoa: `pessoa[1]` é o nosso "bilhetinho". Ele diz para a função `sorted()`: "Para cada pessoa nesta lista, use o segundo item dela (`pessoa[1]`, que é a idade) como chave para a ordenação". É uma maneira elegante e compacta de definir essa lógica de ordenação no local.

### Exemplo com `map()`:

Imagine que você tem uma lista de números e quer obter uma nova lista com o quadrado de cada número:
```py
numeros = [1, 2, 3, 4, 5]
# Usar map() para aplicar uma função a cada elemento
quadrados = list(map(lambda x: x*x, numeros))
print(quadrados)
# Saída: [1, 4, 9, 16, 25]
```

Aqui, `lambda x: x*x` é a função que `map()` aplica a cada elemento da lista numeros. Ela retorna uma nova lista com o resultado da aplicação dessa função a cada item original.

### Exemplo com `filter()`:

Imagine que você tem uma lista de idades e quer filtrar apenas as idades maiores ou iguais a 18:
```py
idades = [15, 22, 17, 30, 18, 12]

# Usar filter() para selecionar elementos que satisfazem uma condição
maiores_de_idade = list(filter(lambda idade: idade >= 18, idades))

print(maiores_de_idade)
# Saída: [22, 30, 18]
```

Neste caso, `lambda idade: idade >= 18` é a função de filtro. `filter()` percorre a lista idades e, para cada idade, verifica se a condição é verdadeira. Se `for`, o elemento é incluído na nova lista.

Limitações:

Funções `lambda` são para coisas simples. Elas são restritas a uma única expressão. Se você precisa de lógica mais complexa, com múltiplas linhas de código, condicionais (`if/else`) ou loops, então uma função `def` tradicional é a escolha certa.

Em resumo, as funções `lambda` são a ferramenta perfeita para aquela "tarefinha rápida" que surge, onde você não precisa de todo o aparato de uma função nomeada. Elas tornam seu código mais conciso e, em muitos casos, mais legível para operações pontuais!

## **Funções Internas e Closures**

Imagine que você tem uma barraca de limonada no seu quintal. Você mesmo faz a limonada (sua função principal), mas para isso, você tem uma "receita secreta" de como cortar os limões e espremer o suco. Essa "receita de corte e espreme" é uma função que só faz sentido dentro da sua função de fazer limonada, certo? Ela não é algo que você vai sair ensinando para todo mundo na rua. Ela é uma função interna.

Em Python, uma função interna (ou aninhada) é exatamente isso: uma função definida dentro de outra função. Ela só existe e pode ser acessada de dentro da função "pai".

Exemplo:
```py
def fazer_limonada(quantidade_limoes):
    acucar = 50 # Variável local da função fazer_limonada

    def espremer_limoes(num_limoes):
        # Esta é uma função interna, só existe aqui dentro
        suco = num_limoes * 10 # Cada limão rende 10ml de suco
        print(f"Espremendo {num_limoes} limões... Produziu {suco}ml de suco.")
        return suco

    suco_total = espremer_limoes(quantidade_limoes)
    print(f"Misturando {suco_total}ml de suco com {acucar}g de açúcar e água.")
    return f"Sua limonada está pronta com {suco_total}ml de suco!"

print(fazer_limonada(3))
# Saída:
    # Espremendo 3 limões... Produziu 30ml de suco.
    # Misturando 30ml de suco com 50g de açúcar e água.
    # Sua limonada está pronta com 30ml de suco!
```

Nesse caso, `espremer_limoes` é uma função interna de `fazer_limonada`. Ela pode acessar a variável acucar (do escopo envolvente), mas ninguém fora de `fazer_limonada` consegue chamar `espremer_limoes` diretamente.
O Poder dos Closures (A Barraca de Limonada Ambulante)
Agora, e se você quisesse que sua "receita de corte e espreme" (a função interna) pudesse ser levada para outro lugar, mesmo depois que você fechou sua barraca de limonada (a função externa terminou)? Isso é um closure!

Um closure ocorre quando uma função interna "se lembra" e continua tendo acesso a variáveis do escopo da função externa (onde ela foi criada), mesmo depois que a função externa já terminou sua execução. É como se a função interna levasse consigo uma "mochila" com as variáveis do ambiente onde ela nasceu.

Exemplo Prático:

Vamos criar uma função que "cria" outras funções de saudação personalizadas:
```py
def criar_saudador(saudacao):
    # 'saudacao' é uma variável do escopo envolvente
    def saudar(nome):
        # 'saudar' é a função interna (o closure)
        # Ela "se lembra" da 'saudacao' mesmo depois que criar_saudador termina
        return f"{saudacao}, {nome}!"

    return saudar # Retornamos a função interna, não o resultado dela

# Criamos diferentes funções de saudação baseadas na saudação inicial
bom_dia = criar_saudador("Bom dia")
boa_noite = criar_saudador("Boa noite")

print(bom_dia("Alice"))   # Saída: Bom dia, Alice!
print(boa_noite("Bob"))   # Saída: Boa noite, Bob!
```

Observe que criar_saudador terminou sua execução, mas as funções `bom_dia` e `boa_noite` (que são as funções internas retornadas) ainda "sabem" qual era a saudacao ("Bom dia" ou "Boa noite") definida no momento em que foram criadas. Elas "fecham" sobre essa variável, por isso o nome closure.

### Quando isso é útil?

* **Fábricas de Funções**: Quando você precisa gerar funções com comportamentos ligeiramente diferentes, baseados em alguma configuração inicial.

* **Encapsulamento de Estado**: Para criar funções que mantêm um certo estado entre chamadas, sem que esse estado seja global.

* **Decoradores**: São amplamente usados na implementação de decoradores (o próximo tópico!).

As funções internas e os closures são conceitos poderosos que abrem portas para padrões de programação mais avançados e flexíveis em Python, permitindo que você crie códigos mais modulares e elegantes!

## **Decoradores**

Sabe quando você tem uma receita de bolo pronta e ela já é boa, mas você quer dar um "toque especial" sem ter que reescrever toda a receita? Tipo, adicionar uma cobertura de chocolate, ou umas raspas de limão?

Em Python, os decoradores fazem exatamente isso com as suas funções! Eles são como "envoltórios" que permitem adicionar funcionalidades extras a uma função existente, sem modificar o código original dela. É uma forma super elegante e poderosa de reutilizar código e manter suas funções focadas no que elas realmente devem fazer.

Imagine a seguinte situação:

Você tem uma função simples que calcula o tempo de preparo de um prato:
```py
def calcular_tempo_preparo(prato):
    
    # Lógica para calcular o tempo
    if prato == "macarrao":
        return 10
    elif prato == "lasanha":
        return 45
    else:
        return 20
```

Agora, você decide que quer que toda vez que essa função `for` chamada, ela também imprima uma mensagem "Iniciando cálculo..." antes e "Cálculo finalizado!" depois, e talvez até o tempo que levou para o cálculo acontecer.

Você poderia ir lá e adicionar prints em todas as suas funções, mas e se você tiver dezenas de funções? Isso viraria uma bagunça!

É aí que o decorador entra em cena, como um mágico!

Como funciona a mágica (o `@`):

Um decorador é, na sua essência, uma função que recebe outra função como argumento, adiciona alguma funcionalidade a ela e retorna uma nova função (ou a função original modificada).

A sintaxe mais comum e "bonitinha" para usar um decorador é com o símbolo `@` (arroba) logo acima da definição da função que você quer decorar.

```py
# Primeiro, vamos criar nosso decorador

def meu_decorador_de_log(func):

    def wrapper(*args, **kwargs):
        print(f"Iniciando a execução da função '{func.__name__}'...")

        import time
        start_time = time.time() # Registra o tempo inicial
        resultado = func(*args, **kwargs) # Executa a função original
        end_time = time.time() # Registra o tempo final
        tempo_decorrido = end_time - start_time

        print(f"Função '{func.__name__}' finalizada. Resultado: {resultado}")
        print(f"Tempo de execução: {tempo_decorrido:.4f} segundos.")
        return resultado

    return wrapper

# Agora, vamos aplicar nosso decorador à função

@meu_decorador_de_log
def calcular_tempo_preparo(prato):
    print(f"Calculando tempo para: {prato}")
    import time
    time.sleep(0.5) # Simula um cálculo que leva tempo
    if prato == "macarrao":
        return 10
    elif prato == "lasanha":
        return 45
    else:
        return 20

# Agora, quando você chama a função, o decorador já está agindo!

calcular_tempo_preparo("macarrao")
print("-" * 30)
calcular_tempo_preparo("lasanha")
#Saída:
    # Iniciando a execução da função 'calcular_tempo_preparo'...
    # Calculando tempo para: macarrao
    # Função 'calcular_tempo_preparo' finalizada. Resultado: 10
    # Tempo de execução: 0.50XX segundos.

    # Iniciando a execução da função 'calcular_tempo_preparo'...
    # Calculando tempo para: lasanha
    # Função 'calcular_tempo_preparo' finalizada. Resultado: 45
    # Tempo de execução: 0.50XX segundos.
```
### O que aconteceu?

A função `meu_decorador_de_log` foi definida. Ela recebe uma `func` (a função a ser decorada) como entrada.
Dentro dela, definimos uma função `wrapper`. Essa `wrapper` é a que realmente contém a lógica extra (os prints, o cálculo de tempo) e, crucialmente, ela chama a func original.
O `meu_decorador_de_log` retorna a função `wrapper`.
Quando você coloca `@meu_decorador_de_log` antes de `def calcular_tempo_preparo(...)`, o Python faz o seguinte:
`calcular_tempo_preparo = meu_decorador_de_log(calcular_tempo_preparo)`
Ou seja, ele passa sua função original para o decorador, e o decorador "embrulha" sua função com o `wrapper` e a retorna. A partir de então, quando você chama `calcular_tempo_preparo()`, na verdade, você está chamando a função `wrapper` que o decorador retornou.

### Por que eles são tão legais?

* **Reutilização de Código**: Você escreve a lógica de log (ou qualquer outra funcionalidade) uma vez e a aplica a quantas funções quiser.
* **Separação de Preocupações**: Sua função calcular_tempo_preparo continua focada apenas em calcular o tempo. A preocupação de "fazer log" fica com o decorador. Isso deixa seu código mais limpo e fácil de entender.
* **Adição de Funcionalidades Comuns**: Autenticação, logs, cache, validação de argumentos, tratamento de erros – tudo isso pode ser implementado de forma elegante com decoradores.

Decoradores são uma das características mais elegantes e Pythonicas da linguagem, e dominá-los é um passo importante para escrever código mais modular e poderoso! É como ter um kit de upgrades super fácil de aplicar nas suas funções!
