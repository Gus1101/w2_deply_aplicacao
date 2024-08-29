from pydantic import BaseModel, PositiveFloat, PositiveInt

class ProdutosSchema(BaseModel):
    id : PositiveInt
    nome : str
    descricao : str
    preco : PositiveFloat
    disponivel : bool