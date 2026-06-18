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

def calcular_total(pedidos):
    total = sum(menu_items[item][1] for item in pedidos if item in menu_items)
    return total

pedidos = [1, 3, 7]  # Brigadeiro, Brownie, Banoffee
print("Total da compra: R$", calcular_total(pedidos))