import sqlite3
import unicodedata

DEFAULT_DB = "estoque.db"


def remover_acentos(texto: str) -> str:
    nfkd = unicodedata.normalize("NFKD", texto or "")
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower()


def init_db(db_path: str = DEFAULT_DB):
    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sku TEXT NOT NULL UNIQUE,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL CHECK(preco > 0),
                quantidade INTEGER NOT NULL CHECK(quantidade >= 0)
            )
        """)
        conn.commit()


def validar_dados(sku: str, nome: str, categoria: str, preco: float, quantidade: int):
    if not sku or not sku.strip():
        raise ValueError("O código SKU é obrigatório.")
    if not nome or len(nome.strip()) < 2:
        raise ValueError("Informe um nome válido para o produto.")
    if not categoria or not categoria.strip():
        raise ValueError("A categoria é obrigatória.")
    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")
    if quantidade < 0:
        raise ValueError("A quantidade em estoque não pode ser negativa.")


def criar_produto(sku: str, nome: str, categoria: str, preco: float, quantidade: int, db_path: str = DEFAULT_DB):
    validar_dados(sku, nome, categoria, preco, quantidade)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "INSERT INTO produtos (sku, nome, categoria, preco, quantidade) VALUES (?, ?, ?, ?, ?)",
            (sku.strip().upper(), nome.strip(), categoria.strip(), round(preco, 2), quantidade),
        )
        conn.commit()


def listar_produtos(busca: str = "", db_path: str = DEFAULT_DB):
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        linhas = conn.execute("SELECT * FROM produtos ORDER BY id DESC").fetchall()
        produtos = [dict(linha) for linha in linhas]

    if busca and busca.strip():
        termo = remover_acentos(busca.strip())
        produtos = [
            p for p in produtos
            if termo in remover_acentos(p["nome"])
            or termo in remover_acentos(p["sku"])
            or termo in remover_acentos(p["categoria"])
        ]
    return produtos


def buscar_por_id(produto_id: int, db_path: str = DEFAULT_DB):
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        linha = conn.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,)).fetchone()
        return dict(linha) if linha else None


def atualizar_produto(produto_id: int, sku: str, nome: str, categoria: str, preco: float, quantidade: int, db_path: str = DEFAULT_DB):
    validar_dados(sku, nome, categoria, preco, quantidade)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """UPDATE produtos
               SET sku = ?, nome = ?, categoria = ?, preco = ?, quantidade = ?
               WHERE id = ?""",
            (sku.strip().upper(), nome.strip(), categoria.strip(), round(preco, 2), quantidade, produto_id),
        )
        conn.commit()


def excluir_produto(produto_id: int, db_path: str = DEFAULT_DB):
    with sqlite3.connect(db_path) as conn:
        conn.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        conn.commit()