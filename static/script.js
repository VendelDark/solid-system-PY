
function exibirMensagem(mensagem) {
    const mensagemElement = document.getElementById('mensagem');
    mensagemElement.textContent = mensagem;
}

function embaralharBaralho() {
    fetch('/embaralhar-baralho')
        .then(response => response.json())
        .then(data => {
            exibirMensagem('Baralho embaralhado com sucesso!');
        })
        .catch(error => {
            console.error('Erro ao embaralhar baralho:', error);
            exibirMensagem('Erro ao desenhar cartas. Por favor, tente novamente.');
        });
    }
function desenharCartasPilha(){
fetch(`/desenhar-cartas/${deckId}/${count}`)
.then(response => response.json())
.then(data => {
    // Exibir as cartas desenhadas
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

fetch(`/embaralhar-pilha/${deckId}/${pileName}`)
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

fetch(`/listar-cartas-pilha/${deckId}/${pileName}`)
.then(response => response.json())
.then(data => {
    // Exibir as cartas da pilha
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

fetch(`/desenhar-cartas-pilha/${deckId}/${pileName}/draw`)
.then(response => response.json())
.then(data => {
    // Exibir as cartas desenhadas da pilha
    exibirMensagem('Cartas da pilha desenhadas com sucesso!');
})
.catch(error => {
    console.error('Erro ao desenhar cartas da pilha:', error);
    exibirMensagem('Erro ao desenhar cartas da pilha. Por favor, tente novamente.');
});
}

function retornarCartas() {
const deckId = prompt('Digite o ID do baralho:');

fetch(`/retornar-cartas/${deckId}`)
.then(response => response.json())
.then(data => {
    exibirMensagem('Cartas retornadas com sucesso!');
})
.catch(error => {
    console.error('Erro ao retornar cartas:', error);
    exibirMensagem('Erro ao retornar cartas. Por favor, tente novamente.');
});
}