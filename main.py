from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/embaralhar-baralho')
def embaralhar_baralho():
    response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/')
    data = response.json()
    return jsonify(data)

@app.route('/desenhar-cartas')
def desenhar_cartas():
    deck_id = request.args.get('deck_id')
    count = request.args.get('count')
    response = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}')
    data = response.json()
    return jsonify(data)

@app.route('/embaralhar-pilha')
def embaralhar_pilha():
    deck_id = request.args.get('deck_id')
    pile_name = request.args.get('pile_name')
    response = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/shuffle/')
    data = response.json()
    return jsonify(data)

@app.route('/listar-cartas-pilha')
def listar_cartas_pilha():
    deck_id = request.args.get('deck_id')
    pile_name = request.args.get('pile_name')
    response = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/list/')
    data = response.json()
    return jsonify(data)

@app.route('/desenhar-cartas-pilha')
def desenhar_cartas_pilha():
    deck_id = request.args.get('deck_id')
    pile_name = request.args.get('pile_name')
    response = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/draw/')
    data = response.json()
    return jsonify(data)

@app.route('/retornar-cartas')
def retornar_cartas():
    deck_id = request.args.get('deck_id')
    response = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/pile/default/draw/?cards=AS,2S')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
