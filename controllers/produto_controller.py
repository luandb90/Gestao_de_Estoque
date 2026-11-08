import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import produto_model

produto_bp = Blueprint("produto", __name__)


def converter_moeda(valor_str: str) -> float:
    limpo = (valor_str or "").strip().replace("R$", "").replace(" ", "").replace(",", ".")
    return float(limpo)


@produto_bp.route("/", methods=["GET"])
def index():
    busca = request.args.get("q", "")
    editar_id = request.args.get("editar_id", type=int)
    produtos = produto_model.listar_produtos(busca=busca)
    produto_edicao = produto_model.buscar_por_id(editar_id) if editar_id else None

    valor_total = sum(p["preco"] * p["quantidade"] for p in produtos)
    estoque_baixo = sum(1 for p in produtos if p["quantidade"] < 5)

    return render_template(
        "index.html",
        produtos=produtos,
        busca=busca,
        produto_edicao=produto_edicao,
        valor_total=valor_total,
        estoque_baixo=estoque_baixo,
    )


@produto_bp.route("/salvar", methods=["POST"])
def salvar():
    produto_id = request.form.get("id")
    sku = request.form.get("sku", "")
    nome = request.form.get("nome", "")
    categoria = request.form.get("categoria", "")

    try:
        preco = converter_moeda(request.form.get("preco", ""))
        quantidade = int(request.form.get("quantidade", ""))

        if produto_id:
            produto_model.atualizar_produto(int(produto_id), sku, nome, categoria, preco, quantidade)
            flash("Produto atualizado com sucesso!", "sucesso")
        else:
            produto_model.criar_produto(sku, nome, categoria, preco, quantidade)
            flash("Produto cadastrado no estoque!", "sucesso")

    except ValueError as erro:
        msg = str(erro)
        if "could not convert" in msg or "invalid literal" in msg:
            msg = "Preencha preço e quantidade apenas com números válidos (ex: 49,90 e 10)."
        flash(msg, "erro")
    except sqlite3.IntegrityError:
        flash("Já existe um produto cadastrado com este código SKU.", "erro")

    return redirect(url_for("produto.index"))


@produto_bp.route("/excluir/<int:produto_id>", methods=["POST"])
def excluir(produto_id: int):
    produto_model.excluir_produto(produto_id)
    flash("Item removido do estoque.", "sucesso")
    return redirect(url_for("produto.index"))