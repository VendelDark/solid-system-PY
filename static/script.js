// Função para exibir mensagem na tela
function exibirMensagem(mensagem) {
    const mensagemElement = document.getElementById('mensagem');
    mensagemElement.textContent = mensagem;
}

// Função para iniciar o jogo
function iniciarJogo() {
    fetch('/iniciar-jogo')
        .then(response => response.json())
        .then(data => {
            exibirMensagem('Jogo iniciado com sucesso!');
            // Aqui você pode implementar a lógica para exibir as cartas do jogador e do dealer
        })
        .catch(error => {
            console.error('Erro ao iniciar o jogo:', error);
            exibirMensagem('Erro ao iniciar o jogo. Por favor, tente novamente.');
        });
}

// Função para pedir uma carta
function pedirCarta() {
    fetch('/pedir-carta')
        .then(response => response.json())
        .then(data => {
            // Aqui você pode implementar a lógica para exibir a carta que foi pedida
            exibirMensagem('Carta pedida com sucesso!');
        })
        .catch(error => {
            console.error('Erro ao pedir uma carta:', error);
            exibirMensagem('Erro ao pedir uma carta. Por favor, tente novamente.');
        });
}

// Função para parar o jogo
function pararJogo() {
    fetch('/parar-jogo')
        .then(response => response.json())
        .then(data => {
            // Aqui você pode implementar a lógica para mostrar o resultado do jogo
            exibirMensagem('Jogo encerrado!');
        })
        .catch(error => {
            console.error('Erro ao parar o jogo:', error);
            exibirMensagem('Erro ao parar o jogo. Por favor, tente novamente.');
        });
}