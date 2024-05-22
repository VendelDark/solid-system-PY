from flask import Flask, render_template, request
import requests

app = Flask(__name__)

DECK_API_BASE_URL = "https://deckofcardsapi.com/api/deck"
player_cards = []
new_cards = []
deck_id = None  # Inicializa a variável deck_id

def get_new_deck(deck_count=1):
    response = requests.get(f"{DECK_API_BASE_URL}/new/shuffle/?deck_count={deck_count}")
    return response.json()['deck_id']

def draw_cards(deck_id, count=2):
    response = requests.get(f"{DECK_API_BASE_URL}/{deck_id}/draw/?count={count}")
    return response.json()['cards']

def calculate_score(cards):
    score = 0
    ace_count = 0
    value_map = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'JACK': 10, 'QUEEN': 10, 'KING': 10, 'ACE': 11
    }
    for card in cards:
        value = card['value']
        if value.upper() in value_map:
            score += value_map[value.upper()]
            if value == 'ACE':
                ace_count += 1
        else:
            print(f"Carta não reconhecida: {value}")
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score

@app.route('/', methods=['GET', 'POST'])
def home():
    global player_cards, new_cards, deck_id  # Declarando as variáveis globais
    if request.method == 'POST':
        option = request.form['option']
        if option == '1':  # Hit
            new_cards = draw_cards(deck_id, 1)
            player_cards.extend(new_cards)
            player_score = calculate_score(player_cards)
            if player_score > 21:
                message = f"Você estourou com uma pontuação de {player_score}!"
                return render_template('index.html', message=message, player_cards=player_cards, player_score=player_score, deck_id=deck_id)
            return render_template('index.html', player_cards=player_cards, player_score=player_score, deck_id=deck_id)
        elif option == '2':  # Stand
            dealer_cards = draw_cards(deck_id, 2)
            dealer_score = calculate_score(dealer_cards)
            result = ""
            if 'player_score' in locals():
                if dealer_score > 21 or dealer_score < player_score:
                    result = "Você ganhou!"
                elif dealer_score == player_score:
                    result = "Empate!"
                else:
                    result = "O dealer ganhou!"
            return render_template('result.html', player_cards=player_cards, player_score=player_score, dealer_cards=dealer_cards, dealer_score=dealer_score, result=result)
        elif option == '3':  # Quit
            return "Obrigado por jogar! Até a próxima."

    # Estado inicial do jogo
    deck_id = get_new_deck(1)
    initial_cards = draw_cards(deck_id, 2)
    player_cards = initial_cards
    player_score = calculate_score(player_cards)
    for card in player_cards:
        card['image_url'] = card['image']  # Adiciona a URL da imagem à carta
    return render_template('index.html', player_cards=player_cards, player_score=player_score, deck_id=deck_id)

if __name__ == '__main__':
    app.run(debug=True)
