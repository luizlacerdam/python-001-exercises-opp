from src.livro.livro import Livro
import pytest

pytestmark = pytest.mark.dependency()


def test_descricao_livro(capsys):
    livro = Livro("The Book of five rings", "Myamoto Musashi", 300)
    print(livro)
    repr = capsys.readouterr()
    assert repr.out == "O livro The Book of five rings de Myamoto Musashi possui 300 páginas.\n"
    
