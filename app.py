from flask import Flask
from controllers.produto_controller import produto_bp
from models.produto_model import init_db

app = Flask(__name__, template_folder="views/templates")
app.secret_key = "chave-local-pit-engenharia-software"
app.register_blueprint(produto_bp)

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)