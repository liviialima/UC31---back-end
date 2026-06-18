from flask import Flask, render_template, request
from flask import session, redirect, url_for, jsonify

app = Flask(__name__)

menu_items = {
    1: ("Brigadeiro", 5),
    2: ("Beijinho", 5),
    3: ("Brownie", 8),
    4: ("Gelatina colorida", 4),
    5: ("Mousse de maracujá", 7),
    6: ("Quindim", 9),
    7: ("Banoffee", 10),
    8: ("Sorvete artesanal", 5),
    9: ("Gelatina sem açúcar", 6),
    10: ("Mousse de chocolate", 10),
    11: ("Cookies", 3),
    12: ("Waffles", 8),
    13: ("Churros", 4),
    14: ("Pudim", 8),
    15: ("Tiramisu", 8),
    16: ("Doce de banana", 8),
    17: ("Petit Gateau", 15),
    18: ("Palha Italiana", 9),
    19: ("Cajuzinho", 8),
    20: ("Sonho", 8),
    21: ("Marshmallows", 8),
    22: ("Pavê", 8),
    23: ("Cupcake", 8),
    24: ("Macarons", 4),
}

@app.route("/")
def index():
    return render_template("index.html", menu=menu_items)

@app.route("/comprar", methods=["POST"])
def comprar():
    pedidos = request.form.getlist("item")
    pedidos = list(map(int, pedidos))
    total = sum(menu_items[i][1] for i in pedidos if i in menu_items)
    escolhidos = [menu_items[i][0] for i in pedidos]
    return render_template("resultado.html", total=total, escolhidos=escolhidos)

if __name__ == "__main__":
    # favoriting system using server-side session
    app.secret_key = "dev-secret-change-me"


    @app.route("/favorito/toggle/<int:item_id>", methods=["POST"])
    def toggle_favorite(item_id):
        favorites = session.get("favorites", [])
        if item_id in favorites:
            favorites.remove(item_id)
            action = "removed"
        else:
            if item_id in menu_items:
                favorites.append(item_id)
                action = "added"
            else:
                return jsonify({"status": "error", "message": "item not found"}), 404
        session["favorites"] = favorites
        # support AJAX toggle or normal form submit
        if request.is_json or request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"status": "ok", "action": action, "favorites": favorites})
        return redirect(request.referrer or url_for("index"))

    @app.route("/favoritos")
    def favoritos():
        favorites = session.get("favorites", [])
        escolhidos = [menu_items[i][0] for i in favorites if i in menu_items]
        total = sum(menu_items[i][1] for i in favorites if i in menu_items)
        return render_template("favoritos.html", escolhidos=escolhidos, total=total, favorites=favorites)

    app.run(debug=True)