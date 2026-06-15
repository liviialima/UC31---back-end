from flask import Flask, session, redirect, url_for, flash, request, render_template_string

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_desafio'

TEMPLATE_HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Favoritos com Session</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        .container { max-width: 600px; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .produto, .favorito { display: flex; justify-content: space-between; padding: 10px; margin-bottom: 8px; border: 1px solid #ddd; border-radius: 4px; }
        .produto { background-color: #eef7ff; }
        .favorito { background-color: #ffeef2; }
        .btn { padding: 5px 10px; text-decoration: none; border: none; border-radius: 4px; cursor: pointer; color: white; }
        .btn-add { background-color: #28a745; }
        .btn-del { background-color: #dc3545; }
        .flash { padding: 10px; margin-bottom: 15px; border-radius: 4px; }
        .success { background-color: #d4edda; color: #155724; }
        .danger { background-color: #f8d7da; color: #721c24; }
        .info { background-color: #d1ecf1; color: #0c5460; }
    </style>
</head>
<body>
<div class="container">
    <h2> Sistema de Favoritos</h2>

    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        {% for category, message in messages %}
          <div class="flash {{ category }}">{{ message }}</div>
        {% endfor %}
      {% endif %}
    {% endwith %}

    <h3> Produtos Disponíveis</h3>
    
    <div class="produto">
        <span>Smartphone XYZ (R$ 1500)</span>
        <form action="/favoritos/adicionar" method="POST" style="margin:0;">
            <input type="hidden" name="id" value="1">
            <input type="hidden" name="nome" value="Smartphone XYZ">
            <button type="submit" class="btn btn-add">Favoritar</button>
        </form>
    </div>
    
    <div class="produto">
        <span>Notebook Pro (R$ 4500)</span>
        <form action="/favoritos/adicionar" method="POST" style="margin:0;">
            <input type="hidden" name="id" value="2">
            <input type="hidden" name="nome" value="Notebook Pro">
            <button type="submit" class="btn btn-add">Favoritar</button>
        </form>
    </div>

    <div class="produto">
        <span>Fone Bluetooth (R$ 250)</span>
        <form action="/favoritos/adicionar" method="POST" style="margin:0;">
            <input type="hidden" name="id" value="3">
            <input type="hidden" name="nome" value="Fone Bluetooth">
            <button type="submit" class="btn btn-add">Favoritar</button>
        </form>
    </div>

    <hr>

    <h3>Meus Favoritos ({% if favoritos %}{{ favoritos|length }}{% else %}0{% endif %})</h3>
    {% if favoritos %}
        {% for item in favoritos %}
            <div class="favorito">
                <span>{{ item.nome }} (ID: {{ item.id }})</span>
                <a href="/favoritos/remover/{{ item.id }}" class="btn btn-del">Remover</a>
            </div>
        {% endfor %}
    {% else %}
        <p style="color: #777;">Nenhum produto favoritado ainda.</p>
    {% endif %}
</div>
</body>
</html>
"""

@app.route('/')
@app.route('/favoritos')
def visualizar_favoritos():
    lista_favoritos = session.get('favoritos', [])
    return render_template_string(TEMPLATE_HTML, favoritos=lista_favoritos)

@app.route('/favoritos/adicionar', methods=['POST'])
def adicionar_favorito():
    id_produto = request.form.get('id')
    nome_produto = request.form.get('nome')
    
    novo_favorito = {'id': id_produto, 'nome': nome_produto}
    
    favoritos = session.get('favoritos', [])
    
    if novo_favorito not in favoritos:
        favoritos.append(novo_favorito)
        session['favoritos'] = favoritos 
        session.modified = True          
        flash(f'"{nome_produto}" foi adicionado aos seus favoritos!', 'success')
    else:
        flash(f'"{nome_produto}" já está na sua lista de favoritos.', 'info')
        
    return redirect(url_for('visualizar_favoritos'))


@app.route('/favoritos/remover/<id_produto>')
def remover_favorito(id_produto):
    favoritos = session.get('favoritos', [])
    
    favoritos_atualizados = [p for p in favoritos if p['id'] != str(id_produto)]
    
    session['favoritos'] = favoritos_atualizados
    session.modified = True
    
    flash('Produto removido dos favoritos.', 'danger')
    return redirect(url_for('visualizar_favoritos'))


if __name__ == '__main__':
    app.run(debug=True)
