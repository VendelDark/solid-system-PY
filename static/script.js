// let deckId = '';
// let jogadorPontuacao = 0;
// let dealerPontuacao = 0;

// function exibirMensagem(mensagem) {
//     const mensagemElement = document.getElementById('mensagem');
//     mensagemElement.textContent = mensagem;
// }

// function iniciarJogo() {
//     fetch('https://deckofcardsapi.com/api/deck/new/shuffle/')
//         .then(response => response.json())
//         .then(data => {
//             deckId = data.deck_id;
//             exibirMensagem('Jogo iniciado. Clique em "Pedir Carta" para receber suas cartas.');
//             jogadorPontuacao = 0;
//             dealerPontuacao = 0;
//             document.getElementById('pontuacao-jogador').textContent = '';
//             document.getElementById('pontuacao-dealer').textContent = '';
//             document.getElementById('cartas-jogador').innerHTML = '';
//             document.getElementById('cartas-dealer').innerHTML = '';
//         })
//         .catch(error => {
//             console.error('Erro ao iniciar jogo:', error);
//             exibirMensagem('Erro ao iniciar jogo. Por favor, tente novamente.');
//         });
// }

// function pedirCarta() {
//     fetch(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=1`)
//         .then(response => response.json())
//         .then(data => {
//             const carta = data.cards[0];
//             const valorCarta = obterValorCarta(carta);
//             jogadorPontuacao += valorCarta;
//             document.getElementById('pontuacao-jogador').textContent = `Pontuação do Jogador: ${jogadorPontuacao}`;
//             document.getElementById('cartas-jogador').innerHTML += `<img src="${carta.image}" alt="${carta.code}">`;
//             if (jogadorPontuacao > 21) {
//                 exibirMensagem('Você estourou! Fim de jogo.');
//                 pararJogo();
//             }
//         })
//         .catch(error => {
//             console.error('Erro ao pedir carta:', error);
//             exibirMensagem('Erro ao pedir carta. Por favor, tente novamente.');
//         });
// }

// function pararJogo() {
//     fetch(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=2`)
//         .then(response => response.json())
//         .then(data => {
//             const cartasDealer = data.cards;
//             const valorCartasDealer = cartasDealer.map(carta => obterValorCarta(carta));
//             dealerPontuacao = valorCartasDealer.reduce((total, valor) => total + valor, 0);
//             document.getElementById('pontuacao-dealer').textContent = `Pontuação do Dealer: ${dealerPontuacao}`;
//             cartasDealer.forEach(carta => {
//                 document.getElementById('cartas-dealer').innerHTML += `<img src="${carta.image}" alt="${carta.code}">`;
//             });
//             while (dealerPontuacao < 17) {
//                 pedirCartaDealer();
//             }
//             determinarVencedor();
//         })
//         .catch(error => {
//             console.error('Erro ao parar jogo:', error);
//             exibirMensagem('Erro ao parar jogo. Por favor, tente novamente.');
//         });
// }

// function pedirCartaDealer() {
//     fetch(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=1`)
//         .then(response => response.json())
//         .then(data => {
//             const carta = data.cards[0];
//             const valorCarta = obterValorCarta(carta);
//             dealerPontuacao += valorCarta;
//             document.getElementById('pontuacao-dealer').textContent = `Pontuação do Dealer: ${dealerPontuacao}`;
//             document.getElementById('cartas-dealer').innerHTML += `<img src="${carta.image}" alt="${carta.code}">`;
//         })
//         .catch(error => {
//             console.error('Erro ao pedir carta do Dealer:', error);
//         });
// }

// function determinarVencedor() {
//     if (jogadorPontuacao > 21) {
//         exibirMensagem('Você perdeu! Sua pontuação passou de 21.');
//     } else if (dealerPontuacao > 21 || jogadorPontuacao > dealerPontuacao) {
//         exibirMensagem('Parabéns! Você ganhou.');
//     } else if (jogadorPontuacao < dealerPontuacao) {
//         exibirMensagem('Você perdeu! O Dealer ganhou.');
//     } else {
//         exibirMensagem('Empate! Ninguém ganhou.');
//     }
// }

// function obterValorCarta(carta) {
//     const valor = carta.value;
//     if (['JACK', 'QUEEN', 'KING'].includes(valor)) {
//         return 10;
//     } else if (valor === 'ACE') {
//         return 11;
//     } else {
//         return parseInt(valor);
//     }
// }