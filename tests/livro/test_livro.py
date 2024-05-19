from src.livro.livro import Livro
import pytest

pytestmark = pytest.mark.dependency()


def test_cria_livro():
    livro = Livro("The Book of five rings", "Myamoto Musashi", 300)
    assert livro.titulo == "The Book of five rings"
    assert livro.autor == "Myamoto Musashi"
    assert livro.paginas == 300
