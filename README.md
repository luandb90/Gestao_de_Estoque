# 📦 Inventário Inteligente — Sistema de Gestão de Estoque

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Microframework-lightgrey?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

## 💻 Sobre o Projeto
O **Inventário Inteligente** é uma aplicação web responsiva para controle e gestão de estoque. Desenvolvido como Projeto Integrador Transdisciplinar (PIT II) do curso de Engenharia de Software, o sistema foca em estabilidade, integridade de dados e facilidade de uso (IHC).

O projeto aplica conceitos práticos de Engenharia de Software, como a separação de responsabilidades no padrão arquitetural **MVC (Model-View-Controller)**, tratamento de exceções, validação de regras de negócio e testes unitários.

## ✨ Funcionalidades
- **CRUD Completo:** Criação, leitura, atualização e exclusão de produtos.
- **Dashboard Dinâmico:** Cálculo automático do valor total financeiro em estoque e quantidade de itens listados.
- **Alertas Inteligentes:** Destaque visual automático para produtos com estoque baixo (< 5 unidades).
- **Busca Otimizada:** Barra de pesquisa inteligente com normalização de strings (ignora acentos e letras maiúsculas/minúsculas).
- **Sanitização de Dados:** Tratamento automático de inputs do usuário (ex: converte preços digitados com vírgula para ponto flutuante, evitando *Internal Server Errors*).
- **Proteção de Integridade:** Bloqueio e alertas visuais contra códigos SKU duplicados, estoque negativo e preços zerados.
- **Prevenção de Erros (IHC):** Validação e caixas de confirmação nativas antes de ações destrutivas (exclusão).

## 🛠️ Tecnologias e Arquitetura
A aplicação foi construída visando uma arquitetura limpa:

- **Back-end:** Python 3.12 com Flask.
- **Banco de Dados:** SQLite 3 (ideal para ambientes de desenvolvimento e aplicações locais).
- **Front-end:** HTML5, CSS3, JavaScript e Jinja2 (Template Engine).
- **Qualidade/Testes:** Pytest.

**Estrutura MVC:**
- `/models`: Classes, entidades e comunicação com o banco de dados (regras estritas de domínio).
- `/controllers`: Lógica de roteamento HTTP, validações, tratamento do payload e captura de exceções (`IntegrityError`).
- `/views/templates`: Interfaces de usuário renderizadas dinamicamente.

## 🚀 Como Executar o Projeto Localmente

**Pré-requisitos:** Ter o [Python](https://www.python.org/downloads/) instalado na sua máquina.

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/luandb90/Gestao_de_Estoque.git
   ```
2. **Acesse a pasta do projeto:**
   ```bash
   cd Gestao_de_Estoque
   ```
3. **Crie e ative um ambiente virtual (Recomendado):**
   - No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Execute a aplicação:**
   ```bash
   python app.py
   ```
6. **Acesse no navegador:**
   Abra `http://127.0.0.1:5000`

## 🧪 Testes Automatizados
O sistema possui uma suíte de testes unitários para validar as regras da camada de Modelo e segurança de dados. Para executar os testes, utilize o comando:
```bash
python -m pytest -v
```

## 👨‍💻 Autor
**Luan Brito**
- Estudante de Engenharia de Software
- Experiência em Suporte Operacional/NOC e transição para o Desenvolvimento Full-Stack.
- [Conecte-se comigo no LinkedIn](https://www.linkedin.com/in/luan-brito/)
  
