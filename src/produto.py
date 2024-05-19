class Produto:
    def __init__(
        self, nome: str, codigo: str, preco: float, quantidade: int
    ) -> None:
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

    def get_preco(self) -> float:
        return self.preco

    def get_quantidade(self) -> int:
        return self.quantidade

    def atualizar_preco_do_produto(self, novo_preco: float) -> None:
        if novo_preco < 0:
            raise ValueError("Preço não pode ser negativo")
        else:
            self.preco = novo_preco

    def adicionar_estoque_do_produto(self, quantidade: int) -> None:
        self.quantidade += quantidade

    def remover_estoque_do_produto(self, quantidade: int) -> None:
        self.quantidade -= quantidade
