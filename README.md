[![Build Status](https://travis-ci.org/Alfareiza/cards-to-trello-from-movidesk.svg?branch=master)](https://travis-ci.org/Alfareiza/cards-to-trello-from-movidesk)

# Cria Cards no Trello de Movidesk 

Programa de escritorio que cria cards no trello a partir de tickets registrados no movidesk.
- Que é movidesk >  Plataforma de Atendimento (Help Desk) [O que é Movidesk?](https://www.movidesk.com)
- Que é Trello > Plataforma de Organização de Projetos [O que é trello?](https://trello.com/c/Bbpc1cRl/2-o-que-é-trello)

## Interface

![Splash Screen](https://github.com/Alfareiza/cards-to-trello-from-movidesk/blob/master/files/img/splash_screen_example.png?raw=True)

![Interface](https://github.com/Alfareiza/cards-to-trello-from-movidesk/blob/master/files/img/interface_example.png?raw=true)

## Vamos lá

O programa procura os tickets registrados no movidesk, e através da interface é possível criar um card no trello com as informações do ticket. Você conseguirá selecionar quais membros, etiquetas e a lista onde o card será criado.

### Requisitos

- [x] É necessário ter Pip e [Python 3.8.1](https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe) instalado e configurados como variáveis de ambiente. Feito isso, você deve instalar `pipenv` da seguinte forma.
```
pip install pipenv
```
- [x] Obter informações de `TRELLO_TOKEN`, `TRELLO_KEY`, `TRELLO_BOARD` e `MOVIDESK_TOKEN`.
        
    - `TRELLO_KEY`: Para obter o KEY, você deve acessar neste site: https://trello.com/app-key
    - `TRELLO_TOKEN` : Para obter o TOKEN, você deve obter primeiro o KEY, e [nesse site](https://trello.com/app-key) tem o link para gerar o token.  
    - `TRELLO_BOARD` : Para obter o TRELLO_BOARD você deve ir até sua conta e pegar o nome do BOARD. Lembre de considerar as mayúsculas e minúsculas
    - `MOVIDESK_TOKEN`: Para obter o TOKEN do movidesk você deve acessar ao Movidesk, logo em Configurações > Conta > Parâmetros e na guia ambiente clique no botão "Gerar nova chave"

- [x] Criar arquivo `.env`
    Você deve criar um arquivo de extensão .env que tenha a seguinte estrutura com os dados obtidos no passo anterior:
    ```
    TRELLO_TOKEN=
    TRELLO_KEY=
    TRELLO_BOARD=MEU BOARD
    MOVIDESK_TOKEN=
    ``` 
### Instalação

Após instalar o pipenv no seu PC, você deve executar o seguinte comando na pasta onde o projeto foi clonado.

```
pipenv install -d
```

Logo,

```
python files/main.py
```

Será executado um splashscreen que internamente terá os valores de Trello. Logo, vai carregar a interface onde poderá interagir da seguinte forma:
- número do ticket (obrigatório):  digite o numero do ticket e o programa irá validar a existência dele quando digitar no botão "Create", e ter selecionado uma lista.
- lista (obrigatório): selecione a lista onde o ticket vai ficar.
- etiquetas (opcional): selecione quantas etiquetas deseje para o card.
- membros (opcional): selecione quantos membros deseje para o card.


## Arquivos do Projeto

- .env: Arquivo que deve ficar na raiz com as informações de TRELLO_TOKEN, TRELLO_KEY, TRELLO_BOARD, MOVIDESK_TOKEN. Esse possui informações confidenciais e por isso cada usuário deve ter o seu.  
- [start.bat](https://github.com/Alfareiza/cards-to-trello-from-movidesk/blob/master/start.bat): Atalho para windows que ajuda a executar o projeto sem que seja pela linha de comando. Para que funcione sua execução, ele deve estar na pasta raíz do projeto.  
- [files/main.py](https://github.com/Alfareiza/cards-to-trello-from-movidesk/blob/master/files/main.py): Módulo principal que chama ao splash seguido da interface de iteração.
- [files/ui_splash_screen.py](https://github.com/Alfareiza/cards-to-trello-from-movidesk/blob/master/files/ui_splash_screen.py): Módulo que carrega a tela inicial do programa. A construção desse splash foi graças a [Wanderson Magalhaes](https://www.youtube.com/watch?v=Ap865V3sAdw)   
- [files/ui_main.py](https://github.com/Alfareiza/cards-to-trello-from-movidesk/blob/master/files/ui_main.py): Módulo que interage com o usuário, ele valida e captura as informações do usuário. Esse módulo comunica-se com os módulos [files/trello.py](https://github.com/Alfareiza/cards-to-trello-from-movidesk/blob/master/files/trello.py) e [files/movidesk.py](https://github.com/Alfareiza/cards-to-trello-from-movidesk/blob/master/files/movidesk.py) para a criação do card no trello.

### Como Debugar

Pode ser que precise debugar pois algo não esperado esteja acontecendo, para isso, no windows você deve executar pela linha de comando, ubicado na pasta do projeto o seguinte:

```
".venv\Scripts\python.exe" -X dev "files/main.py"
```

## Construido com

* [PyQT](https://www.riverbankcomputing.com/software/pyqt) - Graphic Library used for interface user.
* [PySide](https://wiki.qt.io/PySide2) - Binding Library for Qt used for SplashScreen.
* [API Trello](https://developer.atlassian.com/cloud/trello/rest/) - Used to get information of trello. 
* [API Movidesk](https://atendimento.movidesk.com/kb/article/256/movidesk-ticket-api) - Used to get information of tickets.

## Como contribuir

Todo o código segue as normas PEP8, exceto para o max-line-length, que contém 120 caracteres. Cada função/classe/método/módulo deve ter docstrings.

1. Fork o projeto e clona ele ou faz o seguinte: git clone https://github.com/Alfareiza/cards-to-trello-from-movidesk.git
2. Instala o pipenv: `pip install pipenv`
3. Instala as dependencias do dev: `pipenv install -d`
4. Desenvolve os features com tests. (opcional por enquanto)
5. Executa os tests localmente: `pipenv run pytest` (opcional por enquanto)
6. Envia um pull request com testes num commit simple.
7. Envia o PR para revisão.
8. Após revisado e corrigido, o PR será aceito.
9. Cooque seu nome e username na parte de contribuições.

## Licenciamento

Esse projeto é licenciado com GPL - veja o [LICENSE.md](https://github.com/Alfareiza/cards-to-trello-from-movidesk/blob/master/README.md) arquivo para mais detalhes.
