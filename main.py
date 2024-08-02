from fastapi import FastAPI, HTTPException
from typing import List, Dict

produtos: List[Dict[str, any]] = [
	{
		"id":1,
		"nome":"Smartphone",
		"descricao":"um telefone inteligente",
		"preco":1500.0,
		"disponivel":False,
	},
	{
		"id":2,
		"nome":"Notebook",
		"descricao":"Um computador portatil",
		"preco":3500.0,
		"disponivel": False,
	},
    {
        "id":3,
		"nome":"Tablet",
        "descricao":"Um celular maior",
        "preco":4000.0,
        "disponivel": False,
	}
]

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Olá":"Mundo"}

@app.get("/lista_de_produtos")
def lista_de_produtos():
	return produtos

@app.get("/lista_de_produtos/{id}")
def buscar_produto(id: int):
    for produto in produtos:
        if produto["id"] == id:
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")