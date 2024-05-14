from flask import Flask, jsonify
from blackjack import iniciar_jogo, pedir_carta, parar_j

import requests
import json

# Função para embaralhar o baralho
def embaralhar_baralho():
    response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/")
    data = response.json()
    deck_id = data['deck_id']
    return deck_id

# Função para desenhar cartas do baralho
def desenhar_cartas(deck_id, count):
    response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}")
    data = response.json()
    cards = data['cards']
    return cards

# Função para iniciar o jogo
def iniciar_jogo():
    deck_id = embaralhar_baralho()
    jogador = desenhar_cartas(deck_id, 2)
    dealer = desenhar_cartas(deck_id, 2)
    return deck_id, jogador, dealer

# Função para pedir uma carta
def pedir_carta(deck_id):
    carta = desenhar_cartas(deck_id, 1)
    return carta

# Função para parar o jogo e mostrar o resultado
def parar_jogo(deck_id, jogador, dealer):
    # Lógica para determinar o vencedor e mostrar o resultado
    # Aqui você deve implementar a lógica do jogo de Blackjack
    resultado = "Implemente a lógica do jogo aqui"
    return resultado