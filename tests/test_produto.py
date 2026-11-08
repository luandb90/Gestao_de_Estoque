import sqlite3
import pytest
from models import produto_model
from controllers.produto_controller import converter_moeda

@pytest.fixture
def banco_temp(tmp_path):
    caminho = str(tmp_path / "teste_estoque.db")
    produto_model.init_db(caminho)
    return caminho


def test_criar_e_listar_produto(banco_temp):
    produto_model.criar_produto("TEC-01", "Teclado Mecânico", "Periféricos", 199.90, 8, db_path=banco_temp)
    itens = produto_model.listar_produtos(db_path=banco_temp)
    assert len(itens) == 1
    assert itens[0]["sku"] == "TEC-01"


def test_conversao_moeda_com_virgula():
    assert converter_moeda("39,90") == 39.90
    assert converter_moeda("R$ 120,50") == 120.50


def test_bloqueia_estoque_negativo_e_preco_zero(banco_temp):
    with pytest.raises(ValueError):
        produto_model.criar_produto("ERR-01", "Mouse", "Periféricos", 50.0, -3, db_path=banco_temp)

    with pytest.raises(ValueError):
        produto_model.criar_produto("ERR-02", "Mouse", "Periféricos", 0.0, 5, db_path=banco_temp)


def test_bloqueia_sku_duplicado(banco_temp):
    produto_model.criar_produto("CAM-001", "Camiseta Básica", "Vestuário", 49.90, 10, db_path=banco_temp)
    with pytest.raises(sqlite3.IntegrityError):
        produto_model.criar_produto("CAM-001", "Calça Jeans", "Vestuário", 119.90, 4, db_path=banco_temp)


def test_busca_ignora_acentos(banco_temp):
    produto_model.criar_produto("BON-01", "Boné Aba Curva", "Acessórios", 59.90, 3, db_path=banco_temp)
    resultado = produto_model.listar_produtos(busca="bone", db_path=banco_temp)
    assert len(resultado) == 1