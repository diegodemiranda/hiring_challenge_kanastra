# README.md

## Descrição do Projeto

Este projeto é uma aplicação web que permite a criação de cobranças. A aplicação é dividida em duas partes principais: o backend, que é uma API construída com FastAPI, e o frontend, que é uma aplicação React.

## Estrutura do backend

O backend é organizado da seguinte forma:

- `backend/`: Este diretório contém o código do backend da aplicação, que é uma API construída com FastAPI.
  - `crud.py`: Este arquivo contém as operações de banco de dados para a entidade `Charge`.
  - `database.py`: Este arquivo configura a conexão com o banco de dados.
  - `models.py`: Este arquivo define o modelo de dados para a entidade `Charge`.
  - `schemas.py`: Este arquivo define os esquemas Pydantic para a entidade `Charge`.
  - `main.py`: Este é o ponto de entrada da aplicação. Ele define as rotas da API e configura o middleware.

## Como Executar o Projeto

1. Certifique-se de que você tem Docker e Docker Compose instalados em sua máquina.

2. Navegue até o diretório que contém o arquivo `docker-compose.yml`.

3. Execute o seguinte comando para construir as imagens Docker e iniciar os contêineres:

```bash
docker-compose up --build
```

4. A aplicação estará disponível em `http://localhost:8000`.

## Variáveis de Ambiente

As seguintes variáveis de ambiente são necessárias para executar a aplicação:

- `DATABASE_URL`: A URL de conexão com o banco de dados.
- `FRONTEND_URL`: A URL do frontend da aplicação.
- `REACT_APP_API_URL`: A URL da API do backend.

Essas variáveis de ambiente podem ser definidas em um arquivo `.env` na raiz do projeto.


## Estrutura do frontend

O frontend é organizado da seguinte forma:

- `frontend/`: Este diretório contém o código do frontend da aplicação, que é uma aplicação React.
  - `src/`: Este diretório contém o código fonte da aplicação React.
    - `assets/`: Este diretório contém os ativos da aplicação, como imagens.
    - `components/`: Este diretório contém os componentes React da aplicação.
      - `ChargeForm.js`: Este componente é um formulário que permite ao usuário criar uma nova cobrança.
    - `App.js`: Este é o componente principal da aplicação. Ele renderiza o `ChargeForm`.
    - `App.scss`: Este arquivo contém os estilos globais da aplicação.
    - `index.js`: Este é o ponto de entrada da aplicação React.
    - `reportWebVitals.js`: Este arquivo é usado para relatar as métricas da web vitals para o Google Analytics.
    - `setupTests.js`: Este arquivo é usado para configurar os testes da aplicação.
    - `App.test.js`: Este arquivo contém os testes para o componente `App`.

## Como Executar o Projeto

1. Certifique-se de que você tem Node.js e npm instalados em sua máquina.

2. Navegue até o diretório `frontend` do projeto.

3. Execute o seguinte comando para instalar as dependências do projeto:

```bash
npm install
```

4. Execute o seguinte comando para iniciar a aplicação:

```bash
npm start
```

5. A aplicação estará disponível em `http://localhost:3000`.

## Variáveis de Ambiente

As seguintes variáveis de ambiente são necessárias para executar a aplicação:

- `REACT_APP_API_URL`: A URL da API do backend.

Essas variáveis de ambiente podem ser definidas em um arquivo `.env` na raiz do diretório `frontend`.


## Descrição da geração da imagem Docker

A geração da imagem é organizado da seguinte forma:

- `Dockerfile`: Este arquivo define as instruções para construir a imagem Docker para a aplicação. Ele é dividido em duas partes: a construção do frontend e a construção do backend.
- `docker-compose.yml`: Este arquivo define os serviços que compõem a aplicação. Ele inclui um serviço para o banco de dados (Postgres) e um serviço para a aplicação web (que inclui o frontend e o backend).
- `requirements.txt`: Este arquivo lista as dependências Python necessárias para o backend da aplicação.

## Como Executar o Projeto

1. Certifique-se de que você tem Docker e Docker Compose instalados em sua máquina.

2. Navegue até o diretório que contém o arquivo `docker-compose.yml`.

3. Execute o seguinte comando para construir as imagens Docker e iniciar os contêineres:

```bash
docker-compose up --build
```

4. A aplicação estará disponível em `http://localhost:8000`.

## Variáveis de Ambiente

As seguintes variáveis de ambiente são necessárias para executar a aplicação:

- `DATABASE_URL`: A URL de conexão com o banco de dados.
- `REACT_APP_API_URL`: A URL da API do backend.

Essas variáveis de ambiente podem ser definidas em um arquivo `.env` na raiz do projeto.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
