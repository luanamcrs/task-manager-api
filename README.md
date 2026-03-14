# Task Manager API 🚀

API REST desenvolvida em Python para gerenciamento de tarefas.
Este projeto foi criado com o objetivo de praticar conceitos fundamentais de **desenvolvimento backend**, como criação de APIs, operações CRUD e comunicação via HTTP.

A aplicação permite criar, visualizar, atualizar e remover tarefas por meio de endpoints de uma API.

---

# Objetivo do Projeto

Este projeto foi desenvolvido como parte do meu aprendizado em desenvolvimento backend, com foco em:

* criação de APIs
* entendimento de requisições HTTP
* implementação de operações CRUD
* manipulação de dados utilizando JSON
* prática com frameworks modernos de backend

---

# Tecnologias Utilizadas

* Python
* FastAPI
* Uvicorn

---

# Funcionalidades

A API permite realizar as seguintes operações:

* Criar uma nova tarefa
* Listar todas as tarefas
* Atualizar uma tarefa existente
* Remover uma tarefa

Cada tarefa contém as seguintes informações:

* id
* titulo
* descricao
* concluida

---

# Estrutura da API

Principais endpoints da aplicação:

GET /tarefas
Lista todas as tarefas cadastradas.

POST /tarefas
Cria uma nova tarefa.

PUT /tarefas/{id}
Atualiza uma tarefa existente.

DELETE /tarefas/{id}
Remove uma tarefa.

---

# Exemplo de Requisição

Exemplo de criação de tarefa:

```
POST /tarefas
```

```
{
 "titulo": "Estudar FastAPI",
 "descricao": "Criar minha primeira API",
 "concluida": false
}
```

Resposta da API:

```
{
 "id": 1,
 "titulo": "Estudar FastAPI",
 "descricao": "Criar minha primeira API",
 "concluida": false
}
```

---

# Como Executar o Projeto

1. Clone o repositório

```
git clone https://github.com/seu-usuario/task-manager-api.git
```

2. Acesse a pasta do projeto

```
cd task-manager-api
```

3. Crie um ambiente virtual

```
python -m venv venv
```

4. Ative o ambiente virtual

Windows:

```
venv\Scripts\activate
```

5. Instale as dependências

```
pip install -r requirements.txt
```

6. Execute o servidor

```
uvicorn app.main:app --reload
```

---

# Documentação da API

Após iniciar o servidor, a documentação automática pode ser acessada em:

```
http://127.0.0.1:8000/docs
```

---

# Sobre Mim

Sou estudante de Tecnologia em Informática para Negócios e estou em busca de oportunidades de estágio na área de tecnologia para desenvolver minhas habilidades em programação, desenvolvimento backend e engenharia de software.
