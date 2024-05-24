from flask import Flask, render_template, request
import requests

app = Flask(__name__)

DECK_API_BASE_URL = "https://deckofcardsapi.com/api/deck"
player_cards = []
dealer_cards = []
deck_id = None  # Inicializa a variável deck_id
player_score = 0  # Inicializa a pontuação do jogador
dealer_score = 0  # Inicializa a pontuação do dealer
dealer_stopped = False  # Flag para indicar se o dealer parou

def get_new_deck(deck_count=1):
    response = requests.get(f"{DECK_API_BASE_URL}/new/shuffle/?deck_count={deck_count}")
    return response.json()['deck_id']

def draw_cards(deck_id, count=2):
    response = requests.get(f"{DECK_API_BASE_URL}/{deck_id}/draw/?count={count}")
    if response.status_code == 200:
        data = response.json()
        if 'cards' in data:
            return data['cards']
        else:
            print("Erro: 'cards' não encontrado na resposta da API.")
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
    return []

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

def is_blackjack(cards):
    if len(cards) == 2:
        suits = {card['suit'] for card in cards}
        values = {card['value'] for card in cards}
        return 'SPADES' in suits and 'CLUBS' in suits and ('ACE' in values and ('10' in values or 'JACK' in values or 'QUEEN' in values or 'KING' in values))
    return False

@app.route('/', methods=['GET', 'POST'])
def home():
    global player_cards, dealer_cards, deck_id, player_score, dealer_score, dealer_stopped  # Declarando as variáveis globais
    message = ""  # Inicializa a mensagem

    if request.method == 'POST':
        option = request.form['option']
        player_score = calculate_score(player_cards)  # Calcula a pontuação do jogador antes de verificar a opção
        dealer_stopped = False  # Reseta a flag do dealer

        if option == '1':  # Hit
            new_cards = draw_cards(deck_id, 1)
            player_cards.extend(new_cards)
            player_score = calculate_score(player_cards)
            
            # Ação do dealer
            while dealer_score < 17:
                dealer_cards.extend(draw_cards(deck_id, 1))
                dealer_score = calculate_score(dealer_cards)

            if dealer_score >= 17:
                dealer_stopped = True

            if player_score > 21 or is_blackjack(player_cards) or dealer_score > 21 or is_blackjack(dealer_cards):
                return determine_winner()

            message = "O dealer parou." if dealer_stopped else ""

            return render_template('index.html', player_cards=player_cards, player_score=player_score, deck_id=deck_id, dealer_cards=dealer_cards, dealer_score=dealer_score, message=message)

        elif option == '2':  # Stand
            while dealer_score < 17:
                dealer_cards.extend(draw_cards(deck_id, 1))
                dealer_score = calculate_score(dealer_cards)

            return determine_winner()
        
        elif option == '3':  # Quit
            return "Obrigado por jogar! Até a próxima."

        elif option == '4':  # Hit 2 cartas
            new_cards = draw_cards(deck_id, 2)
            player_cards.extend(new_cards)
            player_score = calculate_score(player_cards)

            # Ação do dealer
            while dealer_score < 17:
                dealer_cards.extend(draw_cards(deck_id, 1))
                dealer_score = calculate_score(dealer_cards)

            if dealer_score >= 17:
                dealer_stopped = True

            if player_score > 21 or is_blackjack(player_cards) or dealer_score > 21 or is_blackjack(dealer_cards):
                return determine_winner()

            message = "O dealer parou." if dealer_stopped else ""

            return render_template('index.html', player_cards=player_cards, player_score=player_score, deck_id=deck_id, dealer_cards=dealer_cards, dealer_score=dealer_score, message=message)

    # Estado inicial do jogo
    deck_id = get_new_deck(1)
    player_cards = draw_cards(deck_id, 2)
    dealer_cards = draw_cards(deck_id, 2)
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    dealer_stopped = False  # Reseta a flag do dealer

    return render_template('index.html', player_cards=player_cards, player_score=player_score, deck_id=deck_id, dealer_cards=dealer_cards, dealer_score=dealer_score, message=message)

def determine_winner():
    global player_score, dealer_score, player_cards, dealer_cards
    if player_score > 21:
        result = f"Você estourou com uma pontuação de {player_score}! O dealer ganhou."
    elif dealer_score > 21:
        result = f"O dealer estourou com uma pontuação de {dealer_score}! Você ganhou."
    elif is_blackjack(player_cards):
        result = "Você fez um Blackjack! Você ganhou."
    elif is_blackjack(dealer_cards):
        result = "O dealer fez um Blackjack! O dealer ganhou."
    elif player_score == 21:
        result = "Você fez 21! Você ganhou."
    elif dealer_score == 21:
        result = "O dealer fez 21! O dealer ganhou."
    elif player_score > dealer_score:
        result = f"Você ganhou com uma pontuação de {player_score} contra {dealer_score} do dealer."
    elif player_score < dealer_score:
        result = f"O dealer ganhou com uma pontuação de {dealer_score} contra {player_score}."
    else:
        result = f"Empate com ambos tendo a pontuação de {player_score}."

    return render_template('result.html', player_cards=player_cards, player_score=player_score, dealer_cards=dealer_cards, dealer_score=dealer_score, result=result)

if __name__ == '__main__':
    app.run(debug=True)
