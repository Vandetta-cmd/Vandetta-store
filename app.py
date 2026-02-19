from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Camiseta Oversized", "preco": 79.90},
    {"id": 2, "nome": "Moletom Premium", "preco": 149.90},
    {"id": 3, "nome": "Calça Cargo Street", "preco": 119.90}
]

carrinho = []

template = """
<!DOCTYPE html>
<html>
<head>
    <title>Vandetta Store</title>
    <style>
        body {
            font-family: Arial;
            background: #0f0f0f;
            color: white;
            margin: 0;
        }
        header {
            background: black;
            padding: 20px;
            text-align: center;
            font-size: 24px;
            letter-spacing: 2px;
        }
        .container {
            padding: 20px;
        }
        .produto {
            background: #1c1c1c;
            padding: 20px;
            margin: 15px 0;
            border-radius: 12px;
        }
        button {
            background: #e60023;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 6px;
            cursor: pointer;
        }
        .carrinho {
            background: #141414;
            padding: 20px;
            margin-top: 30px;
            border-radius: 12px;
        }
    </style>
</head>
<body>

<header>
    🛍️ VANDATTA STORE - STREETWEAR
</header>

<div class="container">

    <h2>Produtos</h2>

    {% for produto in produtos %}
    <div class="produto">
        <h3>{{ produto.nome }}</h3>
        <p>R$ {{ produto.preco }}</p>
        <form method="POST" action="/add/{{ produto.id }}">
            <button type="submit">Adicionar ao Carrinho</button>
        </form>
    </div>
    {% endfor %}

    <div class="carrinho">
        <h2>🛒 Carrinho</h2>
        {% if carrinho %}
            <ul>
                {% for item in carrinho %}
                    <li>{{ item.nome }} - R$ {{ item.preco }}</li>
                {% endfor %}
            </ul>
            <h3>Total: R$ {{ total }}</h3>
        {% else %}
            <p>Carrinho vazio.</p>
        {% endif %}
    </div>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    total = sum(item["preco"] for item in carrinho)
    return render_template_string(template, produtos=produtos, carrinho=carrinho, total=round(total, 2))

@app.route("/add/<int:id>", methods=["POST"])
def add(id):
    for produto in produtos:
        if produto["id"] == id:
            carrinho.append(produto)
            break
    return redirect(url_for("home"))

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
