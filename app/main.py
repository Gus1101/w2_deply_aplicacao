from fastapi import FastAPI
from data.data import Produtos
from app.schema import ProdutosSchema
from typing import List

app = FastAPI()
produtos = Produtos()

@app.get("/")
def hello_world():
    return {"Olá":"Mundo"}

@app.get("/lista_de_produtos", response_model=List[ProdutosSchema])
def lista_de_produtos():
	return produtos.lista_de_produtos()

@app.get("/lista_de_produtos/{id}", response_model=ProdutosSchema)
def busca_um_produto(id: int):
      return produtos.buscar_produto(id)

@app.post("/produtos", response_model=ProdutosSchema)
def incluir_produto(produto: ProdutosSchema):
      produtos.adicionar_produto(produto.model_dump())

@app.delete("/deletar_produto/{id}")
def deletar_produto(id: int):
      produtos.deletar_produto(id) 