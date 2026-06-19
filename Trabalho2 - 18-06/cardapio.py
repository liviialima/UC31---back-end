from flask import Flask, render_template, session, redirect, url_for
import webbrowser
from threading import Timer

app = Flask(__name__)
app.secret_key = "troque_essa_chave_para_producao"

menu_items = {
    1: ("Coxinha", 6),
    2: ("Kibe", 5),
    3: ("Empada", 5),
    4: ("Pastel de carne", 6),
    5: ("Pastel de queijo", 5),
    6: ("Quibe assado", 7),
    7: ("Esfiha", 5),
    8: ("Enroladinho de salsicha", 4),
    9: ("Salgadinho de frango", 6),
    10: ("Bolinha de queijo", 5),
    11: ("Risoles", 6),
    12: ("Pão de queijo", 4),
    13: ("Empanada", 6),
    14: ("Mini pizza salgada", 7),
    15: ("Torta salgada", 8),
    16: ("Croquete", 4),
    17: ("Pastel de palmito", 6),
    18: ("Sanduíche natural", 9),
    19: ("Mini quiche", 8),
    20: ("Pão de batata", 5),
    21: ("Wrap pequeno", 9),
    22: ("Bolinho de bacalhau", 10),
    23: ("Salgado integral", 7),
    24: ("Mini coxinha vegana", 6)
}


@app.before_request
def ensure_session_lists():
    if "favorites" not in session:
        session["favorites"] = []

    if "carrinho" not in session:
        session["carrinho"] = []


@app.route("/")
def index():
    return render_template("index.html", menu=menu_items)


@app.route("/item/<int:item_id>")
def item(item_id):
    item = menu_items.get(item_id)

    if item:
        return render_template(
            "item.html",
            item=item,
            item_id=item_id
        )

    return "Item não encontrado", 404


# -------------------------
# FAVORITOS
# -------------------------

@app.route("/favoritos")
def favoritos():
    fav_ids = session.get("favorites", [])

    items = [
        (i, menu_items[i])
        for i in fav_ids
        if i in menu_items
    ]

    return render_template(
        "favoritos.html",
        items=items
    )


@app.route("/favoritar/<int:item_id>")
def favoritar(item_id):

    if item_id not in menu_items:
        return "Item não encontrado", 404

    favoritos = session.get("favorites", [])

    if item_id not in favoritos:
        favoritos.append(item_id)

    session["favorites"] = favoritos

    return redirect(url_for("favoritos"))


@app.route("/remover_favorito/<int:item_id>")
def remover_favorito(item_id):

    favoritos = session.get("favorites", [])

    if item_id in favoritos:
        favoritos.remove(item_id)

    session["favorites"] = favoritos

    return redirect(url_for("favoritos"))


# -------------------------
# CARRINHO
# -------------------------

@app.route("/adicionar_carrinho/<int:item_id>")
def adicionar_carrinho(item_id):

    if item_id not in menu_items:
        return "Item não encontrado", 404

    carrinho = session.get("carrinho", [])

    carrinho.append(item_id)

    session["carrinho"] = carrinho

    return redirect(url_for("carrinho"))


@app.route("/carrinho")
def carrinho():

    ids = session.get("carrinho", [])

    items = [
        (i, menu_items[i])
        for i in ids
        if i in menu_items
    ]

    total = sum(
        menu_items[i][1]
        for i in ids
        if i in menu_items
    )

    return render_template(
        "carrinho.html",
        items=items,
        total=total
    )


@app.route("/remover_carrinho/<int:item_id>")
def remover_carrinho(item_id):

    carrinho = session.get("carrinho", [])

    if item_id in carrinho:
        carrinho.remove(item_id)

    session["carrinho"] = carrinho

    return redirect(url_for("carrinho"))


# -------------------------
# CONTA / RESUMO
# -------------------------

@app.route("/conta")
def conta():

    ids = session.get("carrinho", [])

    itens = [
        (i, menu_items[i])
        for i in ids
        if i in menu_items
    ]

    total = sum(
        menu_items[i][1]
        for i in ids
        if i in menu_items
    )

    return render_template(
        "conta.html",
        itens=itens,
        total=total
    )


# -------------------------
# ABRIR NAVEGADOR
# -------------------------

def abrir_navegador():
    webbrowser.open("http://127.0.0.1:5000/")


if __name__ == "__main__":
    Timer(1, abrir_navegador).start()
    app.run(debug=True, use_reloader=False)