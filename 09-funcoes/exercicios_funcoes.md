## Exercício 1: 
Crie uma função chamada `boas_vindas`. Dentro desta função, use o comando `print()` para exibir a mensagem `"Olá! Esta é minha primeira função."`. Após definir a função, lembre-se de chamá-la para que a mensagem seja impressa.

## Exercício 2: 
Escreva uma função chamada `detalhes_produto` que aceite três parâmetros: nome, preco e categoria. A função deve imprimir uma frase formatada como: `"Produto: [Nome], Categoria: [Categoria], Preço: R$[Preço]"`.

* Chame a função uma vez usando argumentos posicionais (na ordem correta).

* Chame a função uma segunda vez usando argumentos nomeados, passando os argumentos em uma ordem diferente (ex: preco, nome, categoria).

## Exercício 3:
Crie uma função chamada `calcular_media` que receba dois números, `a` e `b`, como parâmetros. Em vez de imprimir o resultado, a função deve usar a palavra-chave `return` para devolver a média aritmética dos dois números (ou seja, `(a + b) / 2`). Após definir a função, chame-a com os valores **10** e **20**, armazene o valor retornado em uma variável chamada `media_resultado` e, por fim, imprima o valor dessa variável.

## Exercício 4: 
Defina uma função chamada `criar_personagem` que aceite dois parâmetros: nome (obrigatório) e classe (opcional). O parâmetro classe deve ter um valor padrão de `"Aventureiro"`. A função deve imprimir `"Personagem [Nome] criado como [Classe]!"`.

* Chame a função passando apenas o nome ("Herói").

* Chame a função passando o nome ("Mago") e a classe ("Feiticeiro").

## Exercício 5: 
Crie uma função `relatorio_final` que aceite um número variável de notas (usando `*args`) e um número variável de informações do aluno (usando `**kwargs`). A função deve:

* Calcular e imprimir a média das notas recebidas em `*args`.

* Imprimir `"Detalhes do Aluno:"`.

* Iterar sobre o dicionário `**kwargs` e imprimir cada chave e valor (ex: "Nome: João", "Turma: 3B"). 
  
* Exemplo de chamada: `relatorio_final(8.5, 9.0, 7.0, nome="Ana", turma="Python B", status="Aprovada")`.

## Exercício 6: 
Defina uma variável global chamada `total_vendas` e inicialize-a com 0. Crie uma função chamada `registrar_venda` que aceite um `valor_venda`. Dentro desta função, utilize a palavra-chave `global` para acessar e modificar a variável `total_vendas`, adicionando o `valor_venda` a ela. Faça três chamadas para `registrar_venda(100)`, `registrar_venda(50)` e `registrar_venda(200)`. No final do script, imprima o valor final da variável global `total_vendas`.

## Exercício 7: 
Você tem uma lista de nomes:` nomes = ["Ana", "Pedro", "Maria", "João", "Beatriz"]`. Use a função `sorted()` em conjunto com uma função `lambda` para ordenar essa lista pelo comprimento de cada nome (do menor para o maior), e não pela ordem alfabética. (Dica: use o argumento `key` da função `sorted()`). Imprima a lista ordenada.

## Exercício 8: 
Crie uma função "fábrica" chamada `gerar_saudacao_personalizada` que aceite um prefixo (ex: "Bom dia"). Dentro dela, defina uma função interna chamada `saudar` que aceite um nome. A função `saudar` deve retornar a string `f"{prefixo}, {nome}!"`, utilizando o prefixo do escopo envolvente. A função externa (`gerar_saudacao_personalizada`) deve retornar a função interna `saudar`. 

* Crie uma variável` saudacao_manha = gerar_saudacao_personalizada("Bom dia")`.

* Imprima o resultado de `saudacao_manha("Carlos")`.

## Exercício 9: 
Crie um decorador chamado `timer`. Este decorador deve:

* Definir uma função `wrapper` interna que aceite `*args` e `**kwargs`.
* Antes de executar a função original, imprimir `"Iniciando função..."`.
* Executar a função original e armazenar seu resultado.
* Depois de executar, imprimir `"Função finalizada."`.

Retornar o resultado da função original. Aplique este decorador (usando a sintaxe `@timer`) a uma função chamada `tarefa_simples` que simplesmente imprime `"Executando tarefa..."` e retorna `True`. Chame a função `tarefa_simples()`.
