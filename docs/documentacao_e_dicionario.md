# StockFlow - Documentação Técnica Revisada (PIT II)

## 1. Escopo e Arquitetura (MVC)
Aplicação web para controle de estoque de pequenos comércios, estruturada no padrão **MVC (Model-View-Controller)**:
- **Model (`models/produto_model.py`)**: Regras de domínio, validação de integridade e persistência SQL.
- **View (`views/templates/index.html`)**: Interface limpa, responsiva e com feedback imediato de ações (IHC).
- **Controller (`controllers/produto_controller.py`)**: Tratamento de requisições HTTP, sanitização de entradas (ex.: conversão de moeda com vírgula) e roteamento.

## 2. Diagrama de Classe de Persistência (Resumo Revisado)
**Classe: Produto**
- `+ id: int (PK, Auto Increment)`
- `+ sku: string`
- `+ nome: string`
- `+ categoria: string`
- `+ preco: float`
- `+ quantidade: int`
- Métodos: `validar_dados()`, `criar_produto()`, `listar_produtos()`, `atualizar_produto()`, `excluir_produto()`

## 3. Projeto Físico e Dicionário de Dados (Tabela `produtos`)

| Atributo | Tipo Físico (SQL) | Domínio / Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT`, Não nulo | Identificador único interno do registro |
| `sku` | ` VARCHAR(30)` | `UNIQUE`, `NOT NULL` | Código identificador único do produto no estoque |
| `nome` | `VARCHAR(120)` | `NOT NULL`, mín. 2 caracteres | Nome descritivo do item |
| `categoria` | `VARCHAR(60)` | `NOT NULL` | Categoria de organização (ex.: Vestuário, Periféricos) |
| `preco` | `DECIMAL(10,2)` | `NOT NULL`, `CHECK (preco > 0)` | Preço unitário de venda em reais (R$) |
| `quantidade`| `INTEGER` | `NOT NULL`, `CHECK (quantidade >= 0)` | Saldo físico atual disponível no estoque |