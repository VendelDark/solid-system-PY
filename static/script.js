function exibirMensagem(mensagem) {
    const mensagemElement = document.getElementById('mensagem');
    mensagemElement.textContent = mensagem;
}

function embaralharBaralho() {
    fetch('https://deckofcardsapi.com/api/deck/new/shuffle/')
        .then(response => response.json())
        .then(data => {
            exibirMensagem('Baralho embaralhado com sucesso!');
        })
        .catch(error => {
            console.error('Erro ao embaralhar baralho:', error);
            exibirMensagem('Erro ao embaralhar baralho. Por favor, tente novamente.');
        });
}

function desenharCartas() {
    const deckId = prompt('Digite o ID do baralho:');
    const count = prompt('Digite a quantidade de cartas a desenhar:');

    fetch(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=${count}`)
        .then(response => response.json())
        .then(data => {
            // Exibir as cartas desenhadas
            const cartas = data.cards.map(card => `<img src="${card.image}" alt="${card.code}">`);
            document.getElementById('cartas').innerHTML = cartas.join('');
            exibirMensagem('Cartas desenhadas com sucesso!');
        })
        .catch(error => {
            console.error('Erro ao desenhar cartas:', error);
            exibirMensagem('Erro ao desenhar cartas. Por favor, tente novamente.');
        });
}

function embaralharPilha() {
    const deckId = prompt('Digite o ID do baralho:');
    const pileName = prompt('Digite o nome da pilha:');

    fetch(`https://deckofcardsapi.com/api/deck/${deckId}/pile/${pileName}/shuffle/`)
        .then(response => response.json())
        .then(data => {
            exibirMensagem('Pilha embaralhada com sucesso!');
        })
        .catch(error => {
            console.error('Erro ao embaralhar pilha:', error);
            exibirMensagem('Erro ao embaralhar pilha. Por favor, tente novamente.');
        });
}

function listarCartasPilha() {
    const deckId = prompt('Digite o ID do baralho:');
    const pileName = prompt('Digite o nome da pilha:');

    fetch(`https://deckofcardsapi.com/api/deck/${deckId}/pile/${pileName}/list/`)
        .then(response => response.json())
        .then(data => {
            // Exibir as cartas da pilha
            const cartasPilha = data.piles[pileName].cards.map(card => `<img src="${card.image}" alt="${card.code}">`);
            document.getElementById('cartasPilha').innerHTML = cartasPilha.join('');
            exibirMensagem('Cartas da pilha listadas com sucesso!');
        })
        .catch(error => {
            console.error('Erro ao listar cartas da pilha:', error);
            exibirMensagem('Erro ao listar cartas da pilha. Por favor, tente novamente.');
        });
}

function desenharCartasPilha() {
    const deckId = prompt('Digite o ID do baralho:');
    const pileName = prompt('Digite o nome da pilha:');

    fetch(`https://deckofcardsapi.com/api/deck/${deckId}/pile/${pileName}/draw/`)
        .then(response => response.json())
        .then(data => {
            // Exibir as cartas desenhadas da pilha
            const cartasPilhaDesenhadas = data.cards.map(card => `<img src="${card.image}" alt="${card.code}">`);
            document.getElementById('cartasPilhaDesenhadas').innerHTML = cartasPilhaDesenhadas.join('');
            exibirMensagem('Cartas da pilha desenhadas com sucesso!');
        })
        .catch(error => {
            console.error('Erro ao desenhar cartas da pilha:', error);
            exibirMensagem('Erro ao desenhar cartas da pilha. Por favor, tente novamente.');
        });
}

function retornarCartas() {
    const deckId = prompt('Digite o ID do baralho:');

    fetch(`https://deckofcardsapi.com/api/deck/${deckId}/pile/default/draw/?cards=AS,2S`)
        .then(response => response.json())
        .then(data => {
            exibirMensagem('Cartas retornadas com sucesso!');
        })
        .catch(error => {
            console.error('Erro ao retornar cartas:', error);
            exibirMensagem('Erro ao retornar cartas. Por favor, tente novamente.');
        });
}