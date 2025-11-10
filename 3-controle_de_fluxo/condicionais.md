# Estruturas condicionais
Estruturas condicionais são simplesmente desvios que o fluxo de execução de um código poderá levar. Os comandos destas estruturas são if, else e elif. 

<img src="Screenshot_2025-11-10_00-06-38.png">

Por padrão, os programas em python são executados na ordem que estão inseridos no código, também conhecidos de programas sequenciais, em que as ações acontecem do início ao fim, umas após a outra. Por outro lado, em algumas situações, um caminho pode abrir vertentes de possibilidades para seguir. Um exemplo seria o trajeto para ir do restaurante até o mercado de carro, porém, neste dia em questão, são 13:00h e há um congestionamento em parte do caminho usual. Então, você como motorista, pode seguir o caminho usual, que você sabe que é a opção mais curta até o mercado, mas hoje possui congestionamento, ou ir por um outro caminho, que é mais longo, mas está sem congestionamento. O conceito por trás desta questão é muito parecido com o funcionamento na linguagem de programação.

Agora, vamos pensar na escola, que você recebe notas pelas provas e trabalhos que faz durante o ano. Ao final do ano letivo, você precisa estar acima da média, 7 pontos, para ir para a próxima série.

Digamos que nesse cenário, o aluno teve duas avaliações, então teremos as variáveis nota1 e nota2 no código. Devemos calcular a média aritmética, e com o resultado, sabermos se o aluno foi aprovado ou reprovado. Como fazer isto?
```
nota1 = float(input('Digite a nota da 1° avaliação: '))
nota2 = float(input('Digite a nota da 2° avaliação: '))

media = (nota1 + nota2) / 2

if (media >= 7):
    print('Aluno aprovado')
else:
    print('Aluno reprovado')
```
A estrutura do if sempre estará acompanhada de uma condição, está condição deve retornar verdadeiro ou falso. É isso que a estrutura valida, se for verdadeiro, entrará no bloco de comandos do if, caso contrário, passará para o próximo comando, se houver um else, entrará no bloco de comandos do else.

Provavelmente, você já notou que um comando if quer saber se algo é verdadeiro ou falso. A utilização de operadores lógicos e de comparação sempre geram como resultado um valor lógico, isto é, True ou False.
Pensando em criar um algoritmo para determinar o dia da semana a partir da entrada do usuário, em que 1 equivale a domingo, 2 refere-se a segunda-feira e assim sucessivamente, como podemos estruturar este código?

Pode parecer algo simples e monótono de se pensar. Podemos visualizar esta lógica por trás do resultado que buscamos, através do diagrama a seguir.

<img src="Screenshot_2025-11-10_00-07-21.png">

Para esta estrutura introduziremos um novo comando em nosso código: o elif!

Pense comigo: no exemplo da escola, a vida era simples. Ou você estava aprovado ou estava reprovado. Só tínhamos dois caminhos (o if e o else).

Mas e se tivéssemos mais de duas possibilidades?

Voltando ao nosso problema do dia da semana, a situação é bem diferente. Temos sete possibilidades, certo?

* Se for 1, o dia é Domingo.
* Se for 2, o dia é Segunda.
* Se for 3, o dia é Terça.
* ...e por aí vai!

Se fôssemos usar apenas o if e o else, a coisa ficaria meio confusa e repetitiva, parecendo um monte de caixas empilhadas. É aí que o nosso novo amigo, o elif (que é a junção de else if), entra em campo para salvar o dia!

O elif permite que você verifique múltiplas condições de forma organizada. Ele só é checado se o if anterior (ou o elif anterior) for falso. Se for verdadeiro, ele executa o bloco dele e pula o resto das verificações. Pense nele como: "Já que a primeira não rolou, E SE for essa aqui?"

Vamos ver como ficaria o nosso código para descobrir o dia da semana:
```
dia = int(input('Digite um número de 1 a 7: '))
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-feira')
elif dia == 3:
    print('Terça-feira')
elif dia == 4:
    print('Quarta-feira')
elif dia == 5:
    print('Quinta-feira')
elif dia == 6:
    print('Sexta-feira')
elif dia == 7:
    print('Sábado')
else:
    # E se o usuário digitar 8 ou 0? O "else" entra em ação!
    print('Valor inválido! Digite um número de 1 a 7.')
```

Viu que maravilha? A gente usa o if para a primeira condição, quantos elif forem necessários para as condições intermediárias, e o else no final fica como a nossa "porta de segurança", capturando qualquer caso que não se encaixe em nenhuma das condições anteriores (como quando o usuário digita 8 ou um número negativo!).

### Recapitulando a estrutura:
1. Começa sempre com um if.
2. Pode ter zero, um ou vários elif no meio.
3. Pode ter zero ou um else no final.

## Operador ternário:

Agora que você já está craque no if-else, deixe eu te apresentar o atalho dos ninjas: a operação ternária, também conhecido como if-else de uma linha.

Lembram do nosso primeiro exemplo da escola?
```
if (media >= 7):
    print('Aluno aprovado')
else:
    print('Aluno reprovado')
```

Perceba que a única coisa que o if e o else fazem é atribuir um valor ou executar uma ação simples (como um print) com base em uma condição.

Se você está apenas querendo decidir o valor de uma variável ou o resultado de um print entre duas opções, o Python permite que você faça isso de forma super compacta, usando a estrutura ternária:

```
valor = valor_se_verdadeiro if condição else valor_se_falso
```

Esta estrutura deve ser atribuída a uma variável.

```
status_aluno = 'Aluno aprovado' if media >= 7 else 'Aluno reprovado'
print(status_aluno)
```

**Lembre-se**: A operação ternária é ótima para coisas simples de duas opções. Para lógica mais complexa, com múltiplas condicionais, o formato tradicional continua sendo a melhor pedida para manter o seu código fácil de ler.
