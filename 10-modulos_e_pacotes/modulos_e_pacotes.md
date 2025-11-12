# Módulos em Python

Python permite organizar código em partes menores chamadas **módulos**.

Um módulo é um arquivo `.py` que contém funções, classes ou variáveis que podem ser reutilizadas em outros arquivos. Organizar módulos é como guardar ferramentas em caixas diferentes: em vez de deixar tudo espalhado, você separa por utilidade.

## Exemplo de módulo

Arquivo `saudacao.py`:

```py
def ola(nome):
    print(f'Olá, {nome}! Seja bem-vindo(a).')
```

Usando o módulo em outro arquivo (`principal.py`):

```py
import saudacao
saudacao.ola('Morgana')
```

O Python procura módulos nos caminhos listados em `sys.path`, incluindo:

- o diretório atual
- diretórios padrão da instalação
- pacotes instalados via `pip`

## Formas de importação

- `import modulo`
- `from modulo import funcao`
- `import modulo as apelido`

### Proteção com `main`

Para evitar que partes do código sejam executadas quando um módulo é importado, use a proteção com `if __name__ == '__main__':`:

```py
if __name__ == '__main__':
    # código executado somente se o arquivo for rodado diretamente
    pass
```

## Pacotes em Python

Um **pacote** é uma coleção de módulos organizados dentro de uma pasta. O arquivo `__init__.py` indica que o diretório é um pacote. Ele pode:

- estar vazio
- conter inicializações
- definir o que será exportado

Estrutura de exemplo:

```
meu_projeto/
├── util/
│   ├── __init__.py
│   ├── saudacao.py
│   └── calculo.py
└── app.py
```

Importando funções do pacote:

```py
from util.saudacao import ola
ola('Maria Eduarda')
```

Pacotes permitem hierarquias complexas, suporte a namespaces e integração com pacotes externos instalados via `pip`, como `numpy` ou `requests`.

Importações podem ser absolutas ou relativas:

- Importações absolutas especificam o caminho completo do pacote ou módulo a partir da raiz do projeto (ex.: `from meu_projeto.util.saudacao import ola`).
- Importações relativas usam pontos para indicar a posição atual dentro da hierarquia do pacote (ex.: `from .saudacao import ola` dentro de `util/calculo.py`).

Enquanto as importações absolutas são geralmente preferidas pela clareza em projetos grandes, as relativas podem ser úteis para referenciar módulos dentro do mesmo pacote, especialmente em submódulos.

Dentro do arquivo `__init__.py` de um pacote, é possível definir uma lista chamada `__all__`. Essa lista especifica quais módulos ou nomes serão importados quando um usuário utilizar a sintaxe `from pacote import *`. Isso permite um controle explícito sobre a interface pública do pacote, evitando a importação de nomes internos ou não desejados.

## Boas práticas

Seguir convenções como as **PEP 8** (estilo de código) e **PEP 257** (docstrings) garante legibilidade e consistência.

Dicas principais:

- Organize importações em blocos: módulos nativos, depois pacotes externos e, por fim, módulos internos.
- Use docstrings para documentar funções e classes.
- Prefira `python -m pacote.modulo` para executar pacotes corretamente.
- Cuidado com argumentos mutáveis em funções (exemplo abaixo).

### Exemplo: evitar argumentos mutáveis como padrão

Evite:

```py
def adiciona(item, lista=[]):
    lista.append(item)
    return lista
```

Prefira:

```py
def adiciona(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

## Exemplos adicionais

Exemplo de módulo com múltiplas funções (assumindo a estrutura `meu_projeto/util/calculo.py`):

```py
# meu_projeto/util/calculo.py
def soma(a, b):
    return a + b

def multiplicar(a, b):
    return a * b
```

Importando e usando funções específicas:

```py
from util.calculo import soma, multiplicar
print(soma(5, 3))             # Saída: 8
print(multiplicar(4, 2))      # Saída: 8
```

## Como executar

Dentro da pasta `meu_projeto/`:

```sh
python app.py
```

Ou, se estiver na pasta acima (como pacote raiz):

```sh
python -m meu_projeto.app
```

Esses exemplos mostram como o Python facilita o reuso de código e a organização de projetos de forma clara e eficiente.
