from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/embaralhar-baralho')
def embaralhar_baralho():
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/desenhar-cartas/<deck_id>/<int:count>')
def desenhar_cartas(deck_id, count):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/embaralhar-pilha/<deck_id>/<pile_name>')
def embaralhar_pilha(deck_id, pile_name):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/shuffle/"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/listar-cartas-pilha/<deck_id>/<pile_name>')
def listar_cartas_pilha(deck_id, pile_name):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/list/"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/desenhar-cartas-pilha/<deck_id>/<pile_name>/draw')
def desenhar_cartas_pilha(deck_id, pile_name):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/draw/"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/retornar-cartas/<deck_id>')
def retornar_cartas(deck_id):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/return/"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)