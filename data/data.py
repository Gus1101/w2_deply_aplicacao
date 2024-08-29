from typing import List, Dict
from fastapi import HTTPException
from app.schema import ProdutosSchema

class Produtos:
	
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

	def lista_de_produtos(self):
		return self.produtos

	def buscar_produto(self,id):
		for produto in self.produtos:
			if produto["id"] == id:
				return produto
		raise HTTPException(status_code=404, detail="Produto não encontrado")
	
	def adicionar_produto(self, produto):
		self.produtos.append(produto.dict())
		return produto
	
	def deletar_produto(self, id):
		self.produtos = [produto for produto in self.produtos if produto["id"] != id]
		return self.produtos