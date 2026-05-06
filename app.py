@app.template("/")
def template():
    return render_template('login')


from Flask import flask

app = Flask(__name__)

@app.route("/")
def home():
    return "olá, mundo!"

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/operacao/<tipo>/<float:n1>/<float:n2>')
def operacao(n1, n2):
    if tipo == 'Soma':
        resultado = n1 + n2
    elif tipo == 'Subtração':
        resultado = n1 - n2
    elif tipo == 'Divisão':
        resultado = n1 / n2
    else:
        resultado = n1 * n2
        return resultado
    
    #Questão 01
     
    @app.route('/saudacao/<nome>')
    def saudacao(nome):
        return f'ola,{nome}'
    
    #Questão 02

    @app.route('/somar, defaults={"n1": "0", "n2":"0",}')
    def soma(n1,n2):
        resultado = n1+n2


   #Questão 03 

@app.route('/idade/<nome>/<int:idade>')
def verificar_idade(nome, idade):
    if idade <= 18:
        return f"Olá {nome} Você é de menor"
    else:
        return "Você é de maior"

#Questão 04

@app.route('/produto/<nome>/<float:preco> ')
def produto(nome, preço):
    return f'O produto{nome} custa R$ {preço:.2f}'




 

