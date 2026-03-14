from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tarefas = []
contador_id = 1


class Tarefa(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False


@app.get("/")
def home():
    return {"mensagem": "API de Gerenciamento de Tarefas"}


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    global contador_id

    nova_tarefa = {
        "id": contador_id,
        "titulo": tarefa.titulo,
        "descricao": tarefa.descricao,
        "concluida": tarefa.concluida
    }

    tarefas.append(nova_tarefa)
    contador_id += 1

    return nova_tarefa


@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, tarefa: Tarefa):
    for t in tarefas:
        if t["id"] == id:
            t["titulo"] = tarefa.titulo
            t["descricao"] = tarefa.descricao
            t["concluida"] = tarefa.concluida
            return t

    return {"erro": "Tarefa não encontrada"}


@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    for t in tarefas:
        if t["id"] == id:
            tarefas.remove(t)
            return {"mensagem": "Tarefa removida"}

    return {"erro": "Tarefa não encontrada"}